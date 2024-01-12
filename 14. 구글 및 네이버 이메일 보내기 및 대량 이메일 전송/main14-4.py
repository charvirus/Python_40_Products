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

html_body = """
	<section>
		<h1> 제목1 </h1>
		<p>첫 번째 내용입니다.</p>
	</section>
	<section>
		<h1> 제목2 </h1>
		<p>두 번째 내용입니다.</p>
	</section>
"""

msg.attach(MIMEText(html_body, 'html'))

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()
