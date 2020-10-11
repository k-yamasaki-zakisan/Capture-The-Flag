## 問題文
Q16.[Network+Forensic]HTTP Traffic

HTTPはWebページを閲覧する時に使われるネットワークプロトコルである。
ここに、とあるWebページを見た時のパケットキャプチャファイルがある。
このファイルから、見ていたページを復元して欲しい

http_traffic.pcap

## 解答
ネットワーク パケットの解析とhttp プロトコルのコンテンツ化を求められているためWiresharkを利用

Wiresharkのfile→Exportobjects→HTTPから全てのコンテンツを復元

HTML,css,js,imgが復元でき、元のフォルダ構成に各ファイルを配置してメインページのHTMLをブラウザ表示してボタンクリックするとflagを取得できる

## 参考
WiresharkでHTTPコンテンツの復元：https://hebikuzure.wordpress.com/2010/07/12/wireshark-%E3%81%A7-http-%E3%82%B3%E3%83%B3%E3%83%86%E3%83%B3%E3%83%84%E3%82%92%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%8C%96%E3%81%99%E3%82%8B/