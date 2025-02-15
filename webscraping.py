# -*- coding: utf-8 -*-
"""WebScraping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Oh-Oj1OqFDQUyyUSo4NWziJupiT1C1cK
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.mercadolibre.com.co/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    h1_count = len(soup.find_all("h1"))
    h2_count = len(soup.find_all("h2"))
    h3_count = len(soup.find_all("h3"))

    print(f"Cantidad de <h1>: {h1_count}")
    print(f"Cantidad de <h2>: {h2_count}")
    print(f"Cantidad de <h3>: {h3_count}")
else:
    print(f"Error al acceder a la página: {response.status_code}")