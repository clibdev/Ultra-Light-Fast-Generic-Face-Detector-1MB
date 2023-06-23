# Fork of [Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.0. (🔥)
* Sample script [detect_img.py](detect_img.py) for inference of single image.
* The following deprecations and errors has been fixed:
  * DeprecationWarning: 'np.float' is a deprecated alias for builtin 'float'.
  * FutureWarning: Cython directive 'language_level' not set.
  * Cython Warning: Using deprecated NumPy API.
  * cv2.error: Can't parse 'xx'. Sequence item with index 0 has a wrong type.
  * cv2.error: Can't parse 'xx'. Expected sequence length 4, got 2.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

| Name                     | Easy  | Medium  | Hard  | Link                                                                                                                           |
|--------------------------|-------|---------|-------|--------------------------------------------------------------------------------------------------------------------------------|
| version-slim (320 x 240) | 0.770 | 0.671   | 0.395 | [PyTorch](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases/latest/download/version-slim-320.pth) |
| version-RFB (320 x 240)  | 0.787 | 0.698   | 0.438 | [PyTorch](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases/latest/download/version-RFB-320.pth)  |
| version-slim (640 x 480) | 0.853 | 0.819   | 0.539 | [PyTorch](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases/latest/download/version-slim-640.pth) |
| version-RFB (640 x 480)  | 0.855 | 0.822   | 0.579 | [PyTorch](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases/latest/download/version-RFB-640.pth)  |

# Inference

```shell
python detect_img.py --net_type RFB --path imgs/1.jpg
```

# WIDERFace evaluation

* Download WIDERFace [validation dataset](https://drive.google.com/file/d/1GUCogbp16PMGa39thoMMeWxp7Rp5oM8Q/view).
* Move dataset to `data/widerface/val` directory.

```shell
cd widerface_evaluate
```
```shell
python evaluation_on_widerface.py
```
```shell
python setup.py build_ext --inplace
```
```shell
python evaluation.py
```
