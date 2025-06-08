import undetected_chromedriver as uc
from core import extract

def fetch_page_uc(url):
    options = uc.ChromeOptions()
    options.headless = True  # 设置为 False 可在调试时看到浏览器
    driver = uc.Chrome(options=options)
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html

# 抓取页面
url = "https://hackernoon.com/from-one-off-transactions-to-intelligent-payments-the-evolution-of-open-banking-with-vrp"
html = fetch_page_uc(url)

# 写入文件
with open("businesswire_page.html", "w", encoding="utf-8") as f:
    f.write(html)


content = extract.extract_main_text(html)
if not content:  # 成功提取，直接返回
    # 尝试备选提取器
    content = extract.extract_main_text_with_newspaper(html)


    
with open("businesswire_page.txt", "w", encoding="utf-8") as f:
    f.write(content if content else "未能提取到内容")

print("已保存 HTML 到 businesswire_page.html")
# print("提取的主要内容：", content)