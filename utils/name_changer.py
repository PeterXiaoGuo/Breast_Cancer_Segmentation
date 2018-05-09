import os

files_path = '/home/henning/PycharmProjects/Pytorch-UNet/data/train_masks/'

lst = os.listdir(files_path)

for file_name in lst:
    if file_name.startswith("ytma"):
        os.rename(files_path + file_name, files_path + file_name + '.tif')

