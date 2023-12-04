### Project: CSV Table Converter

This project provides a tool to convert source CSV tables to match a given template CSV format. It uses Hugging Face's Sentence Transformers to map columns semantically and transforms the values as needed to align with the template. The project includes creating a virtual environment and installing necessary packages.

### Prerequisites

- Python 3.6 or higher
- pip (Python’s package installer)

### Setup

1. **Clone the Repository**

   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

   Replace `<repository_url>` with the URL of your Git repository and `<repository_directory>` with the name of your project directory.
2. **Create a Virtual Environment**

   Run the `create_env.py` script to create a virtual environment and install the required packages.

   ```sh
   python create_env.py
   ```

   This will create a virtual environment named `myenv` and install the packages listed in `requirements.txt` into this environment.
3. **Activate the Virtual Environment**

   - On Windows:

     ```sh
     myenv\Scripts\activate
     ```
   - On MacOS/Linux:

     ```sh
     source myenv/bin/activate
     ```

### Usage

After setting up and activating the virtual environment, you can run the `convert_table.py` script to convert your source CSV to match the template CSV format.

```sh
python convert_table.py --source <path_to_source_csv> --template <path_to_template_csv> --target <path_to_target_csv>
```

Replace `<path_to_source_csv>`, `<path_to_template_csv>`, and `<path_to_target_csv>` with the actual paths to your source, template, and target CSV files, respectively.

### Example

```sh
python convert_table.py --source source.csv --template template.csv --target target.csv
python convert_table.py --source data/table_A.csv --template template.csv --target target.csv
```

### Output

The script will create a new CSV file specified by `--target`, with the structure (columns and value formats) as defined in the Template CSV file, and the values in this file will be populated from the corresponding columns in the Source CSV file after applying the necessary transformations.

### Deactivate Virtual Environment

Once you are done, you can deactivate the virtual environment:

```sh
deactivate
```

### Troubleshooting

If you encounter any issues while setting up or running the scripts, please check the following:

- Ensure you have the correct Python version installed.
- Ensure the virtual environment is activated before running `convert_table.py`.
- Check the paths provided to the scripts are correct.
- Ensure the `requirements.txt` and Python scripts are in the current working directory while creating the virtual environment.

### Conclusion

This project provides a convenient tool to map and transform CSV tables to conform to a given template, utilizing the semantic similarity capabilities of Sentence Transformers from Hugging Face. Make sure to follow the setup instructions carefully to install the necessary packages in a virtual environment.
