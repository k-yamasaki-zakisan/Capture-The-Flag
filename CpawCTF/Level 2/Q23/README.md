## 問題文
Q28.[Network] Can you login？

古くから存在するネットワークプロトコルを使った通信では、セキュリティを意識していなかったこともあり、様々な情報が暗号化されていないことが多い。そのため、パケットキャプチャをすることでその情報が簡単に見られてしまう可能性がある。

次のパケットを読んで、FLAGを探せ！

network100.pcap

## 解答
.pcapファイルの解析をすべく、wiresharkを起動してパケットを眺めていた

infoにLogin successfulであったり認証情報を発見

ftpサーバーにログインすべくmac_osにftpコマンドを使うためのパッケージをインストール

```
% brew install tnftp
```

ftpサーバーへの進入と秘密ファイルの入手方法を以下に示す

```
% ftp
ftp> open
(to) 157.7.52.186
Connected to 157.7.52.186.
220 Welcome to Cpaw CTF FTP service.
Name (157.7.52.186:kazu): cpaw_user
331 Please specify the password.
Password: 5f4dcc3b5aa765d61d8327deb882cf99
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -l
229 Entering Extended Passive Mode (|||60009|).
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp            36 Sep 01  2017 dummy
226 Directory send OK.
ftp> ls -la
229 Entering Extended Passive Mode (|||60020|).
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp            42 Jun 18  2019 .
drwxr-xr-x    2 ftp      ftp            42 Jun 18  2019 ..
-rw-r--r--    1 ftp      ftp            39 Sep 01  2017 .hidden_flag_file
-rw-r--r--    1 ftp      ftp            36 Sep 01  2017 dummy
226 Directory send OK.
ftp> get .hidden_flag_file
local: .hidden_flag_file remote: .hidden_flag_file
229 Entering Extended Passive Mode (|||60005|).
150 Opening BINARY mode data connection for .hidden_flag_file (39 bytes).
100% |****************************************|    39       50.98 KiB/s    00:00 ETA
226 Transfer complete.
39 bytes received in 00:00 (4.11 KiB/s)
```

ローカルにダウンドードした「.hidden_flag_file」内でflagを取得した