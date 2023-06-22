# Fork of [Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.0. (🔥)

# Installation

```shell
pip install -r requirements.txt
```



[English](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB ) | [中文简体](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/blob/master/README_CN.md)
# Ultra-Light-Fast-Generic-Face-Detector-1MB 
# Ultra-lightweight face detection model
![img1](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/blob/master/readme_imgs/27.jpg)
This model is a lightweight facedetection model designed for edge computing devices.

- In terms of model size, the default FP32 precision (.pth) file size is **1.04~1.1MB**, and the inference framework int8 quantization size is about **300KB**.
- In terms of the calculation amount of the model, the input resolution of 320x240 is about **90~109 MFlops**.
- There are two versions of the model, version-slim (network backbone simplification,slightly faster) and version-RFB (with the modified RFB module, higher precision).
- Widerface training pre-training model with different input resolutions of 320x240 and 640x480 is provided to better work in different application scenarios.
- Support for onnx export for ease of migration and inference.
- [Provide NCNN C++ inference code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/tree/master/ncnn).
- [Provide MNN C++ inference code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/tree/master/MNN), [MNN Python inference code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/tree/master/MNN/python), [FP32/INT8 quantized models](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/tree/master/MNN/model).
- [Provide Caffe model](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/tree/master/caffe/model) and [onnx2caffe conversion code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/tree/master/caffe).
- [Caffe python inference code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/blob/master/caffe/ultra_face_caffe_inference.py) and [OpencvDNN inference code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/blob/master/caffe/ultra_face_opencvdnn_inference.py).
 
## Tested the environment that works
- Ubuntu16.04、Ubuntu18.04、Windows 10（for inference）
- Python3.6
- Pytorch1.2
- CUDA10.0 + CUDNN7.6

## Accuracy, speed, model size comparison
The training set is the VOC format data set generated by using the cleaned widerface labels provided by [Retinaface](https://github.com/deepinsight/insightface/blob/master/RetinaFace/README.md)  in conjunction with the widerface data set (PS: the following test results were obtained by myself, and the results may be partially inconsistent).
### Widerface test
- Test accuracy in the WIDER FACE val set (single-scale input resolution: **320*240 or scaling by the maximum side length of 320**)

Model|Easy Set|Medium Set|Hard Set
------|--------|----------|--------
libfacedetection v1（caffe）|0.65 |0.5       |0.233
libfacedetection v2（caffe）|0.714 |0.585       |0.306
Retinaface-Mobilenet-0.25 (Mxnet)   |0.745|0.553|0.232
version-slim|0.77     |0.671       |0.395
version-RFB|**0.787**     |**0.698**       |**0.438**


- Test accuracy in the WIDER FACE val set (single-scale input resolution: **VGA 640*480 or scaling by the maximum side length of 640** )

Model|Easy Set|Medium Set|Hard Set
------|--------|----------|--------
libfacedetection v1（caffe）|0.741 |0.683       |0.421
libfacedetection v2（caffe）|0.773 |0.718       |0.485
Retinaface-Mobilenet-0.25 (Mxnet)   |**0.879**|0.807|0.481
version-slim|0.853     |0.819       |0.539
version-RFB|0.855     |**0.822**       |**0.579**

> - This part mainly tests the effect of the test set under the medium and small resolutions.
> - RetinaFace-mnet (Retinaface-Mobilenet-0.25), from a great job [insightface](https://github.com/deepinsight/insightface), when testing this network, the original image is scaled by 320 or 640 as the maximum side length, so the face will not be deformed, and the rest of the networks will have a fixed size resize. At the same time, the result of the RetinaFace-mnet optimal 1600 single-scale val set was 0.887 (Easy) / 0.87 (Medium) / 0.791 (Hard).

### Terminal device inference speed

- Raspberry Pi 4B MNN Inference Latency **(unit: ms)** (ARM/A72x4/1.5GHz/input resolution: **320x240** /int8 quantization)

Model|1 core|2 core|3 core|4 core
------|--------|----------|--------|--------
libfacedetection v1|**28**    |**16**|**12**|9.7
Official Retinaface-Mobilenet-0.25 (Mxnet)   |46|25|18.5|15
version-slim|29     |**16**       |**12**|**9.5**
version-RFB|35     |19.6       |14.8| 11

- iPhone 6s Plus MNN (version tag：0.2.1.5) Inference Latency ( input resolution : **320x240** )[Data comes from  MNN official](https://www.yuque.com/mnn/en/demo_zoo#bXsRY)

Model|Inference Latency(ms)
------|--------
[slim-320](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/blob/master/MNN/model/version-slim/slim-320.mnn) |6.33
[RFB-320](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/blob/master/MNN/model/version-RFB/RFB-320.mnn)|7.8

- [Kendryte K210](https://kendryte.com/) NNCase Inference Latency (RISC-V/400MHz/input resolution: **320x240** /int8 quantization)[Data comes from NNCase](https://github.com/kendryte/nncase/tree/master/examples/fast_facedetect)

Model|Inference Latency(ms)
------|--------
[slim-320](https://github.com/kendryte/nncase/tree/master/examples/fast_facedetect/k210/kpu_fast_facedetect_example/slim-320.kmodel)|65.6
[RFB-320](https://github.com/kendryte/nncase/tree/master/examples/fast_facedetect/k210/kpu_fast_facedetect_example/RFB-320.kmodel)|164.8

### Model size comparison
- Comparison of several open source lightweight face detection models:

Model|model file size（MB）
------|--------
libfacedetection v1（caffe）| 2.58
libfacedetection v2（caffe）| 3.34
Official Retinaface-Mobilenet-0.25 (Mxnet) | 1.68
version-slim| **1.04**
version-RFB| **1.11** 

## Generate VOC format training data set and training process

1. Download the wideface official website dataset or download the training set I provided and extract it into the ./data folder:

  (1) The clean widerface data pack after filtering out the 10px*10px small face: [Baidu cloud disk (extraction code: cbiu)](https://pan.baidu.com/s/1MR0ZOKHUP_ArILjbAn03sw) 、[Google Drive](https://drive.google.com/open?id=1OBY-Pk5hkcVBX1dRBOeLI4e4OCvqJRnH )
  
  (2) Complete widerface data compression package without filtering small faces: [Baidu cloud disk (extraction code: ievk)](https://pan.baidu.com/s/1faHNz9ZrtEmr_yw48GW7ZA)、[Google Drive](https://drive.google.com/open?id=1sbBrDRgctEkymIpCh1OZBrU5qBS-SnCP )

2. **(PS: If you download the filtered packets in (1) above, you don't need to perform this step)** Because the wideface has many small and unclear faces, which is not conducive to the convergence of efficient models, it needs to be filtered for training.By default,faces smaller than 10 pixels by 10 pixels will be filtered.
run ./data/wider_face_2_voc_add_landmark.py
```Python
 python3 ./data/wider_face_2_voc_add_landmark.py
```
After the program is run and finished, the **wider_face_add_lm_10_10** folder will be generated in the ./data directory. The folder data and data package (1) are the same after decompression. The complete directory structure is as follows:
```Shell
  data/
    retinaface_labels/
      test/
      train/
      val/
    wider_face/
      WIDER_test/
      WIDER_train/
      WIDER_val/
    wider_face_add_lm_10_10/
      Annotations/
      ImageSets/
      JPEGImages/
    wider_face_2_voc_add_landmark.py
```

3. At this point, the VOC training set is ready. There are two scripts: **train-version-slim.sh** and **train-version-RFB.sh** in the root directory of the project. The former is used to train the **slim version** model, and the latter is used. Training **RFB version** model, the default parameters have been set, if the parameters need to be changed, please refer to the description of each training parameter in **./train.py**.

4. Run **train-version-slim.sh**  **train-version-RFB.sh**
```Shell
sh train-version-slim.sh or sh train-version-RFB.sh
```

## Detecting image effects (input resolution: 640x480)
![img1](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/blob/master/readme_imgs/26.jpg)
![img1](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/blob/master/readme_imgs/2.jpg)
![img1](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/blob/master/readme_imgs/4.jpg)
## PS

- If the actual production scene is medium-distance, large face, and small number of faces, it is recommended to use input size input_size: 320 (320x240) resolution for training, and use 320x240 ,160x120 or 128x96 image size input for inference, such as using the provided pre-training  model **version-slim-320.pth** or **version-RFB-320.pth** .
- If the actual production scene is medium or long distance,  medium or small face and large face number, it is recommended to adopt:

 (1) Optimal: input size input_size: 640 (640x480) resolution training, and use the same or larger input size for inference, such as using the provided pre-training model **version-slim-640.pth** or **version-RFB-640.pth** for inference, lower False positives.
 
 (2) Sub-optimal: input size input_size: 320 (320x240) resolution training, and use 480x360 or 640x480 size input for predictive reasoning, more sensitive to small faces, false positives will increase.
 
- The best results for each scene require adjustment of the input resolution to strike a balance between speed and accuracy.
- Excessive input resolution will enhance the recall rate of small faces, but it will also increase the false positive rate of large and close-range faces, and the speed of inference will increase exponentially.
- Too small input resolution will significantly speed up the inference, but it will greatly reduce the recall rate of small faces.
- The input resolution of the production scene should be as consistent as possible with the input resolution of the model training, and the up and down floating should not be too large.

## TODO LIST

- Add some test data

## Completed list
 - [Widerface test code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/tree/master/widerface_evaluate)
 - [NCNN C++ inference code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/tree/master/ncnn) ([vealocia](https://github.com/vealocia))
 - [MNN C++ inference code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/tree/master/MNN), [MNN Python inference code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/tree/master/MNN/python)
 - [Caffe model](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/tree/master/caffe/model) and [onnx2caffe conversion code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/tree/master/caffe)
 - [Caffe python inference code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/blob/master/caffe/ultra_face_caffe_inference.py) and [OpencvDNN inference code](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB/blob/master/caffe/ultra_face_opencvdnn_inference.py)
  
## Third-party related projects
 - [NNCase C++ inference code](https://github.com/kendryte/nncase/tree/master/examples/fast_facedetect)
 - [UltraFaceDotNet (C#)](https://github.com/takuya-takeuchi/UltraFaceDotNet)
 - [faceDetect-ios](https://github.com/Ian778/faceDetect-ios)
 - [Android-FaceDetection-UltraNet-MNN](https://github.com/jackweiwang/Android-FaceDetection-UltraNet-MNN)
 - [Ultra-Tensorflow-Model-Converter](https://github.com/jason9075/Ultra-Light-Fast-Generic-Face-Detector_Tensorflow-Model-Converter)
 - [UltraFace TNN C++ Demo](https://github.com/DefTruth/lite.ai.toolkit/blob/main/lite/tnn/cv/tnn_ultraface.cpp)
  
##  Reference
- [pytorch-ssd](https://github.com/qfgaohao/pytorch-ssd)
- [libfacedetection](https://github.com/ShiqiYu/libfacedetection/)
- [RFBNet](https://github.com/ruinmessi/RFBNet)
- [RFSong-779](https://github.com/songwsx/RFSong-779)
- [Retinaface](https://github.com/deepinsight/insightface/blob/master/RetinaFace/README.md)
