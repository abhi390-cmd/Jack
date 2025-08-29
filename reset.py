import requests
import webbrowser
webbrowser.open("t.me/eizonpython")
def send_reset_request(username_or_email):
    url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"

    headers = {
        "authority": "www.instagram.com",
        "method": "POST",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.7",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/accounts/password/reset/?source=fxcal",
        "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; M2101K786) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "x-asbd-id": "129477",
        "x-csrftoken": "missing",  
        "x-ig-app-id": "1217981644879628",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "1015181662",
        "x-requested-with": "XMLHttpRequest"
    }

    session = requests.Session()
    session.get("https://www.instagram.com/accounts/password/reset/")
    csrf_token = session.cookies.get_dict().get("csrftoken", "missing")
    headers["x-csrftoken"] = csrf_token

    data = {
        "email_or_username": username_or_email,
        "flow": "fxcal"
    }

    response = session.post(url, headers=headers, data=data)

    if response.status_code == 200:
        print(f"\033[1;32m Ret başarıyla gönderildi : {username_or_email}\033[0m")
        print(response.json())
    else:
        print(f"\033[1;31m[-] Hata oluştu: {response.status_code}\033[0m")
        try:
            print(response.json())
        except:
            print("[-] Beklenmeyen yanıt alındı!")

if __name__ == "__main__":
    email_or_username = input("\033[1;32mENTER EMAIL OR USERNAME: \033[0m")
    print("\033[1;39m—" * 60)
    send_reset_request(email_or_username)
    
    
    # @Eiz0n