#%%
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Paths
ROOT_PATH = Path(__file__).parent
ZIP_DIR_PATH = ROOT_PATH / '13_dir_zip'
ZIPPED_PATH = ROOT_PATH / '13_zipped.zip'
UNZIPPED_PATH = ROOT_PATH / '13_unzipped'

# Removing all previous dirs and files 
shutil.rmtree(ZIP_DIR_PATH, ignore_errors=True)
Path.unlink(ZIPPED_PATH,missing_ok=True)
shutil.rmtree(str(ZIPPED_PATH).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(UNZIPPED_PATH, ignore_errors=True)

# Creating dir
ZIP_DIR_PATH.mkdir(exist_ok=True)

# Function to create files
def create_files(qty: int, zip_dir: Path):
    for i in range(1, qty):
        text = 'file_%s' %i # string interpolation
        with open(zip_dir / f'{text}.txt', 'w') as file:
            file.write(text)

# Creating files
create_files(6, ZIP_DIR_PATH)

# Creating zipped file and adding files
with ZipFile(ZIPPED_PATH, 'w') as zip_file:
    for root, dirs, files in os.walk(ZIP_DIR_PATH):
        for file in files:
            zip_file.write(os.path.join(root, file), file)

# Extracting files to a specific directory
with ZipFile(ZIPPED_PATH, 'r') as unzipped_file:
    unzipped_file.extractall(UNZIPPED_PATH)
        