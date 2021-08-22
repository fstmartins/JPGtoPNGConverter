import sys
import os

from PIL import Image

# grab first and second argument
origin_folder = sys.argv[1]
destination_folder = sys.argv[2]


# check if is new or already exists, and create in the first case

def create_new_folder(folder):
    try:
        os.mkdir(folder)
    except OSError as error:
        print(error)
        print('Performing the action on the existing folder')


def check_folder_exists(folder):
    for root, dirs, files in os.walk('.'):
        for element in dirs:
            if element == folder:
                return True
    return False


# convert images to png and saves them
def convert_images(origin_folder, destination_folder):
    if os.access(origin_folder, os.R_OK):
        for root, dirs, files in os.walk(origin_folder):
            for element in files:
                origin_path = origin_folder + '/' + element
                pokemon = Image.open(origin_path)
                new_pokemon = element[:-3] + 'png'
                destin_path = destination_folder + '/' + new_pokemon
                pokemon.save(destin_path)


def run_script(origin_folder, destination_folder):
    if not check_folder_exists(origin_folder):
        print(f'{origin_folder} folder does not exist in current directory')
        raise FileNotFoundError
    create_new_folder(destination_folder)
    convert_images(origin_folder, destination_folder)


run_script(origin_folder, destination_folder)

