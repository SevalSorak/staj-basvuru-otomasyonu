from urllib.parse import urlparse
import requests

# API anahtarı ve özel arama motoru ID'si (CX) tanımlanır
API_KEY = "**********"
CX = "**********"

with open("companies.txt", "r", encoding="utf-8") as file:
    company_names = [line.strip() for line in file.readlines()]

with open("company_websites.txt", "w", encoding="utf-8") as output_file:
    for company in company_names:
        query = f"{company} site:.com OR site:.net OR site:.org"
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}"
        response = requests.get(url)
        data = response.json()

        if "items" in data:
            first_result = data["items"][0]["link"]
            domain = urlparse(first_result).netloc 
            output_file.write(f"https://{domain}\n")  
        else:
            output_file.write(f"{company}: Sonuç bulunamadı.\n")