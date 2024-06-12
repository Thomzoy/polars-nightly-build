import os
import shutil
import subprocess
import tempfile
from pathlib import Path

REPO_URL = "https://github.com/pola-rs/polars.git" # f"https://github.com/Thomzoy/{REPO_NAME}.git"

import subprocess

def get_latest_tag():
    try:
        # Run the git command to get the latest tag
        result = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'], stdout=subprocess.PIPE)
        # Decode the output and return it
        latest_tag = result.stdout.decode().strip()
        return latest_tag
    except Exception as e:
        print("Error:", e)
        return None

def install_tag(tag):
    subprocess.run(['git', 'checkout', f"tags/{tag}"], check=True)
    subprocess.run(['pip', 'install', "-y" ,"*.whl"], check=True, cwd="./dist")

def install(tag=None):
    try:
        subprocess.run(['git', 'fetch', '--all'], check=True)
        tag = tag or get_latest_tag()

        install_tag(tag)

    except subprocess.CalledProcessError as e:
        print("Error:", e)

install()