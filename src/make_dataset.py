from pathlib import Path
import subprocess
import zipfile

api = "kaggle datasets download -d mlg-ulb/creditcardfraud"
curr_path = Path.cwd()
def download_data():
    Path("data/kaggle_data").mkdir(parents=True,exist_ok=True)
    
    download_command = api
    subprocess.run(download_command,shell=True,check=True,cwd=Path("data/kaggle_data"))
    print("Dataset Downloaded Successfully")

def unzip_data():
    path_to_zip_file = Path('data/kaggle_data/creditcardfraud.zip')
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
       zip_ref.extractall(Path("data/raw"))
    

if Path("data/kaggle_data").exists:
    download_data()
    unzip_data()
else:
    print("data already downloaded")