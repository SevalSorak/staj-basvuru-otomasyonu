# E-posta Toplama ve Gönderme Otomasyonu

Bu proje, belirli web sitelerinden e-posta adreslerini toplamak ve daha sonra bu e-posta adreslerine otomatik olarak mesaj göndermek amacıyla yazılmıştır. Selenium ve BeautifulSoup kullanılarak, web sayfalarındaki e-posta adresleri tespit edilir ve belirli iletişim sayfalarına yönlendirilerek bu e-postalar toplanır. E-posta adresleri daha sonra otomatik olarak belirtilen alıcılara gönderilebilir.

## Proje Özeti

Bu proje, aşağıdaki adımları otomatikleştirir:

*   Belirtilen web sitelerinden e-posta adreslerini toplama.
*   E-posta adreslerini `emails.txt` dosyasına kaydetme.
*   İhtiyaç duyulduğunda, bu adreslere otomatik e-posta gönderme.

## Özellikler:

*   Web sayfalarındaki e-posta adreslerini dinamik olarak toplama (Selenium ile JavaScript ile yüklenen sayfalarda da çalışır).
*   E-posta adreslerini düzenli olarak bir dosyaya kaydetme.
*   Farklı sayfalarda e-posta araması yapabilme (Ana sayfa, iletişim sayfası, hakkımızda sayfası vb.).
*   E-posta göndermeyi otomatikleştirebilme (ayrıca bir SMTP sunucusu veya ilgili API ile entegre edilebilir).

## Başlangıç Rehberi

Aşağıdaki adımları takip ederek projeyi bilgisayarınızda çalıştırabilirsiniz.

### Ön Koşullar

Bu projeyi kullanabilmek için bilgisayarınızda aşağıdaki araçların kurulu olması gerekir:

*   Python 3.6 veya daha yeni bir sürümü
*   `requests`, `BeautifulSoup`, `selenium` gibi Python kütüphaneleri
*   Google Chrome (veya başka bir tarayıcı için uygun driver)

### Kurulum

1.  Python 3 ve pip'i yüklediğinizden emin olun.

2.  Gerekli Python kütüphanelerini yüklemek için şu komutları çalıştırın:

    ```bash
    pip install requests beautifulsoup4 selenium webdriver-manager
    ```

3.  Projeyi indirin veya klonlayın:

    ```bash
    git clone <repo-url>
    ```

### Kullanım

1.  **Web Siteleri Listesini Hazırlama:**

    E-posta aramak istediğiniz web sitelerinin listesini `company_websites.txt` dosyasına yazın. Her bir web sitesini yeni bir satıra ekleyin.

2.  **E-posta Adreslerini Toplama:**

    Projeyi çalıştırarak belirtilen web sitelerinden e-posta adreslerini toplayabilirsiniz:

    ```bash
    python email_scraper.py
    ```

3.  **Sonuçları Görüntüleme:**

    E-posta adresleri toplandıktan sonra, sonuçlar `emails.txt` dosyasına kaydedilecektir. Bu dosyayı açarak tüm topladığınız e-posta adreslerini görebilirsiniz.

4.  **E-posta Gönderme:**

    Toplanan e-posta adreslerine otomatik olarak e-posta gönderebilmek için, SMTP ayarlarınızı yapmanız gerekir. Bu adım opsiyoneldir, ancak işlevsellik için gereklidir.

    #### E-posta Gönderme İçin Ayar Yapma

    E-posta gönderme işlevini kullanabilmek için, SMTP sunucusu (Gmail veya benzeri) ve kimlik doğrulama bilgilerinizi sağlamanız gerekir. Bu ayarlar, kodda belirtilen yere eklenmelidir.