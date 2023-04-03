import qrcode

file_path = r'qr코드모음.txt'

qr = qrcode.QRCode(
    version=5,  # 픽셀들 크기 설정 1~40 숫자가 작을수록 큼
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 수정
    box_size=3,  # 사진의 가로 세로 크기
    border=4,  # 밖의 흰색 여백 크기
)

with open(file_path,encoding='UTF8') as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

        qr.add_data(line)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(line + '.png')

