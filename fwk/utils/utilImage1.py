from PIL import Image, ImageChops, ImageDraw
from enum import Enum


class Color(Enum):
    GREEN = (0, 255, 0),
    WHITE = (255, 255, 255),
    GREY = (190, 190, 190),
    YELLOW = (255, 255, 0),
    IGNORE = None


def image_compare(img1_path, img2_path, save_img1_path="", save_img2_path="", fragmentation=4, ignore_area_list=(()),
                  mark_ignored_area=True) -> int:
    fragments_area_size = 0
    if isinstance(img1_path, Image.Image):
        image1 = img1_path
        image2 = img2_path
    else:
        image1 = Image.open(img1_path)
        image2 = Image.open(img2_path)
    copied_image1 = image1.copy()
    copied_image2 = image2.copy()
    size1 = image1.size
    size2 = image2.size
    if size1 != size2:
        return 100
    for remove_box in ignore_area_list:
        __image_draw_rec(image1, remove_box, outline=Color.IGNORE, fill=Color.WHITE)
        __image_draw_rec(image2, remove_box, outline=Color.IGNORE, fill=Color.WHITE)
    weight = int(size1[0] // fragmentation)
    height = int(size1[1] // fragmentation)
    for j in range(fragmentation):
        for i in range(fragmentation):
            fragment_box = (weight * i, height * j, weight * (i + 1), height * (j + 1))
            region1 = image1.crop(fragment_box)
            region2 = image2.crop(fragment_box)
            diff = ImageChops.difference(region1.convert('RGB'), region2.convert('RGB'))
            diff_box = diff.getbbox()
            if diff_box:
                frag_area_size = (diff_box[2] - diff_box[0]) * (diff_box[3] - diff_box[1])
                fragments_area_size = fragments_area_size + frag_area_size
                result = True
                copied_region1 = copied_image1.crop(fragment_box)
                copied_region2 = copied_image2.crop(fragment_box)
                if save_img1_path != "":
                    __image_draw_rec_paste(copied_image1, copied_region1, fragment_box, diff.getbbox(),
                                           outline=Color.GREEN, fill=Color.IGNORE)
                if save_img2_path != "":
                    __image_draw_rec_paste(copied_image2, copied_region2, fragment_box, diff.getbbox(),
                                           outline=Color.GREEN, fill=Color.IGNORE)
    if mark_ignored_area:
        for remove_box in ignore_area_list:
            if save_img1_path != "":
                __image_mark_ignore_area(copied_image1, remove_box, outline=Color.YELLOW, fill=Color.YELLOW)
            if save_img2_path != "":
                __image_mark_ignore_area(copied_image2, remove_box, outline=Color.YELLOW, fill=Color.YELLOW)
    if save_img1_path != "":
        copied_image1.save(save_img1_path)
    if save_img2_path != "":
        copied_image2.save(save_img2_path)
    return fragments_area_size/(copied_image1.size[0] * copied_image1.size[1]) * 100


def __image_mark_ignore_area(img, box, outline=Color, fill=Color, width=4):
    remove_region = img.crop(box)
    __image_draw_x(remove_region, fill=fill, width=width)
    img.paste(remove_region, box)
    __image_draw_rec(img, box, outline=outline, fill=Color.IGNORE, width=width)


def __image_draw_x(img, fill=Color, width=3):
    draw = ImageDraw.Draw(img)
    shape = [(0, 0), (img.width, img.height)]
    draw.line(shape, fill=fill.value, width=width)
    shape = [(0, img.height), (img.width, 0)]
    draw.line(shape, fill=fill.value, width=width)


def __image_draw_rec_paste(img, region, fragment_box, draw_box, outline=Color, fill=Color, width=2):
    __image_draw_rec(region, draw_box, outline=outline, fill=fill, width=width)
    img.paste(region, fragment_box)


def __image_draw_rec(region, draw_box, outline=Color, fill=Color, width=2):
    if not isinstance(outline, Color):
        raise TypeError('outline must be an instance of Color Enum')
    if not isinstance(fill, Color):
        raise TypeError('fill must be an instance of Color Enum')
    draw = ImageDraw.Draw(region)
    draw.rectangle(draw_box, outline=outline.value, fill=fill.value, width=width)


if __name__ == '__main__':
    img1 = r"E:\1.png"
    img2 = r"E:\2.png"
    ignore_areas_list = [(0, 0, 1920, 500), (200, 200, 700, 500)]
    print(image_compare(img1, img2, fragmentation=6))
    # image_compare2(img1, img2)
