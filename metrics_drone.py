import imagecodecs
import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr


# def psnr(img1, img2):
#     mse = np.mean((img1 - img2) ** 2)
#     if mse == 0:
#         return float('inf')
#     max_val = 255.0
#     return 20 * np.log10(max_val / np.sqrt(mse))


img_ori = imagecodecs.imread('Gregg1_2/DJI_0001.JPG')
img_comp = imagecodecs.imread('Gregg1_2_compressed/DJI_0001.webp')

# img_comp = np.transpose(img_comp, (2, 0, 1))

print(np.shape(img_ori))
print(np.shape(img_comp))


img_ori_arr = np.asarray(img_ori, dtype=np.float32)
img_comp_arr = np.asarray(img_comp, dtype=np.float32)

psnr_value = psnr(img_ori_arr, img_comp_arr, data_range=img_ori_arr.max() - img_ori_arr.min()) 

# Calculate SSIM
ssim_value = ssim(img_ori_arr, img_comp_arr, data_range=img_ori_arr.max() - img_ori_arr.min(),channel_axis=2)
print("PSNR:", psnr_value)
print("SSIM:", ssim_value)
