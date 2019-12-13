# sr-pix2pix
pix2pixを使った超解像
- 拡大処理 X4
- ノイズ除去 弱いガウシアンぼかし&jpegノイズ

## Results
![demo1](https://raw.githubusercontent.com/magureen/sr-pix2pix/master/img/demo1.png)
![demo2](https://raw.githubusercontent.com/magureen/sr-pix2pix/master/img/demo2.png)

## Run
Getting
```
git clone https://github.com/magureen/sr-pix2pix.git
cd sr-pix2pix
```
Install tensorflow2.0
```
pip install tensorflow-gpu # or tensorflow
'''
Run
'''
python sr.py test1.jpg test2.jpg
```
