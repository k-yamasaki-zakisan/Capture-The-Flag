## 問題文

AUTHOR: SYREAL

Description
There is a nice program that you can talk to by using this command in a shell: \<span style="color: red; ">\$ nc mercury.picoctf.net 21135</span>, but it doesn't speak English...

## 解説

\$ nc mercury.picoctf.net 21135
で謎の数字の羅列が出てくる
ヒントに ASCII とかあるから数字をアルファベットに変更するやつかと思い
python でスクリプトを書いて AC

## flag

`picoCTF{g00d_k1tty!_n1c3_k1tty!_afd5fda4}`
