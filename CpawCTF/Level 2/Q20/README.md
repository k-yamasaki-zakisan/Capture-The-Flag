## 問題文
Q20.[Crypto]Block Cipher

与えられたC言語のソースコードを読み解いて復号してフラグを手にれましょう。

暗号文：cpaw{ruoYced_ehpigniriks_i_llrg_stae}

crypto100.c

## 解答
ダウンロードするとC言語のファイルであったので、macでCをコンパイルする方法をググる

```
% gcc CpawCTF/Level\ 2/Q20/crypto100.c
//a.outファイルが作成される
```

コンパイルされたファイルを実行してみる

```
% ./a.out
zsh: segmentation fault  ./a.out
```

エラーが起きているっぽいので調べてみると実行エラーらしい(コンパイルはうまくいっている)

Cのソースを見てみると変換する文字列とkey(数字)がいるらしい

```
% 実行ファイル [変換文字列] [数字]
```
で動いた！

```
% ./a.out ruoYced_ehpigniriks_i_llrg_stae 1
cpaw{ruoYced_ehpigniriks_i_llrg_stae}

% ./a.out ruoYced_ehpigniriks_i_llrg_stae 2
cpaw{urYoec_dheipngriki_s_illgrs_ate}

% ./a.out ruoYced_ehpigniriks_i_llrg_stae 3
cpaw{ourecYe_diphingkiri_sll__grats}

% ./a.out ruoYced_ehpigniriks_i_llrg_stae 4
cpaw{Your_deciphering_skill_is_great}
```

key=4でそれらしき出力が得られた(flag取得)

## 参考
macでC言語コンパイル：https://webkaru.net/clang/mac-gcc-compile/