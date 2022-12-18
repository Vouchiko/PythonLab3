import os
import csv


def create_csv_annotation(dataset: str, class_name: str, annotation_name: str) -> None:
    path_to_class = os.path.join(dataset, "dataset", class_name)
    class_names = os.listdir(path_to_class)
    with open(annotation_name, mode="w", newline='') as file:
        file_writer = csv.writer(file, delimiter=",")
        for name in class_names:
            file_writer.writerow(
                [os.path.abspath(name), os.path.join('dataset', class_name, name), class_name])


def run1(dataset: str, class_name: str, annotation_name: str) -> None:
    create_csv_annotation(dataset, class_name, annotation_name)