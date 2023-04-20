import itertools
import zipfile

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zfile = zipfile.ZipFile(r'암호.zip') # 압축 파일을 불러옴

for len in range(1, 6):
    to_attempt = itertools.product(passwd_string, repeat=len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            zfile.extractall(pwd=passwd.encode())
            print(f"비밀번호는 {passwd} 입니다.")
            break
        except:
            pass
