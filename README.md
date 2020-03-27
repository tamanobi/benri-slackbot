# 便利機能を詰め込んだSlackApps

このプロジェクトは、 [STECH](https://peraichi.com/landing_pages/view/stech2020) 内で作成されたものです。

# 予定

- 今日作るものの紹介
  - ニュースを教えてくれるボット
- 登場する技術要素
  - 言語・環境: Python, Flask, Poetry
  - コーディング: VS Code
  - API: Slack API, Qiita API, はてなブックマーク RSS, Flickr API
  - ストレージ(検索エンジン): Argolia
  - インフラ: now
  - 開発プロクシ: ngrok
  - CI/CD
- Slack Apps
  - Slack Apps 作成
  - Incoming Webhook でSlack API入門
  - Python環境の用意をする
  - メンションに反応させてみる
    - ngrok を使って開発する
  - テストコードを書いて実行してみる
  - 実際にインターネットに公開してみる
  - image hogehoge で画像検索させる
    - Flickr APIを使う
  - news ではてなブログのニュースを流させる
    - はてなブックマーク RSSを使う
  - news hogehoge でQiitaから記事を取ってくる
    - Qiita APIを使う
- CI/CDを使う
  - GitHub Actionsで自動デプロイ
- データを保存させてみる
  - DBを使うのが面倒だったのでArgoliaで無料にする
  - add で単語を登録する
  - find で単語を探す(誰がいつ登録したか返す)
- 終わり
