import requests
from bs4 import BeautifulSoup

def get_faq_data():
    url = "https://www.mosdac.gov.in/faqs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    faqs = []
    for block in soup.find_all("div", class_="panel-body"):
        text = block.get_text(strip=True)
        if text:
            faqs.append(text)
    return faqs

