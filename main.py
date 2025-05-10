import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])



# Чтение файла requirements.txt и установка библиотек
with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Установка {package}...")
        install(package)

