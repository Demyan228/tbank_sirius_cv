from rembg import remove
import os
from PIL import Image
import numpy as np

def get_average_color(img):
    img = img.resize((1, 1))  # Уменьшение картинки до 1x1 для усреднения цветов
    avg_color = img.getpixel((0, 0))  # Получаем цвет единственного пикселя

    avg_color_rgba = list(avg_color) + [255]
    return avg_color_rgba



def remove_bg(imgs_folder, res_folder, bg_color=None):
    if not os.path.isdir(res_folder):
        os.mkdir(res_folder)
    for img_name in os.listdir(imgs_folder):

        inp_path = os.path.join(imgs_folder, img_name)
        out_path = os.path.join(res_folder, f"{img_name.split('.')[0]}.png")
        if os.path.exists(out_path):
            continue
        img = Image.open(inp_path)
        if not bg_color:
            bg_rm_img = remove(img, bg_color=get_average_color(img))
        else:
            bg_rm_img = remove(img, bg_color=bg_color)
        bg_rm_img.save(out_path)

bg_color = (255, 255, 255, 255) # white

remove_bg("sirius_data", "res_data", bg_color)
