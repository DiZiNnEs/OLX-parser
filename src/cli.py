import json


class CLI:
    def __init__(self):
        pass

    def greeting(self):
        print('Приветсвую пользователь')
        print('Я беру результаты из сайта www.olx.kz и сохраняю их в файлах типа .json')

    def read(self):
        for json_files in ['result.json', 'result_2.json']:
            with open(json_files) as f:
                data = json.load(f)

            json_data = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False).strip('\n')

            print(json_data)
