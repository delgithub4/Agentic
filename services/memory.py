import json


class Memory:

    FILE = "data/memory.json"

    def save(self, task):

        try:

            with open(self.FILE, "r") as file:
                history = json.load(file)

        except:

            history = []

        history.append(task)

        with open(self.FILE, "w") as file:
            json.dump(history, file, indent=4)

