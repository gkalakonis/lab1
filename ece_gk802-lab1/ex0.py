import requests  
from datetime import datetime



url = input("Enter url: ")
if not url.startswith("http://"):
    url="http://"+url

with requests.get(url) as response:  
    website_headers=response.headers
    print(f"Website: {url}\nHeaders{website_headers}")
    server_info=website_headers.get("Server")
    cookies_info=response.cookies
   
    if server_info:
        print(f"\nServer information{server_info}")
    else:
        print("\nNo server information found")

    if cookies_info:
        for cookie in cookies_info:
            print(f"Cookie {cookie.name}={cookie.value}")
            expires_date = datetime.utcfromtimestamp(round(cookie.expires)).strftime('%a, %d %b %Y %H:%M:%S GMT')#μετατροπή στην επιθυμητή μορφή
            print(f"expires: {expires_date}")
    else:
        print("No cookies found")
   
