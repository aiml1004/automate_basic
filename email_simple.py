from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT=465
SMTP_USER = 'kusung25@gmail.com'
# 실제 비밀번호를 입력해야 합니다.
SMTP_PASSWORD = 'uyxhytdovynrzwcy'

def send_mail(emailto, subject, email_contents_path, attachment=False): #name, 
    msg = MIMEMultipart('alternative')

    if attachment:
        msg = MIMEMultipart('mixed')
    msg['From'] = SMTP_USER
    msg['To'] = emailto
    #msg['CC'] = cc
    msg['Subject'] = subject

    #메일 본문 처리
    with open(email_contents_path, encoding="utf-8") as fp:
        # Create a text/html message
        content = MIMEText(fp.read(), 'html')
        msg.attach(content)     

    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders

        file_data = MIMEBase('application', 'octet-stream')
        f = open(attachment,'rb')
        file_contents = f.read()
        file_data.set_payload(file_contents)
        encoders.encode_base64(file_data)

        from os.path import basename
        filename = basename(attachment)
        file_data.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(file_data)
        
    smtp = SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.send_message(msg)
    smtp.close()
    return 'ok'

"""    
emailfrom = "kusung25@gmail.com"
emailto   = "kusung25@naver.com" 
subject = "정통부 사업공모 게시판 신규게시물 송신 건"
email_contents_path = 'email_content.txt'
ROOT_DIR= 'C:\\mylab\\book\\automate_basic' 
attachment = ROOT_DIR+'\\send.zip' #"send.zip"
send_mail(emailto, subject, email_contents_path, attachment)
"""
