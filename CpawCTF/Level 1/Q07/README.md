## 問題文
Q7.[Reversing] Can you execute ?

拡張子がないファイルを貰ってこのファイルを実行しろと言われたが、どうしたら実行出来るのだろうか。
この場合、UnixやLinuxのとあるコマンドを使ってファイルの種類を調べて、適切なOSで実行するのが一般的らしいが…

問題ファイル： exec_me

## 解答
拡張子のない「exec_me」というファイルをダウンロードしたのでmac_osでfileコマンドでファイルの種類を調査、ELFのバイナリ形式のファイルであることが判明(以下にコマンドの結果を示す)

### Mac_os環境
```
% file exec_me
exec_me: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=663a3e0e5a079fddd0de92474688cd6812d3b550, not stripped
```

Mac_osでは実行できなかったためLinux環境(今回はDebian)を用意する必要があった

実行結果を以下に示す

### Mac_os環境
```
% ./exec_me
zsh: exec format error: ./exec_me
```

### Linux環境(Debian)
```
# ./exec_me
cpaw{Do_you_know_ELF_file?}
```






