import qrcode

# QR 설정
qr = qrcode.QRCode(
    version=5,  # 픽셀들 크기 설정 1~40 숫자가 작을수록 큼
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 수정
    box_size=3,  # 사진의 가로 세로 크기
    border=4,  # 밖의 흰색 여백 크기
)

qr_data = 'www.naver.com'
qr.add_data(qr_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(qr_data+'.png')