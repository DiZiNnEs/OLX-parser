import json
from .browser import Browser


class Json:
    def __init__(self, browser: Browser):
        self.browser = browser

    def add(self, results) -> None:
        dates_to_json = json.dumps(results, indent=4, ensure_ascii=False)

        with open('result.json', 'w', encoding='utf8') as file:
            file.write(dates_to_json)
