## 問題文
Q22.[Web]Baby's SQLi - Stage 1-

困ったな……どうしよう……．
ぱろっく先生がキャッシュカードをなくしてしまったショックからデータベースに逃げ込んでしまったんだ．
うーん，君SQL書くのうまそうだね．ちょっと僕もWeb問作らなきゃいけないから，連れ戻すのを任せてもいいかな？
多分，ぱろっく先生はそこまで深いところまで逃げ込んで居ないと思うんだけども……．

とりあえず，逃げ込んだ先は以下のURLだよ．
一応，報酬としてフラグを用意してるからよろしくね！

https://ctf.spica.bz/baby_sql/

Caution
・sandbox.spica.bzの80,443番ポート以外への攻撃は絶対にしないようにお願いします．
・あなたが利用しているネットワークへの配慮のためhttpsでの通信を推奨します．

## 解答
URLで遷移するとSQLを発行するinputタグとヒント文がある

```
Stage1.Writing SQL
さて，SQLのおさらいです．下のフォームはSQL文を入れるとそのまま動作します．どうやらぱろっく先生は「palloc_home」というテーブルの2番目にいるようです．
```

ヒントに従いSQLを発行してみる

```
SELECT * FROM palloc_home WHERE id=2;

id	flag	next stage url
2	Congrats! Flag is ... "cpaw{palloc_escape_from_stage1;(}".Go to next stage!	https://ctf.spica.bz/baby_sql/stage2_7b20a808e61c8573461cf92b1fe63b3f/index.php
```

flagカラムでflagを発見した
