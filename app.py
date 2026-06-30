from scraper import scrape_website
from chunker import chunk_text
from vector_store import create_vector_store

url = input("Enter Website URL: ")

scrape_website(url)

chunk_text("website.txt")

create_vector_store()