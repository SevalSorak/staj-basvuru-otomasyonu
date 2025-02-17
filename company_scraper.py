import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://bilisimvadisi.com.tr/hakkimizda/firmalar/" # Örnek URL

def get_all_firms():
    """Tüm firmaları çeker, gerekirse 'Daha Fazlasını Yükle' butonuna basar."""
    options = Options()
    options.add_argument("--headless")  # Tarayıcıyı arka planda çalıştır
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # ChromeDriver'ı otomatik olarak yükler ve başlatır
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(URL)
    time.sleep(3)  

    while True:
        try:
            load_more_button = driver.find_element(By.CLASS_NAME, "loadmore-exbt")
            driver.execute_script("arguments[0].click();", load_more_button)  
            time.sleep(2)  
        except:
            print("✅ Tüm firmalar yüklendi veya buton bulunamadı.")  
            break  

    # Firma isimlerini <h3> etiketleri içerisinden çek
    firm_elements = driver.find_elements(By.TAG_NAME, "h3")  
    firm_names = [firm.text.strip() for firm in firm_elements]  

    driver.quit()  
    return firm_names  

firms = get_all_firms()

with open("companies.txt", "w", encoding="utf-8") as f:
    for firm in firms:
        f.write(firm + "\n")

print("✅ Firmalar 'companies.txt' dosyasına kaydedildi!")
