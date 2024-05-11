import os
from pathlib import Path

import logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)


package_name = 'project name'                                                   # Change the project name

list_of_files = [
    
    "LICENSE",
    "README.md",
    "images/.gitkeep",                                                          # supporting images for github readme
    
    "setup.py",
    "requirements.txt",
    
    "notebooks/experiments.ipynb",
    "config/config.yaml",
    "params.yaml",
    
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/config/configuration.py",
    f"src/{package_name}/constants/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/training_stages/__init__.py",
    f"src/{package_name}/training_stages/stage_01_data_ingestion.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/pipeline/training_pipeline.py",
    f"src/{package_name}/pipeline/prediction_pipeline.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/common.py",
    
    "dvc.yaml",
    
    'app.py',                                                                   # for creating the flask application 
    'templates/index.html',                                                     # for creating the ui for the application
    'static/styles.css',
    
    "Dockerfile",
    ".github/workflows/main.yaml",
    
    # 'tests/unit/__init__.py',                            # folder for unit testing
    # 'tests/unit/unit.py',
    # 'tests/integration/__init__.py',                     # folder for integration testing
    # 'tests/integration/integration.py',
    # 'setup.cfg',
    # 'pyproject.toml',
    # 'tox.ini',                                          # to test the project in the local environment

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory -> {filedir}; for the file -> {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file -> {filepath}")
    else:
        logging.info(f"--- {filename} is already exists ---")