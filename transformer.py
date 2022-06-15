from data_capsule import DataCapsule
import requests


class Transformer:
    config: dict

    def __init__(self, config: dict):
        self.config = config

    def __rename(self, dc: DataCapsule):
        new_dc = DataCapsule()
        rename = self.config.get('rename')
        mp = {}
        for item in rename:
            mp = {**mp, **item}

        if rename:
            if dc.fields:
                for field in dc.fields:
                    the_name = mp[field] if field in mp else field
                    new_dc.fields.append(the_name)
                    new_dc.document[the_name] = dc.document[field]
            else:
                for item in dc.document.items():
                    field = item[0]
                    value = item[1]
                    the_name = mp[field] if field in mp else field
                    new_dc.document[the_name] = value

        return new_dc

    def __concat(self, dc: DataCapsule):
        concat = self.config.get('concat')
        if concat:
            print("concat", concat)
            for item in concat:
                print("item", item)
                c = item.copy()
                sep = c['sep']
                c.pop("sep")
                for k, v in c:
                    dest_field = k
                    src_fields = [i for i in v]
                    dc.document[dest_field] = str(sep).join([dc.document[i] for i in src_fields])
                    if dest_field not in dc.fields:
                        dc.fields.append(dest_field)
        return dc

    def __api_call(self, dc: DataCapsule):
        api_call = self.config.get('api_call')
        if api_call:
            for a in api_call:
                dest_field = a['dest_field']
                api_address = a['api_address']
                method = a['method']
                response_field = a['response_field']

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
                        raise Exception('API returned no response')

                dc.document[dest_field] = response.json()[response_field]

        return dc

    def run(self, dc_list: list):
        ret_list = list()
        for dc in dc_list:
            renamed = self.__rename(dc)
            concatenated = self.__concat(renamed)
            api_called = self.__api_call(concatenated)
            ret_list.append(api_called)

        return ret_list
