import requests


def get_picture_url(): 
    URL = "https://dog.ceo/api/breeds/image/random"
    requestGet = requests.get(url = URL)
    picture_url = requestGet.json()
    code_result = requestGet.status_code
    if code_result == 200:
        return picture_url['message']
    return ""

