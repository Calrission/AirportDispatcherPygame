from Saves.Saver import Saver
import os
import pickle

class ScoreSaver(Saver):
    def __init__(self, path: str):
        super().__init__(path)

        self.data = {
            'Level-1': 0,
            'Level-2': 0,
            'Level-3': 0,
        }

        try:
            if not os.path.exists(self.path):
                with open(self.path, 'wb') as f:
                    pickle.dump(self.data, f)
            else:
                self.load()
        except Exception as ex:
            print('ScoreSaver:', ex)