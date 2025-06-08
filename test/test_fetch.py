# test_fetch.py
from core.fetch import fetch_url

url = "https://razorpay.com/blog/ai-in-payments/"
html = fetch_url(url)

if html:
    print("✅ HTML fetched successfully.")
    print(html[:500])  # Show preview
else:
    print("❌ Failed to fetch article.")
