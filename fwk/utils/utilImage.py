from PIL import Image, ImageChops, ImageDraw
import math
import operator
from functools import reduce


def image_compare(img1_path, img2_path, save_path="", fragmentation=3, outline_on_first=False) -> bool:
    image1 = Image.open(img1_path)
    image2 = Image.open(img2_path)
    img_tmp = image2
    if outline_on_first:
        img_tmp = image1
    size = img_tmp.size
    weight = int(size[0] // fragmentation)
    height = int(size[1] // fragmentation)
    for j in range(fragmentation):
        for i in range(fragmentation):
            box = (weight * i, height * j, weight * (i + 1), height * (j + 1))
            region1 = image1.crop(box)
            region2 = image2.crop(box)

            region_tmp = region2
            if outline_on_first:
                region_tmp = region1

            diff = ImageChops.difference(region1.convert('RGB'), region2.convert('RGB'))
            if diff.getbbox():
                draw = ImageDraw.Draw(region_tmp)
                draw.rectangle(diff.getbbox(), outline=(0, 255, 0))
                img_tmp.paste(region2, box)
    if save_path != "":
        img_tmp.save(save_path)
    img_tmp.show(12)

    #region.show(1)
    #region.save('{}{}.png'.format(j, i))

    diff = ImageChops.difference(image1.convert('RGB'), image2.convert('RGB'))

    if outline_on_first:
        img_tmp = image1
    if diff.getbbox():
        draw = ImageDraw.Draw(img_tmp)
        draw.rectangle(diff.getbbox(), outline=(0, 255, 0))
        if save_path != "":
            img_tmp.save(save_path)
        img_tmp.show(12)
        return True
    return False




def image_compareb(img1_path, img2_path):
    with Image.open(img1_path) as im1:
        with Image.open(img2_path) as im2:
            max_size = (max(im1.width, im2.width), max(im1.height, im2.height))
            imA = Image.new("RGB", max_size)
            imA.paste(im1.convert("RGB"))
            imB = Image.new("RGB", max_size)
            imB.paste(im2.convert("RGB"))
    pxA = imA.load()
    pxB = imB.load()
    outlined = []
    rects = []
    d = ImageDraw.Draw(imB)
    for x in range(max_size[0]):
        for y in range(max_size[1]):
            if (x, y) in outlined or pxA[x, y] == pxB[x, y]:
                continue

            w, h = 10, 20
            overlap = False
            for a in range(w):
                for b in range(h):
                    point = (x + a, y + b)
                    if point in outlined:
                        overlap = True
                        break
                    outlined.append(point)
                if overlap:
                    break
            if overlap:
                continue
            rects.append((x, y, x + w, y + h))
    for rect in rects:
        d.rectangle(rect, outline="#f00")
    imB.show(11)
    # imB.save("out.png")


def image_compare2(img1_path, img2_path):
    image1 = Image.open(img1_path)
    image2 = Image.open(img2_path)
    diff = ImageChops.difference(image1, image2)
    h = diff.histogram()
    sq = (value * ((idx % 256) ** 2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares / float(image1.size[0] * image2.size[1]))
    return print(rms)


# f1
def image_compare(img1_path, img2_path, save_path="", outline_on_first=False) -> bool:
    image1 = Image.open(img1_path)
    image2 = Image.open(img2_path)
    diff = ImageChops.difference(image1.convert('RGB'), image2.convert('RGB'))
    img_tmp = image2
    if outline_on_first:
        img_tmp = image1
    if diff.getbbox():
        draw = ImageDraw.Draw(img_tmp)
        draw.rectangle(diff.getbbox(), outline=(0, 255, 0))
        if save_path != "":
            img_tmp.save(save_path)
        return True
    return False


# f1
def image_compares(img1_path, img2_path):
    image1 = Image.open(img1_path)
    image2 = Image.open(img2_path)
    h1 = image1.histogram()
    h2 = image2.histogram()
    result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    return 1


# f2
def calculate(image1, image2):
    image1 = Image.open(img1_path)
    image2 = Image.open(img2_path)
    g = image1.histogram()
    s = image2.histogram()
    assert len(g) == len(s), "error"
    data = []
    for index in range(0, len(g)):
        if g[index] != s[index]:
            data.append(1 - abs(g[index] - s[index]) / max(g[index], s[index]))
        else:
            data.append(1)
    return sum(data) / len(g)


def split_image(image, part_size):
    pw, ph = part_size
    w, h = image.size
    sub_image_list = []
    assert w % pw == h % ph == 0, "error"
    for i in range(0, w, pw):
        for j in range(0, h, ph):
            sub_image = image.crop((i, j, i + pw, j + ph)).copy()
            sub_image_list.append(sub_image)
    return sub_image_list


def image_comparea(img1_path, img2_path, size=[256, 256], part_size=[64, 64]):
    image1 = Image.open(img1_path)
    image2 = Image.open(img2_path)
    img1 = image1.resize(size).convert("RGB")
    sub_image1 = split_image(img1, part_size)
    img2 = image2.resize(size).convert("RGB")
    sub_image2 = split_image(img2, part_size)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
        x = size[0] / part_size[0]
        y = size[1] / part_size[1]
        pre = round((sub_data / (x * y)), 6)
        print(pre * 100)
    return pre * 100


if __name__ == '__main__':
    img1_path = r"D:\Dev\Result\20220112_092002_412374\Old_imgs\o.png"  # 指定图片路径
    img2_path = r"D:\Dev\Result\20220112_092002_412374\Old_imgs\2.png"
    # result = rmsdiff(img1, img2)
    print(image_compare(img1_path, img2_path))
