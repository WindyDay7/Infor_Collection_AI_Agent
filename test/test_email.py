import yagmail
from config import settings
from core.logger import logger

def send_email_with_file(subject: str, body: str, to: str, filepath: str):
    yag = yagmail.SMTP(
        user=settings.EMAIL_USER,
        password=settings.EMAIL_PASSWORD,
        host='smtp.qq.com',
        port=465,
        smtp_ssl=True  # <<<<< 关键
    )
    yag.send(
        to=to,
        subject=subject,
        contents=[body, filepath],
    )
    print("✅ Email sent successfully.")


out_path = "/home/windyday/study/study_llm/Infor_Collection_AI_Agent/output/news_digest_20250608.md"

# 只发送最后生成的 markdown 文件
send_email_with_file(
    subject=f"📰 Weekly News Digest",
    body="Please find the weekly news summary attached.",
    to=settings.EMAIL_RECEIVER,
    filepath=out_path
)
