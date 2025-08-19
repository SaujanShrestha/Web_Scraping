import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import os

def fetch_latest_headline():
    url = "https://english.onlinekhabar.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    article = soup.find("div", class_="ok-post-contents")
    if article:
        headline_tag = article.find("h2").find("a")
        author_tag = article.find("span", class_="ok-post-hours")

        headline = headline_tag.text.strip()
        link = headline_tag["href"]
        author = author_tag.text.strip() if author_tag else "Unknown"

        file_exists = os.path.isfile("headlines.csv")
        with open("headlines.csv", "a", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Fetched At", "Headline", "Author", "Link"])
            writer.writerow([datetime.now(), headline, author, link])

        print("Saved:", headline)
    else:
        print("No headline found.")
        
fetch_latest_headline()
