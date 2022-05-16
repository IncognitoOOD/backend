class DataCapsule:
    fields = set()

    def __init__(self, doc_id, version=1, document=None, process_data=None, metadata=None, logs=None,
                 id_field_name=None,
                 fields_update=None):
        if metadata is None:
            metadata = {}
        if process_data is None:
            process_data = {}
        self.version = version
        self.document = document
        [self.fields.add(x) for x in self.document.keys()]
        self.process_data = process_data
        self.metadata = metadata
        self.logs = logs
        self.transform_meta = dict()
        self.doc_id = doc_id
        self.id_field_name = id_field_name
        self.fields_update = fields_update

    def add_process_data(self, process_data):
        self.process_data.update(process_data)

    def update_fields(self):
        self.fields = set()
        [self.fields.add(x) for x in self.document.keys()]
        [self.fields.add(x) for x in self.process_data.keys()]
