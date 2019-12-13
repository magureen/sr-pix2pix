# sr-pix2pix
pix2pixを使った超解像
- 拡大処理 X4
- ノイズ除去 弱いガウシアンぼかし&jpegノイズ

## Results
![demo1](https://raw.githubusercontent.com/magureen/sr-pix2pix/master/img/demo1.png)
![demo2](https://raw.githubusercontent.com/magureen/sr-pix2pix/master/img/demo2.png)

## Run
```
# Install tensorflow2.0
pip install tensorflow-gpu # or tensorflow

python sr.py test.png
```
