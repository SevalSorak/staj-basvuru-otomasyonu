import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time
from urllib.parse import urljoin

# Selenium ayarları 
options = webdriver.ChromeOptions()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

def get_emails_from_text(text):
    """Metin içindeki e-posta adreslerini çeker"""
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, text) 
    return list(set(emails)) if emails else []  


def get_contact_email(url):
    """Statik sayfalarda e-posta adresi bulma"""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}  
        response = requests.get(url, headers=headers, timeout=10) 
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, "html.parser") 
        emails = get_emails_from_text(soup.text)  

        return emails if emails else None  
    except requests.exceptions.RequestException:
        return None  


def get_contact_email_selenium(url):
    """JavaScript ile yüklenen sayfalarda e-posta adresi bulma"""
    try:
        driver.get(url) 
        time.sleep(3)  
        page_text = driver.page_source  
        emails = get_emails_from_text(page_text)  

        return emails if emails else None
    except Exception:
        return None 


def find_email(website_url):
    """Ana sayfa ve iletişim sayfasında e-posta arar"""
    print(f"📌 {website_url} adresinde e-posta aranıyor...")

    # 1️⃣ Ana Sayfada E-posta Adresi Ara
    emails = get_contact_email(website_url)
    if emails:
        print(f"✅ Ana sayfada bulundu: {emails}")
        return emails  

    # 2️⃣ Ana sayfada bulunamadıysa Selenium ile kontrol et
    emails = get_contact_email_selenium(website_url)
    if emails:
        print(f"✅ Ana sayfada (Selenium) bulundu: {emails}")
        return emails  

    # 3️⃣ İletişim Sayfalarını Tahmin Et ve E-posta Adresi Ara
    possible_pages = [
        urljoin(website_url, "contact"),  
        urljoin(website_url, "iletisim"),  
        urljoin(website_url, "about"),  
        urljoin(website_url, "hakkimizda"),  
        urljoin(website_url, "bize-ulasin"),  
    ]

    for page in possible_pages:
        emails = get_contact_email(page)  #
        if emails:
            print(f"✅ {page} sayfasında bulundu: {emails}")
            return emails  

        emails = get_contact_email_selenium(page) 
        if emails:
            print(f"✅ {page} sayfasında (Selenium) bulundu: {emails}")
            return emails 

    print(f"❌ {website_url} adresinde e-posta bulunamadı.")
    return None 


with open("company_websites.txt", "r", encoding="utf-8") as file:
    websites = [line.strip() for line in file.readlines()] 

all_emails = []

for site in websites:
    emails = find_email(site)  
    if emails:
        all_emails.extend(emails)  

with open("emails.txt", "w", encoding="utf-8") as email_file:
    for email in all_emails:
        email_file.write(email + "\n")  

driver.quit() 
