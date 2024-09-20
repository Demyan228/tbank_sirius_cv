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
        bg_rm_img = remove(img)
        if not bg_color:
            return bg_rm_img
        width, height = bg_rm_img.size
        background = Image.new("RGBA", (width, height), bg_color)

        # Накладываем оригинальное изображение поверх нового фона, используя альфа-канал как маску
        background.paste(bg_rm_img, (0, 0), bg_rm_img)

        # Сохраняем результат
        background.save(out_path, "PNG")

white_shades_rgba = {
    "white": (255, 255, 255, 255),
    "snow": (255, 250, 250, 255),
    "ivory": (255, 255, 240, 255),
    "linen": (250, 240, 230, 255),
    "seashell": (255, 245, 238, 255),
    "old_lace": (253, 245, 230, 255),
    "floral_white": (255, 250, 240, 255),
    "ghost_white": (248, 248, 255, 255),
    "antique_white": (250, 235, 215, 255),
    "beige": (245, 245, 220, 255),
    "mint_cream": (245, 255, 250, 255),
    "azure": (240, 255, 255, 255),
    "honeydew": (240, 255, 240, 255),
    "alice_blue": (240, 248, 255, 255),
    "lavender_blush": (255, 240, 245, 255),
    "white_smoke": (245, 245, 245, 255),
    "gainsboro": (220, 220, 220, 255),
    "light_gray": (211, 211, 211, 255),
    "platinum": (229, 228, 226, 255),
    "pearl": (234, 224, 200, 255),
    "champagne": (247, 231, 206, 255),
    "alabaster": (242, 240, 230, 255),
    "eggshell": (240, 234, 214, 255)}
bg_color = white_shades_rgba["white"]

remove_bg("sirius_data", "res_data", bg_color=None)
