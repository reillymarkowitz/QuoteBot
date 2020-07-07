from scraper import Scraper

def handler(event, context):
    scraper = Scraper()
    scraper.scrape()
