import csv
import os


class Iterator1:
    def __init__(self, dataset: str, name: str, path: str):
        self.path = ""
        self.name = ""
        self.names = []
        self.limit = 0
        self.counter = 0
        self.dataset = ""
        self.init(dataset, name, path)

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        else:
            raise StopIteration

    def init(self, dataset: str, name: str, path: str):
        if not "dataset" in path:
            raise ("error")
        self.path = path
        self.name = name
        self.names = os.listdir(os.path.join(dataset, self.path, self.name))

        for i in self.names:
            if not ".jpg" in i:
                self.names.remove(i)
        self.limit = len(self.names)
        self.counter = 0

    def clear(self):
        self.counter = 0

    def setName(self, name: str):
        self.init(self.dataset, name, self.path)

    def getName(self):
       print(self.name)

    def setPath(self, path: str):
        self.init(self.dataset, self.name, path)