import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted tags
        for tag in soup(["script", "style"]):
            tag.decompose()

        text = soup.get_text(separator="\n", strip=True)

        with open("website.txt", "w", encoding="utf-8") as file:
            file.write(text)

        print("✅ Website text saved to website.txt")

    except Exception as e:
        print("❌ Error:", e)