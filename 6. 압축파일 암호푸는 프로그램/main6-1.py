import itertools

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range(1, 4):
    to_attempt = itertools.product(passwd_string, repeat=len) # 데카르트 곱
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
