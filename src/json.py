import json
from typing import (
    List,
    Dict,
    Union,
    Any
)

from .browser import Browser


class Json:
    def __init__(self, browser: Browser) -> None:

        self.browser = browser

    def add(self, results: List[Dict[str, Union[int, Any]]]) -> None:
        dates_to_json = json.dumps(results, indent=4, ensure_ascii=False)

        with open('result.json', 'w', encoding='utf8') as file:
            file.write(dates_to_json)

    def read(self) -> None:
        with open('result.json') as file:
            data = json.load(file)

        json_data = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False).strip('\n')

        print(json_data)
