import os
import subprocess
import sys

def create_virtual_env(env_name, requirements_file):
    # Create a virtual environment
    subprocess.run([sys.executable, '-m', 'venv', env_name])
    
    # Activate the virtual environment
    activate_file = os.path.join(env_name, 'Scripts', 'activate') if sys.platform == 'win32' else os.path.join(env_name, 'bin', 'activate')
    activate_command = f'source {activate_file}' if sys.platform != 'win32' else activate_file
    
    # Install packages from requirements.txt
    install_command = f'{activate_command} && pip install -r {requirements_file}'
    os.system(install_command)

if __name__ == "__main__":
    env_name = 'convert_tables'
    requirements_file = 'requirements.txt'
    create_virtual_env(env_name, requirements_file)
    print(f"Virtual environment {env_name} has been created and packages have been installed.")