import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendMail:
    def __init__(self):
        self.sender_email = "sendermail@gmail.com"
        self.receiver_email = "receivermail@hotmail.com"
        self.password = "your password."
        self.subject = "Feedback from user"
        self.body = ""


    def send_mail(self,phone,name,mail,message):
        try:
          with smtplib.SMTP("smtp.gmail.com", 587) as server:
             server.starttls()  # Güvenli bağlantı başlat
             server.login(self.sender_email, self.password)
             server.sendmail(self.sender_email, self.receiver_email, message.as_string())
             print("Success")

        except Exception as e:
             print(f"E-posta gönderimi sırasında hata oluştu: {e}")
