## 問題文

AUTHOR: MADSTACKS

Description
I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## 解説

訳わからん
文字列を 16bit の bytes に変換したら答えが得られるらしい

## flag

`picoCTF{16_bits_inst34d_of_8_d52c6b93}`
