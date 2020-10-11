## 問題文
Q19.[Misc]Image!

Find the flag in this zip file.

file

## 解答
ダウンロードしたzipファイルをダブルクリックで解凍しようとしたが、「対応していないformatのため開けない」とエラー発生

Mac_OSでとりあえずunzipコマンドを試してみた　→　解凍できた

解凍後のmimetypeというファイル内で「application/vnd.oasis.opendocument.graphics」という記述書を発見

ググったらword等で開ける型式らしい事を知った

そのためLibraOfficeにzipファイルを投げ込むと画像ファイルが出現

黒塗り箇所をドラッグしてflagを取得