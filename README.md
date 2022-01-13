# VRDL_HW4_super_resolution

## Breif introduction
* Upsample the image and create the high resolution image with help of a low resolution image.

* model: [srresnet](https://arxiv.org/abs/1609.04802)

* Before Image Super-Resolution:
    - ![](https://i.imgur.com/VNuqorb.png)

* After Image Super-Resolution:
    - ![](https://i.imgur.com/3t5JIlI.png)


* Results: 
Test score PSNR: 27.5819


* Data: 
    * images count: 291

## Environment
- Python 3.7
- Pytorch 1.7.0
- CUDA 10.2

## Install packages

1. Install PyTorch and torchvision according to your cuda version. [official instructions](https://pytorch.org/)

2. Use the following command to install other requirements.
    ```shell
    pip install -r requirements.txt
    ```

## Dataset Preparation
You can download the data [here](https://drive.google.com/drive/folders/1Ta7iW82GHiNnGnz_25MoN9gAxJIzBEOR?usp=sharing).

### Reorganize data folder
After downloading, reorganize the data directory as follow:

```text
data
├── training_hr_images
|   ├── 2092.png
|   ├── 8049.png
|   └── ...
|
└── testing_lr_images
    ├── 00.png
    ├── 01.png
    └── ...
```

### Data Preprocessing

Split data into "train" and "val"
Split ratio: 8: 2 

```shell
python3 train_val_split.py
```

## Train
Train the model:

```shell
python3 train_srresnet.py
```

## Inference
If you just want to inference the results, the pretrained weight is stored in folder "models". The inference results will be stored in folder "results".

```shell
python3 inference.py
```

## Reference
[a-PyTorch-Tutorial-to-Super-Resolution](https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Super-Resolution)

[pytorch-SRResNet](https://github.com/twtygqyy/pytorch-SRResNet)

