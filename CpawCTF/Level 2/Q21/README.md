## 問題文
Q21.[Reversing]reversing easy!

フラグを出す実行ファイルがあるのだが、プログラム(elfファイル)作成者が出力する関数を書き忘れてしまったらしい…

reverse100

## 解答
ファイルの種類を確認、ELFのバイナリ系であることがわかる
```
% file rev100
rev100: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=f94360edd84a940de2b74007d4289705601d618d, not stripped
```
出力関数がないとの事だったので、出力したい文字列はファイル内に存在していると推測

ググって文字列抽出コマンドstringsを発見

```
% strings rev100 | grep cpaw
D$Fcpawf
```

cpawの文字列を検索で発見したので、次の20行を表示させる

```
% strings rev100 | grep -A 20 cpaw
D$Fcpawf
D$J{
D$ y
D$$a
D$(k
D$,i
D$0n
D$4i
D$8k
D$<u
D$@!
T$Le3
[^_]
;*2$"
```

ぽいのが出てきた(flagを取得)

## 参考
バイナリファイルに含まれる文字列の抽出：https://qiita.com/rsooo/items/bb91071685f447ce29db
