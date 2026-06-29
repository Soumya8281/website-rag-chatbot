from scraper import scrape_website
from chunker import chunk_text

url = input("Enter Website URL: ")

scrape_website(url)

chunk_text("website.txt")