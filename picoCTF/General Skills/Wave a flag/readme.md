## 問題文

AUTHOR: SYREAL

Description
Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

## 解説

バイナリファイルらしいから可読部分だけでも炙り出そうと考えた

```
% strings picoCTF/General\ Skills/Wave\ a\ flag/warm | less | grep pico
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}
```

## flag

`picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}`
