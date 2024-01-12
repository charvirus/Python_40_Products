import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

send_email = "haeun41311@gmail.com"
send_pwd = "udeotdnymnlqqpva"

recv_email = "jbrandon413@naver.com"

smtp_name = "smtp.gmail.com"
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = "메일제목은 여기에 넣습니다"
msg['From'] = send_email
msg['To'] = recv_email

text = """
메일 내용을 여기에 적습니다.
여러줄을 입력하여도 됩니다.
"""

contentPart = MIMEText(text)
msg.attach(contentPart)

etc_file_path = r'첨부파일.txt'
with open(etc_file_path,'rb') as f:
    etc_part = MIMEApplication(f.read())
    etc_part.add_header('Content-Disposition','attachment',filename="첨부파일.txt")
    msg.attach(etc_part)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()
