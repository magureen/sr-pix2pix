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
Install tensorflow2.0
```
pip install tensorflow-gpu # or tensorflow
```
Run
```
python sr.py test1.jpg test2.jpg # output test1-sr.png test2-sr.png
```

Use f128 Model
```
python sr.py --model ./model/generator_f128.h5 test1.jpg
```

Windows

[Download](https://) and extract

Drag and drop image file to sr.bat

tested environment
- Windows 7
- cuda 10.0
- cuDNN 7.6.5 for CUDA 10.0
