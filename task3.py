import random
import os
import shutil
import csv
from email import generator


def create_dir(dir_name: str) -> str:
    """This function create directory "dataset2" where we must copy our dataset"""
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    return dir_name


def get_element(class_name: str) -> generator:
    """this function returns us a list of names in the dataset class"""
    for file_name in os.listdir(os.path.join("dataset", class_name)):
        yield file_name


def create_randname_file(dataset: str, annotation_name: str, dir_copy: str) -> None:
    """This function creates a copy of the dataset so that each file from the source dataset receives a random number
    from 0 to 10000, and the dataset is the following structure dataset/number.jpg. """
    file_number = list(range(10001))
    random.shuffle(file_number)
    count = 1
    create_dir(dir_copy)
    for dataset_class in os.listdir("dataset"):
        for file_name in get_element(dataset_class):
            shutil.copy(os.path.join(os.path.join("dataset", dataset_class), file_name),
                        os.path.join(dir_copy, f"{file_number[count]}.jpg"))
            with open(os.path.join(dir_copy, annotation_name), mode="a", encoding="UTF-16", newline='') as file:
                file_writer = csv.writer(file, delimiter="|")
                file_writer.writerow([f"{file_number[count]}.jpg", dataset_class])
            count += 1


def run3(dataset: str, annotation_name: str, dir_copy: str) -> None:
    create_randname_file(dataset, annotation_name, dir_copy)
