## 問題文
Q23.[Reversing]またやらかした！

またprintf（）をし忘れたプログラムが見つかった。
とある暗号を解くプログラムらしい…

reversing200

## 解説
ファイルを調べてみるとまたまたELF系のファイルになっていた

```
% file CpawCTF/Level\ 3/Q23/rev200 
ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=e87140105d6b5c8ea9b0193380ab3b79bfdcd85b, not stripped
```

Level2 Q21と同様に文字列検索してみるが反応なし
```
% strings rev100 | grep cpaw

```

アセンブラコードの閲覧のために以下のライブラリをインストール
```
brew install gdb
```
gdbコマンドでrev200を実行！

```
% gdb rev200
(gdb) disas main
   0x080483ed <+0>:     push   %ebp
   0x080483ee <+1>:     mov    %esp,%ebp
   0x080483f0 <+3>:     push   %edi
   0x080483f1 <+4>:     push   %ebx
   0x080483f2 <+5>:     add    $0xffffff80,%esp
   0x080483f5 <+8>:     movl   $0x7a,-0x78(%ebp)

//とにかく値を代入していく、bitずつずれていきます。またなぜかメモリが降順

   0x080483fc <+15>:    movl   $0x69,-0x74(%ebp)
   0x08048403 <+22>:    movl   $0x78,-0x70(%ebp)
   0x0804840a <+29>:    movl   $0x6e,-0x6c(%ebp)
   0x08048411 <+36>:    movl   $0x62,-0x68(%ebp)
--Type <RET> for more, q to quit, c to continue without paging--
   0x08048418 <+43>:    movl   $0x6f,-0x64(%ebp)
   0x0804841f <+50>:    movl   $0x7c,-0x60(%ebp)
   0x08048426 <+57>:    movl   $0x6b,-0x5c(%ebp)
   0x0804842d <+64>:    movl   $0x77,-0x58(%ebp)
   0x08048434 <+71>:    movl   $0x78,-0x54(%ebp)
   0x0804843b <+78>:    movl   $0x74,-0x50(%ebp)
   0x08048442 <+85>:    movl   $0x38,-0x4c(%ebp)
   0x08048449 <+92>:    movl   $0x38,-0x48(%ebp)
   0x08048450 <+99>:    movl   $0x64,-0x44(%ebp)
   0x08048457 <+106>:   movl   $0x19,-0x7c(%ebp)
   0x0804845e <+113>:   lea    -0x40(%ebp),%ebx
--Type <RET> for more, q to quit, c to continue without paging--
   0x08048461 <+116>:   mov    $0x0,%eax
   0x08048466 <+121>:   mov    $0xe,%edx
   0x0804846b <+126>:   mov    %ebx,%edi
   0x0804846d <+128>:   mov    %edx,%ecx
   0x0804846f <+130>:   rep stos %eax,%es:(%edi)
   0x08048471 <+132>:   movl   $0x0,-0x80(%ebp)
   0x08048478 <+139>:   jmp    0x8048491 <main+164>

//ループ開始

   0x0804847a <+141>:   mov    -0x80(%ebp),%eax
   0x0804847d <+144>:   mov    -0x78(%ebp,%eax,4),%eax
   0x08048481 <+148>:   xor    -0x7c(%ebp),%eax
   0x08048484 <+151>:   mov    %eax,%edx
--Type <RET> for more, q to quit, c to continue without paging--
   0x08048486 <+153>:   mov    -0x80(%ebp),%eax
   0x08048489 <+156>:   mov    %edx,-0x40(%ebp,%eax,4)
   0x0804848d <+160>:   addl   $0x1,-0x80(%ebp)
   0x08048491 <+164>:   cmpl   $0xd,-0x80(%ebp)
   0x08048495 <+168>:   jle    0x804847a <main+141>

//+<141>に戻ります

   0x08048497 <+170>:   mov    $0x0,%eax
   0x0804849c <+175>:   sub    $0xffffff80,%esp
   0x0804849f <+178>:   pop    %ebx
   0x080484a0 <+179>:   pop    %edi
   0x080484a1 <+180>:   pop    %ebp
   0x080484a2 <+181>:   ret    
--Type <RET> for more, q to quit, c to continue without paging--
End of assembler dump.
```

ここからアセンブラを言語に変換して実行するといいらいいがよくわからんからスキップ

## 参考
gdbコマンドインストール：https://qiita.com/yuzu_afro/items/988020dd65fb4f43962a

答え：https://rightcode.co.jp/blog/information-technology/c-language-gdb-decompile-vernam-cipher-decryption