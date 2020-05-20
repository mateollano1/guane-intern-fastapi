import requests

URL = "https://dog.ceo/api/breeds/image/random"

def get_picture_url(): 
    picture_url = requests.get(url = URL)
    code_result = picture_url.status_code
    if code_result == 200:
        return picture_url['message']
    return ""

