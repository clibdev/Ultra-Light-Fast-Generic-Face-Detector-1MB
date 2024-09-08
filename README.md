# Fork of [Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.4. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases). (🔥)
* Sample script [detect_img.py](detect_img.py) for inference of single image.
* Added command line arguments to [convert_to_onnx.py](convert_to_onnx.py).
* The following deprecations and errors has been fixed:
  * DeprecationWarning: 'np.float' is a deprecated alias for builtin 'float'.
  * FutureWarning: You are using 'torch.load' with 'weights_only=False'.
  * FutureWarning: Cython directive 'language_level' not set.
  * Cython Warning: Using deprecated NumPy API.
  * cv2.error: Can't parse 'xx'. Sequence item with index 0 has a wrong type.
  * cv2.error: Can't parse 'xx'. Expected sequence length 4, got 2.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

* Download links:

| Name               | Model Size (MB) | Link                                                                                                                                                                                                                                                               | SHA-256                                                                                                                              |
|--------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| UltraFace-slim-320 | 1.1<br>1.2      | [PyTorch](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases/latest/download/ultraface-slim-320.pth)<br>[ONNX](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases/latest/download/ultraface-slim-320.onnx) | cd24abce45da5dbc7cfd8167cd3d5f955382dfc9d9ae9459f0026abd3c2e38a4<br>3a85d818ae391c030694f12558d3b2edf3e47b4bc0916fa5a2f5330867a98cb7 |
| UltraFace-RFB-320  | 1.2<br>1.2      | [PyTorch](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases/latest/download/ultraface-rfb-320.pth)<br>[ONNX](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases/latest/download/ultraface-rfb-320.onnx)   | c722b4427cc71642768baef6e15c659931b56f07425e5d2b0ec033ad41b145b3<br>8611231d4e6c1f3cda9eb5365518ab1c230df71090c11ed8e701b6ab9b7c58bd |
| UltraFace-slim-640 | 1.1<br>1.5      | [PyTorch](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases/latest/download/ultraface-slim-640.pth)<br>[ONNX](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases/latest/download/ultraface-slim-640.onnx) | 02ca778098127c46d2b2680f1c398c7b993c12a424e94c34e6d608beb73481e4<br>5380b75201e135e4b2c42a5ae4b127e8e474b30f82dfcf8c0cacb254bbf5f243 |
| UltraFace-RFB-640  | 1.2<br>1.5      | [PyTorch](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases/latest/download/ultraface-rfb-640.pth)<br>[ONNX](https://github.com/clibdev/Ultra-Light-Fast-Generic-Face-Detector-1MB/releases/latest/download/ultraface-rfb-640.onnx)   | bf34512b1a93dc234178e8a701ecf25c6afddf335a3226accf62982536e160b5<br>a3d2fa1ccd444f244716d96fcf0d32d454e422cb8163faa840f80968e25d6f77 |

* Evaluation results on WIDERFace dataset:

| Name               | Image Size<br>(pixels) | Easy  | Medium | Hard  |
|--------------------|------------------------|-------|--------|-------|
| UltraFace-slim-320 | 320 x 240              | 0.770 | 0.671  | 0.395 |
| UltraFace-RFB-320  | 320 x 240              | 0.787 | 0.698  | 0.438 |
| UltraFace-slim-640 | 640 x 480              | 0.853 | 0.819  | 0.539 |
| UltraFace-RFB-640  | 640 x 480              | 0.855 | 0.822  | 0.579 |

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

# Export to ONNX format

```shell
pip install onnx
```
```shell
python convert_to_onnx.py --model_path models/pretrained/version-slim-320.pth --net_type slim --input_size 320
python convert_to_onnx.py --model_path models/pretrained/version-slim-640.pth --net_type slim --input_size 640
python convert_to_onnx.py --model_path models/pretrained/version-RFB-320.pth --net_type RFB --input_size 320
python convert_to_onnx.py --model_path models/pretrained/version-RFB-640.pth --net_type RFB --input_size 640
```
