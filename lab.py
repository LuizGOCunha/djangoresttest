import requests
import uuid
from pprint import pprint

post_data = {
    "id": uuid.uuid4(),
    "number": 6666
}

r = requests.post('http://127.0.0.1:8000/add/', data=post_data)
