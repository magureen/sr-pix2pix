# sr-pix2pix
pix2pixを使った超解像
- 拡大処理 X4
- ノイズ除去 弱いガウシアンぼかし&jpegノイズ

## Results
![demo1](https://raw.githubusercontent.com/magureen/sr-pix2pix/master/img/demo1.png)
![demo2](https://raw.githubusercontent.com/magureen/sr-pix2pix/master/img/demo2.png)

## Usage
Getting
```
git clone https://github.com/magureen/sr-pix2pix.git
cd sr-pix2pix
```
Install tensorflow
```
pip install tensorflow # or tensorflow-gpu
```
Run
```
python sr.py test1.jpg test2.jpg
# output test1-sr.png test2-sr.png
```

Windows用パッケージ

[ダウンロード](https://github.com/magureen/sr-pix2pix/releases/download/0.0.0/sr-pix2pix.zip)

画像ファイルをsr.batにドラッグアンドドロップすると同じフォルダに-sr.pngが生成されます

