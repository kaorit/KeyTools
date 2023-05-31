# feed2keys.py について

Misskey, Calckey で RSS を購読するためのツールです。

動作確認は以下にて行なっています。

* Ubuntu 22.04.2 LTS
* Python 3.10.6
* Calckey 14.0.0-rc
* Feedparser 6.0.10
* Misskey.py 4.1.0



## 事前準備
### Feedparser をインストールする

Feedparser は RSS / Atomフィードを解析（パース）してサイトの新着記事などの情報を抽出してくれるサードパーティライブラリです。これがないと始まらないのでインストールします。


 ```
$ pip install feedparser
```
※環境によっては```pip3```を使います


詳細: [Python, feedparserでRSS, Atomフィードを解析](https://note.nkmk.me/python-feedparser-tutorial/)

開発: [Github/feedparser](https://github.com/kurtmckee/feedparser)


### Misskey.py をインストールする

Misskey, Calckey への投稿に不可欠なのでインストールします。

```
$ pip install Misskey.py
```


詳細: [Github/Misskey.py](https://github.com/YuzuRyo61/Misskey.py/blob/main/README-JP.md)



## feed2keys.py の使い方
### 動作テスト

使う前に以下の2箇所に設定を書き込みます。
```
#mk = Misskey("yourdomain.ltd", i="API_Key") <== 投稿するアカウントの API Key を設定
d = feedparser.parse('https://www,domain.ltd/rss')
```

保存したらターミナルで1度動かしてみましょう。



```
$ python3 feed2keys.py
```

タイトル、Link url、要約が表示されれば動作確認は OK です。
もしエラーが出たら要約が用意されていない RSS ですので一部変更（下部に記載あり）が必要です。
変更を加えてから再度動かして確認してみてください。


#### 変更が必要な場合

以下の記載を削除してください。
```
   {summaries} //19行目は行削除
 summaries=e['summary'], //22行目
```



### 設定

それではここから本格的に動作させる準備に入ります。

この2箇所は "#" を取ります。
```
#mk = Misskey("yourdomain.ltd", i="API_Key")
#mk.notes_create(text=string, visibility='followers')

　　　⬇︎
mk = Misskey("yourdomain.ltd", i="API_Key")
mk.notes_create(text=string, visibility='followers')

```


ここには "#" を付けます。
```
print(string)

　　　⬇︎
#print(string)
```

これでファイルへの設定は終了です。




### 投稿する

公開範囲は他のサーバーに迷惑をかけないようにデフォルトでフォロワーのみになっています。
実際に動かしてみましょう。

```
$ python3 feed2keys.py
```

これで投稿されていればスクリプトの設定は終了です。



### cron で自動化する

スクリプトが一定時間毎に動くように cron を設定します。

```
$ crontab -e
```

ファイルの末尾に以下を追記します



**毎時5分で1時間おきにコマンドを実行する場合**
```
5 * * * * /usr/bin/python3 /home/calckey/bot/feed2keys.py
```
※パスはご自分の環境に合わせて設定してください。



実際に動作することを確認したら設定はすべて完了です。
