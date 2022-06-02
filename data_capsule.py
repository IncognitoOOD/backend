import json


class DataCapsule:
    def __init__(self, document=None, fields=None):
        if fields is None:
            fields = []
        if document is None:
            document = {}
        self.document = document
        self.fields = fields

    def beautiful_print(self):
        print("fields:", self.fields)
        print(json.dumps(self.document, indent=4))
