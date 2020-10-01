import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
# from email.message import Message
# from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.header import Header
import os
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT=465
SMTP_USER = 'kusung25@gmail.com'
# 실제 비밀번호를 입력해야 합니다.
SMTP_PASSWORD = 'uyxhytdovynrzwcy'
class MailManager:
    '''
    This class is used to send mail
    '''
    def __init__(self, emailfrom, emailto, subject, email_contents_path): #, logger=None        
        msg = MIMEMultipart()
        msg["From"]    = emailfrom
        msg['To']      = emailto
        msg['Subject'] = Header(subject,'utf-8') # 제목 인코딩
        msg.preamble   = "" #preamble #값을 넣지 말고 빈스트링으로 넘겨야 에러 안남
        
        #메일 본문 처리
        with open(email_contents_path, encoding="utf-8") as fp:
            # Create a text/html message
            content = MIMEText(fp.read(), 'html')
            msg.attach(content)          
        self.msg = msg
    
    def attach_file(self, fileToSend):
        ctype, encoding = mimetypes.guess_type(fileToSend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)

        if maintype == "text":
            fp = open(fileToSend)
            # Note: we should handle calculating the charset
            attachment = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "image":
            fp = open(fileToSend, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(fileToSend, "rb")
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachment)
        
        basename = os.path.basename(fileToSend)
        attachment.add_header("Content-Disposition", "attachment", filename=basename)
        self.msg.attach(attachment)
        return 'ok'
    def send_mail(self, attachment_path):
        self.attach_file(attachment_path)
        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        smtp.send_message(self.msg)
        smtp.quit()
        return 'ok'
        
        
emailfrom = "kusung25@gmail.com"
emailto   = "kusung25@naver.com" 
subject = "결과 송신 건"
email_contents_path = 'email_content.txt'
mm = MailManager(emailfrom, emailto, subject, email_contents_path)
ROOT_DIR= 'C:\\mylab\\book\\automate_basic' 
attachment_path = ROOT_DIR+'\\send.zip' #"send.zip"
mm.send_mail(attachment_path)

        