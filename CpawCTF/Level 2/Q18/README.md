## 問題文
Q18.[Forensic]leaf in forest

このファイルの中にはフラグがあります。探してください。
フラグはすべて小文字です！

file

## 解答
ダウンロードしたファイルは拡張子がなかったためfileでタイプを調査

```
% file misc100
misc100: pcap capture file, microsecond ts (little-endian) - version 0.0 (linktype#1768711542, capture length 1869357413)
```

pcapタイプであることが判明した。

Wiresharkで開くかを検討していたら、テキストファイルとしてメモ帳やvsコードで展開ができた

中身は大量の「lovelive!」の文字列となっていたためpythonのスクリプトで「lovelive!」を消した文字列を取得

アルファベットの大文字が３つ不自然に続いている文字列てあったが、
頭の文字列が「CCCPPPAAAWWW{{{」となっていたためcpaw{と変換できると考えられる

pyhtonのスクリプトを修正してflagを取得

cpaw{mgrep}

## コード 
参照：GetUpperStr.py