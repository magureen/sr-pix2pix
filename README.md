# sr-pix2pix
pix2pixを使った超解像
- 拡大処理 X4
- ノイズ除去 弱いガウシアンぼかし&jpegノイズ

## Results
![demo1](https://user-images.githubusercontent.com/58849368/70858751-522e5d80-1f4b-11ea-9ad5-91c659c53b3f.png)
![demo2](https://user-images.githubusercontent.com/58849368/70858753-5c505c00-1f4b-11ea-8860-da210f9c93c2.png)

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

