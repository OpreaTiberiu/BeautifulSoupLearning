import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Write your code below this line 👇

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7"
}

resp = requests.get(URL, headers=headers)
resp.raise_for_status()
html_content = resp.text

soup = BeautifulSoup(html_content, "html.parser")

price_span = soup.find("span", {"class": "a-offscreen"})

print(price_span.getText())

