import requests
import re
req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',req.text)

print(out_addr)
print(out_addr[0])
print(out_addr[1])