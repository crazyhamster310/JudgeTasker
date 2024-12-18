# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from weasyprint import HTML, CSS

SITE_URL = "https://acm.timus.ru/"
ARCHIVE_URL = "https://acm.timus.ru/problemset.aspx?space=1&page=all&locale=ru"


def get_links_by_source(source: str):
    request = requests.get(ARCHIVE_URL)
    if request.status_code != 200:
        return None
    soup = BeautifulSoup(request.text, "html.parser")
    links = []
    for row in soup.find_all(class_="source", string=source):
        links.append(
            SITE_URL
            + row.parent.find(class_="name").find("a").get("href")
            + "&locale=ru"
        )
        links[-1] = links[-1].replace("problem", "print")
    return links


def make_pdf(source: str) -> bytes:
    links = get_links_by_source(source)
    if len(links) == 0:
        return None
    css = CSS(string="body {font-size: 10pt;}")
    documents = [HTML(link).render(stylesheets=[css]) for link in links]
    all_pages = [p for doc in documents for p in doc.pages]
    return documents[0].copy(all_pages).write_pdf()
