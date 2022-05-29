import json

class DataCapsule:
    def __init__(self, document=None):
        self.document = document

    def beautiful_print(self):
        print(json.dumps(self.document, indent=4))
