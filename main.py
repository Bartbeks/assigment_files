__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
# from importlib.metadata import files

import os
import zipfile
from pathlib import Path


files_path = Path(__file__).parent/"data.zip"
cache_path = Path(__file__).parent/"cache"
abs_path = Path(cache_path).absolute()


def clean_cache():
    if not os.path.exists(cache_path):
        os.mkdir(cache_path)
    else:
        for file_name in os.listdir(cache_path):
            file = os.path.join(cache_path, file_name)
            if os.path.isfile(file):
                os.remove(file)
        return


def cache_zip(zip_file_path, cache_dir_path):
    file_dir = zip_file_path.replace("data.zip", "").strip()
    for _ in os.listdir(file_dir):
        if os.path.isfile(zip_file_path):
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(cache_dir_path)
        return


def cached_files():
    text_files = []
    for file_name in os.listdir(abs_path):
        if os.path.isabs(abs_path.joinpath(file_name)):
            text_files.append(abs_path.joinpath(file_name).__str__())
    return text_files


def find_password(files):
    index = 0
    for file_name in files:
        with open(os.path.join(abs_path, file_name), "r"):
            file = open(os.path.join(abs_path, file_name), "r")
        for line in file:
            index += 1
            if 'password' in line:
                password = line.split(":")
                file.close()
                return str(password[1]).strip()


clean_cache()
cache_zip(str(files_path), str(cache_path))
cached_files()
find_password(cached_files())
