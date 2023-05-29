import numpy as np
import pandas as pd
from google.cloud import translate_v2 as translate
import requests
from bs4 import BeautifulSoup as bs

def df_multingue1(urls:list):
    """
    Función para hacer web scraping en eur-lex.

    Args:
        urls: lista de urls de las que se quiere obtener el texto

    Returns:
        pd.dataframe con el texto alineado en tres columnas por idioma.

    """
    entrega_dict = {"Idioma original(EN)": [],
                    "Traducción ES": [],
                    "Traducción RO": []}

    for url in urls:
        response = requests.get(url)
        html = response.content

        soup = bs(html, "html.parser")

        texts_en = soup.find_all("td", lang="EN")
        texts_es = soup.find_all("td", lang="ES")
        texts_ro = soup.find_all("td", lang="RO")

        entrega_dict["Idioma original(EN)"].extend([text.get_text() for text in texts_en if "EMPTY" not in text.get_text()])
        entrega_dict["Traducción ES"].extend([text.get_text() for text in texts_es if "EMPTY" not in text.get_text()])
        entrega_dict["Traducción RO"].extend([text.get_text() for text in texts_ro if "EMPTY" not in text.get_text()])

    return entrega_dict

def df_multingue2(urls):
    """
    Función para hacer web scraping en eur-lex.

    Args:
        urls: lista de urls de las que se quiere obtener el texto

    Returns:
        pd.dataframe con el texto alineado en tres columnas por idioma.

    """
    entrega_dict = {"Traducción FR": [],
                    "Traducción IT": [],
                    "Traducción DA": []}

    for url in urls:
        response = requests.get(url)
        html = response.content

        soup = bs(html, "html.parser")

        texts_fr = soup.find_all("td", lang="FR")
        texts_it = soup.find_all("td", lang="IT")
        texts_da = soup.find_all("td", lang="DA")

        for text in texts_fr:
            text = text.get_text().replace("&nbsp;", " ").strip()
            text2 = text.get_text().replace(u"\xa0", u" ").strip()
            if text and text2 and "EMPTY" not in text:
                entrega_dict["Traducción FR"].append(text)

        for text in texts_it:
            text = text.get_text().replace("&nbsp;", " ").strip()
            text2 = text.get_text().replace(u"\xa0", u" ").strip()
            if text and text2 and "EMPTY" not in text:
                entrega_dict["Traducción IT"].append(text)

        for text in texts_da:
            text = text.get_text().replace("&nbsp;", " ").strip()
            text2 = text.get_text().replace(u"\xa0", u" ").strip()
            if text and text2 and "EMPTY" not in text:
                entrega_dict["Traducción DA"].append(text)

    df = pd.DataFrame(entrega_dict)

    return df