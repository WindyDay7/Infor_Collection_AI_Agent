import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "te279408285@foxmail.com"
receiver_email = "279408285wf@gmail.com"
password = "svclqwllsjscbjed"  # QQ邮箱中生成的授权码

message = MIMEMultipart("alternative")
message["Subject"] = "测试邮件 - SMTP from Python"
message["From"] = sender_email
message["To"] = receiver_email

text = "这是一个 SMTP 测试邮件"
part = MIMEText(text, "plain")
message.attach(part)

# 使用SSL连接QQ邮箱SMTP服务器
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("✅ 邮件发送成功")
