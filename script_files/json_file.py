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

    def increase_comment(self, username: str) -> bool:
        date_now_string = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
        date_now = datetime.datetime.strptime(date_now_string, '%d-%m-%Y %H:%M')
        aux = self.dict_of_username(username) # return the object {}
        try:
            index = self.data.index(aux) # get indice of object
        except:
            return False

        date_string = datetime.datetime.strptime(aux['date'], '%d-%m-%Y %H:%M')
        end_date = date_string
        if self.config['frequency'] == 'day':
            end_date = date_string + datetime.timedelta(hours=24)
        elif self.config['frequency'] == 'day':
            end_date = date_string + datetime.timedelta(hours=1)

        if self.data[index]['number'] == 0 or date_now > end_date:
            self.data[index]['date'] = date_now_string
            self.data[index]['number'] = 0

        if self.data[index]['number'] == self.config['quantity'] and date_now > end_date: #reach the limit and date is higher than the limit
            self.data[index]['number'] = 0
            self.data[index]['date'] = date_now_string

        if self.data[index]['number'] < int(self.config['quantity']):
            self.data[index]['number'] += 1
        else:
            return False
        print(self.data)
        self._save_json_file()
        return True

    def save_new_username(self, username: str):
        if len(self.dict_of_username(username)) == 0:
            self.data.append({'username': username, 'date': datetime.datetime.now().strftime('%d-%m-%Y %H:%M'), 'number': 0})
            self._save_json_file()