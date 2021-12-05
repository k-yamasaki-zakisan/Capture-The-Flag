## 問題文

AUTHOR: SYREAL

Description
Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?

## 解説

Python が与えられる
flag ファイルを与えられるが意味不明
cryptography.fernet とパスワードを使って flag を decode するとなんか良さそう

```
% python3 picoCTF/General\ Skills/Python\ Wrangling/ende.py -d picoCTF/General\ Skills/Python\ Wrangling/flag.txt.en
Please enter the password:ac9bd0ffac9bd0ffac9bd0ffac9bd0ff
picoCTF{4p0110_1n_7h3_h0us3_ac9bd0ff}
```

## flag

`picoCTF{4p0110_1n_7h3_h0us3_ac9bd0ff}`
