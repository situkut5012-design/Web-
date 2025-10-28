# Webスクレイピング＋Slack通知ボット

## プロジェクト概要
このPythonツールは、指定したニュースサイトから最新記事のタイトルを自動で取得し、  
Slackに通知するボットです。  

---

## 使用技術
- Python 3.x
- requests（Webページ取得）
- BeautifulSoup4（HTML解析）
- slack_sdk（Slack通知）
- JSON（設定管理）

---

## 機能
1. 指定URLのニュースサイトからトップ記事を抽出
2. Slackに記事タイトルを自動送信
3. 設定ファイル（config.json）でURLやSlack Webhookを管理
4. 定期実行や手動実行が可能

---

## ファイル構成
