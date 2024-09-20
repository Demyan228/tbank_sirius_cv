#Генерирует описание всего изображения, а чтобы получить описание именно товара нужно указать соответсивующий промпт
#Однако blip очень плохо работает с промптами(или я не разобрался как) он ставит промпт в начало и пытается его дополнить
#Это не подходит для задачи


from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import os
from confiq import device, num_batches
import numpy as np


def resize_images(images, size=(224, 224)):
    resized_images = [img.resize(size) for img in images]
    return resized_images


def split_list(lst, n):
    # Вычисляем размер каждого подсписка
    avg = len(lst) / n
    out = []
    last = 0.0

    # Разбиваем список на подсписки
    while last < len(lst):
        out.append(lst[int(last):int(last + avg)])
        last += avg

    return out


def generate_description(imgs_folder, prompt="", max_length=60):
    all_imgs = [Image.open(os.path.join(imgs_folder, img_name)) for img_name in os.listdir(imgs_folder)]
    desc = []
    c = 0
    for img in all_imgs:
        inputs = processor(img, prompt, return_tensors="pt").to(device)
        out = model.generate(**inputs, max_length=max_length)
        description = processor.decode(out[0],  skip_special_tokens=True)
        desc.append(description)
        c += 1
        if c >= 10:
            break


    return desc

lang_prompt = ("")

# Инициализировать модель и процессор
processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-large')
model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-large')
model.to(device)


print(*generate_description("res_data", lang_prompt), sep="\n")



