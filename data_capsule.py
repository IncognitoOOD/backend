import json


class DataCapsule:
    def __init__(self, document=None, fields=None):
        if fields is None:
            fields = []
        if document is None:
            document = {}
        self.document = document
        self.fields = fields

    def create_from_json(self, j):
        self.document = j['document']
        self.fields = j['fields']

    def get_json(self):
        d = {
            "fields": self.fields,
            "document": self.document
        }
        return d
    def beautiful_print(self):
        print("fields:", self.fields)
        print(json.dumps(self.document, indent=4))
