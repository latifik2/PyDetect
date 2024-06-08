import requests
import json
from pprint import pprint


class Analyzer():
    def __init__(self):
        self.api_url = "https://www.virustotal.com/api/v3" #/files"
        self.api_key = "dd19cca619f4b4c5ade651d73d3a3987224f2e6b5db44c2852af397e1b9bdef9"
        self.session = requests.session()

    def upload_file(self, file_path: str):
        files = {
            'file': ("logs.txt", open(file_path, "rb"), "text/x-python")
        }
        headers = {
            "accept": "application/json",
            "x-apikey": self.api_key
        }
        
        response_text = self.session.post(self.api_url + "/files", files=files, headers=headers).text
        self.analysis_link = json.loads(response_text)['data']['links']['self']

    def get_analysis(self):
        headers = {
            "x-apikey": self.api_key
        }
        r = self.session.get(self.analysis_link, headers=headers)
        print(r.text)


if __name__ == "__main__":
    analyzer = Analyzer()
    analyzer.upload_file("../Logger/logs.txt")
    analyzer.get_analysis()