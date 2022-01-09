import requests
import os
from requests.api import post
from requests.sessions import session
from dotenv import load_dotenv


class VTChecking:
    load_dotenv()

    def __init__(self):
        self.API_ENDPOINT = os.getenv('API_ENDPOINT')
        self.API_KEY = os.getenv('API_KEY')
        self.API_KEY_VAL = os.getenv('API_KEY_VAL')

    def hashExists(self, checkHash):
        # See if file has already been uploaded - display content if yes, try upload if no
        url = f"{self.API_ENDPOINT}{checkHash}"

        headers = {
            "Accept": "application/json",
            self.API_KEY: self.API_KEY_VAL}
        response = requests.request("GET", url, headers=headers)
        return response.text

    @staticmethod
    def parseJson(content):

        lastStatsDict = {}

        extractLastAnalysisDate = datetime.datetime.fromtimestamp(
            checkIDJson['data']['attributes']['last_analysis_date'])
        extractLastAnalysisStats = checkIDJson['data']['attributes']['last_analysis_stats']

        print(f'Last Analysis Date : {extractLastAnalysisDate}')

        print(f'Last Analysis Stats:')
        for key in extractLastAnalysisStats:
            lastStatsDict[key] = extractLastAnalysisStats[key]
            print(F'   {key}: {extractLastAnalysisStats[key]}')

        for key in lastStatsDict:
            if key == 'malicious':
                if lastStatsDict[key] == 0:
                    print(f'\nBased on results, the file appears safe')
                elif lastStatsDict[key] > 0 and lastStatsDict[key] < 2:
                    print(f'\nSome vendors flagged this file, consider additional research')
                elif lastStatsDict[key] > 2:
                    print(f'\nThis file may be malicious, consider not downloading')

    @staticmethod
    def checkError(content):

        extractErrorCode = checkIDJson['error']['code']
        if extractErrorCode == 'NotFoundError':
            print(
                f'This file has not been uploaded to Virus Total before -- consider uploading the file for scanning at \n"https://www.virustotal.com/gui/home/upload"')

        elif extractErrorCode != 'NotFoundError':
            print(f'Error returned from VT is {extractErrorCode}')

        else:
            pass
