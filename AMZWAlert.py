import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
url = 'https://hvr-amazon.my.site.com/BBIndex?refURL=https%3A%2F%2Fhvr-amazon.my.site.com%2F'
province=[
    "BC Canada", "ON Canada"
    ]
while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.text
            location1 = soup.find("h6")
            for i in soup.find_all("h6"):
                if "ON Canada" in i.text:
                    print(i.text,"Time: ", datetime.now())
            print("\n")

        else:
            print(f"Failed to fetch web page. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    time.sleep(2)
