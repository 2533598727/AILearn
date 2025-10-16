import requests
from urllib3 import response

API_URL = "https://api-inference.huggingface.co/models/uer/gpt2-chinese-cluecorpussmall"
API_TOKEN = "hf_XXXXX"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

response =  requests.post(API_URL,headers=headers,json={"inputs":"你好，Huggingface"})
print(response.json())
