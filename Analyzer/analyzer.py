import requests
import json
import os
from dotenv import load_dotenv
from time import sleep
from pprint import pprint


class Analyzer():
    def __init__(self):
        load_dotenv()
        self.api_url = "https://www.virustotal.com/api/v3" #/files"
        self.api_key = os.getenv("API_KEY")
        self.session = requests.session()
        self.analysis_status = "queued"

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
        return json.loads(r.text)
    
    def analysis_loop(self):
        analysis_status = None
        while analysis_status != "completed":
            analysis_data = self.get_analysis()
            analysis_status = analysis_data['data']['attributes']['status']
            print(analysis_status)
            if analysis_status == "queued":
                print("Analysis is processing... Please, wait a minute.")
                sleep(30)
            # pprint(analysis_data)
        return analysis_data


if __name__ == "__main__":
    analyzer = Analyzer()
    analyzer.upload_file("../Logger/logs.txt")
    analysis_result = analyzer.analysis_loop()['data']['attributes']['results']
    for vendor, attributes in analysis_result.items():
        print(vendor, '\t' + attributes['category'])
