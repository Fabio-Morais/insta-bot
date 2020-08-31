import json
import datetime
import configparser

class JsonFile:

    data = [] #{'username': 'fabiouds', 'date': '30-08-2020 21-42-16', 'number': 10}
    config = {'quantity': 60, 'frequency': 'day'}
    def __init__(self):
        self._load_json_file()
        self._import_configs()


    def _import_configs(self):
        config2 = configparser.ConfigParser()
        config2.sections()
        config2.read('example.ini')
        self.config['quantity'] = config2['DEFAULT']['quantity']
        self.config['frequency'] = config2['DEFAULT']['frequency']

    def _load_json_file(self):
        try:
            with open('script_files/_data.json', 'r') as outfile:
                self.data = json.load(outfile)
        except:
            pass

    def _save_json_file(self):
        with open('script_files/_data.json', 'w') as outfile:
            json.dump(self.data, outfile)

    def dict_of_username(self, username: str) -> dict:
        for i in self.data:
            if username == i['username']:
                return i

        return {}

    def increase_comment(self, username: str):
        date_now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
        date_1 = datetime.datetime.strptime(date_now, '%d-%m-%Y %H:%M')
        end_date = date_1
        if self.config['frequency'] == 'day':
            end_date = date_1 + datetime.timedelta(hours=24)
        elif self.config['frequency'] == 'day':
            end_date = date_1 + datetime.timedelta(hours=1)
        aux = self.dict_of_username(username)
        index = self.data.index(aux)

        if aux['number'] == 0:
            self.data[index]['date'] = date_now
            print(2)
        if aux['number'] == self.config['quantity'] and aux['date'] > end_date:
            self.data[index]['number'] = 0
            # date

        if aux['number'] < int(self.config['quantity']):
            self.data[index]['number'] += 1
        print(self.data)
        self._save_json_file()

    def save_new_username(self, username: str):
        if len(self.dict_of_username(username)) == 0:
            self.data.append({'username': username, 'date': datetime.now().strftime('%d-%m-%Y %H:%M'), 'number': 0})
            self._save_json_file()