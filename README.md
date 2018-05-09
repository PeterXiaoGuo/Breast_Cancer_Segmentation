# Pytorch Breast Cancer Segmentation with U-Net

Customized implementation of the [U-Net](https://arxiv.org/pdf/1505.04597.pdf) in Pytorch for Breast Cancer Segmentation (https://bioimage.ucsb.edu/research/bio-segmentation)

This repository is based on the repository of milesial (https://github.com/milesial/Pytorch-UNet)

## Usage

### Prediction

You can easily test the output masks on your images via the CLI.

To see all options:
`python predict.py -h`

To predict a single image and save it:

`python predict.py -i image.jpg -o ouput.jpg`

To predict a multiple images and show them without saving them:

`python predict.py -i image1.jpg image2.jpg --viz --no-save`

You can use the cpu-only version with `--cpu`.

You can specify which model file to use with `--model MODEL.pth`.

### Training

`python train.py -h` should get you started. A proper CLI is yet to be added.

## Warning
In order to process the image, it is split into two squares (a left on and a right one), and each square is passed into the net. The two square masks are then merged again to produce the final image. As a consequence, the height of the image must be strictly superior than half the width. Make sure the width is even too.

## Dependencies
This package depends on [pydensecrf](https://github.com/lucasb-eyer/pydensecrf), available via `pip install`.

## Notes on memory

The model has be trained from scratch on a GTX1070 8GB.
Training with images of 896x768 and a batch size of 4 takes 6GB of memory.
This assumes you use bilinear up-sampling, and not transposed convolution in the model.
