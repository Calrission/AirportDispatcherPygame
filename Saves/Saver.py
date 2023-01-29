import pickle
import os


class Saver:
    def __init__(self, path: str):
        self.path = path
        self.data = {}


    def load(self):
        try:
            with open(self.path, 'rb') as f:
                data = pickle.load(f)
        except Exception as ex:
            print('Saver-load:', ex)

    def save(self, key: str, item: str):
        try:
            self.data[key] = item
            with open(self.path, 'wb') as f:
                pickle.dump(self.data, f)
        except Exception as ex:
            print('Saver-save:', ex)