from celery import shared_task
from bs4 import BeautifulSoup
import requests

@shared_task
def get_app_details(optional_param):
    URL = "https://play.google.com/store/apps"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    titles = [i.text for i in soup.select("div.ULeU3b.neq64b a div.Epkrse")]
    icons = [i['src'] for i in soup.select('div.TjRVLb img')]

    return titles, icons
