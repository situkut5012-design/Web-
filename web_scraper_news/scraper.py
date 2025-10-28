import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import json

# 設定読み込み
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# Webスクレイピング
response = requests.get(config["target_url"])
soup = BeautifulSoup(response.text, "html.parser")

# Yahooニューストップの見出しを抽出（例）
headlines = [h3.text.strip() for h3 in soup.find_all("h3")][:5]

# メール本文作成
body = "今日のニューストップ5:\n" + "\n".join([f"- {title}" for title in headlines])
msg = MIMEText(body)
msg["Subject"] = "ニュース自動通知"
msg["From"] = config["sender_email"]
msg["To"] = config["receiver_email"]

# メール送信
try:
    server = smtplib.SMTP(config["smtp_server"], config["smtp_port"])
    server.starttls()
    server.login(config["sender_email"], config["sender_password"])
    server.send_message(msg)
    server.quit()
    print("✅ メール送信完了！")
except Exception as e:
    print("❌ メール送信に失敗しました:", e)
