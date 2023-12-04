import os
import argparse
import pandas as pd
import datetime
from sentence_transformers import SentenceTransformer, util

# Initialize Sentence Transformer Model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def convert_date_format(date_str, input_format, output_format):
    try:
        date_obj = datetime.datetime.strptime(date_str, input_format)
        return date_obj.strftime(output_format)
    except ValueError:
        return date_str

def map_columns_with_sentence_transformers(source_df, template_df):
    mappings = {}
    for src_col in source_df.columns:
        max_score = 0
        matched_col = None
        for tpl_col in template_df.columns:
            # Craft a prompt to check similarity between column names
            prompt = f"{src_col} {tpl_col}"
            
            # Compute the similarity score between column names
            score = util.pytorch_cos_sim(model.encode(src_col), model.encode(tpl_col)).item()
            
            if score > max_score:
                max_score = score
                matched_col = tpl_col
        
        if matched_col:
            mappings[src_col] = matched_col
    return mappings

def convert_table(source_csv, template_csv, target_csv):
    template_path = os.path.join('templates', template_csv)
    
    source_df = pd.read_csv(source_csv)
    template_df = pd.read_csv(template_path)
   
    mappings = map_columns_with_sentence_transformers(source_df, template_df)
    
    target_df = pd.DataFrame()
    for src_col, tpl_col in mappings.items():
        if tpl_col == 'Date':
            target_df[tpl_col] = source_df[src_col].apply(lambda x: convert_date_format(x, '%d/%m/%Y', '%m-%d-%Y'))
        else:
            target_df[tpl_col] = source_df[src_col]

    # Ensure the 'targets' directory exists
    if not os.path.exists('targets'):
        os.makedirs('targets')
        
    # Save the target_df to the 'targets' directory
    target_path = os.path.join('targets', target_csv)
    target_df.to_csv(target_path, index=False)
    

def main():
    parser = argparse.ArgumentParser(description='Convert source CSV to match template CSV format.')
    parser.add_argument('--source', required=True, help='Path to the source CSV file')
    parser.add_argument('--template', required=True, help='Path to the template CSV file')
    parser.add_argument('--target', required=True, help='Path to save the converted target CSV file')
    
    args = parser.parse_args()
    convert_table(args.source, args.template, args.target)

if __name__ == "__main__":
    main()
