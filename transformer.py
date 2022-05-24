from data_capsule import DataCapsule
import requests


class Transformer:
    config: dict

    def __init__(self, config: dict):
        self.config = config

    def __rename(self, dc: DataCapsule):
        rename = self.config['rename']
        if rename:
            for r in rename:
                old_name = list(r.keys())[0]
                new_name = list(r.values())[0]
                dc.document[new_name] = dc.document[old_name]
                del dc.document[old_name]

        return dc

    def __concat(self, dc: DataCapsule):
        concat = self.config['concat']
        if concat:
            for c in concat:
                dest_field = list(c.keys())[0]
                src_field_1 = c['dest_field'][0]
                src_field_2 = c['dest_field'][1]
                sep = c['sep']
                dc.document[dest_field] = str(c[src_field_1]) + sep + str(c[src_field_2])

        return dc

    def __api_call(self, dc: DataCapsule):
        api_call = self.config['api_call']
        if api_call:
            for a in api_call:
                dest_field = a['dest_field']
                api_address = a['api_address']
                method = a['method']

                args = a['args']
                params = dict()
                if args:
                    for arg in args:
                        arg_name = arg['arg_name']
                        if arg['data']['type'] == 'FROM_DATA_CAPSULE':
                            data = dc.document[arg['data']['src_field']]
                        else:
                            data = arg['data']['value']
                        params[arg_name] = data

                if method == 'GET':
                    try:
                        response = requests.get(url=api_address, params=params)
                    except Exception:
                        raise Exception('API returned no response')
                else:
                    try:
                        response = requests.post(url=api_address, params=params)
                    except Exception:
                        raise Exception('API returned to response')

                dc.document[dest_field] = response.text

        return dc

    def run(self, dc_list: list):
        ret_list = list()
        for dc in dc_list:
            renamed = self.__rename(dc)
            concatenated = self.__concat(renamed)
            api_called = self.__api_call(concatenated)
            ret_list.append(api_called)

        return dc_list
