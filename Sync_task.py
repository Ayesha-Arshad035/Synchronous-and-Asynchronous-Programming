import requests
import time

urls = [
     "https://www.daraz.pk",
    "https://www.alibaba.com",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://colab.google/"
]

def fetch_sync(url):
    response = requests.get(url)
    print(response.text) 
    print(f"{url}")
for url in urls:
    fetch_sync(url)

"""
import requests
urls = [
    "https://www.daraz.pk",
    "https://www.alibaba.com",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://colab.google/"
]
def fetch_sync_with_session(urls):
    with requests.Session() as session:
        for url in urls:
            response = session.get(url)
            print(response.text) 
            print(f"{url}")
fetch_sync_with_session(urls)
"""