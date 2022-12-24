from PIL import Image
import os
import random

path = "photo"
size_one = (120, 80)
size_two = (350, 250)


def select_from_a_folder():
    paths = []
    for directory, folder, files in os.walk(path):
        for i in files:
            paths.append(i)
    return paths


def photo_processing():
    for file_path in select_from_a_folder():
        try:
            image_one = Image.open(f"photo/{file_path}")
            image_two = Image.open(f"photo/{file_path}")
            image_one.thumbnail(size=size_one)
            image_two.thumbnail(size=size_two)
            image_one.save(fp=f"miniatures/{random.randint(0, 10000)}{file_path}")
            print(f"{file_path} saved (120, 80)")
            image_two.save(fp=f"miniatures/{random.randint(0, 10000)}{file_path}")
            print(f"{file_path} saved (350, 250)")
        except:
            print(f"{file_path} - not picture")


def main():
    photo_processing()


if __name__ == "__main__":
    main()
