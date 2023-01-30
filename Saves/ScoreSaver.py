from Saves.Saver import Saver
import os
import pickle


class ScoreSaver(Saver):
    def __init__(self, path: str):
        super().__init__(path)

        self.data = {
            'Scenario/Level-1.scen': 0,
            'Scenario/Level-2.scen': 0,
            'Scenario/Level-3.scen': 0,
        }

        try:
            if not os.path.exists(self.path):
                with open(self.path, 'wb') as f:
                    pickle.dump(self.data, f)
            else:
                self.load()
        except Exception as ex:
            print('ScoreSaver:', ex)
