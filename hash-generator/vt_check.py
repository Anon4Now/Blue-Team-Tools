import requests
import os
from requests.api import post
from requests.sessions import session
from dotenv import load_dotenv
load_dotenv()


API_ENDPOINT = os.getenv('API_ENDPOINT')
API_KEY = os.getenv('API_KEY')
API_KEY_VAL = os.getenv('API_KEY_VAL')

class vtChecking:

    def hashExists(hash):
        
        # See if file has already been uploaded - display content if yes, try upload if no
        url = f"{API_ENDPOINT}{hash}"

        headers = {
            "Accept": "application/json",
            API_KEY: API_KEY_VAL}
        response = requests.request("GET", url, headers=headers)
        return response.text



