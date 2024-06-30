import os
import requests
from dotenv import load_dotenv
from encoding import decode_string, encode_string, decode_integer, encode_integer

load_dotenv()

server_url = os.getenv("SERVER_URL")
api_key = os.getenv("API_KEY")

while True:
    query = input("Enter query: ")
    res = requests.post(server_url, data=encode_string(query), headers={
        "Authorization": f"Bearer {api_key}"
    })

    text = res.content.decode('utf8')
    print(decode_string(text))
