# class aaa:
#     def foo(method):
#         print "foo"
#         return method
#
#     @foo
#     def cc(self):
#         print "cc"


# from PIL import ImageChops, Image
# import math, operator
# def equal(im1, im2):
#     a = Image.open(im1)
#     b = Image.open(im2)
#     h = ImageChops.difference(b, a).getbbox()
#     #return ImageChops.difference(a, b).getbbox()
#     pass
# def c(im1, im2):
#     a = Image.open(im1)
#     b = Image.open(im2)
#     histogram1 = a.histogram()
#     histogram2 = b.histogram()
#     differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, \
#                                                      histogram1, histogram2))) / len(histogram1))
# def get_screenxy_from_bmp(main_bmp, son_bmp):
#     from PIL import Image
#     img_main = Image.open(main_bmp)
#     img_son = Image.open(son_bmp)
#     datas_a = list(img_main.getdata())
#     datas_b = list(img_son.getdata())
#     for i, item in enumerate(datas_a):
#         if datas_b[0] == item and datas_a[i + 1] == datas_b[1]:
#             yx = divmod(i, img_main.size[0])
#             main_start_pos = yx[1] + yx[0] * img_main.size[0]
#
#             match_test = True
#             for n in range(img_son.size[1]):
#                 main_pos = main_start_pos + n * img_main.size[0]
#                 son_pos = n * img_son.size[0]
#
#                 if datas_b[son_pos:son_pos + img_son.size[0]] != datas_a[main_pos:main_pos + img_son.size[0]]:
#                     match_test = False
#                     break
#             if match_test:
#                 return (yx[1], yx[0], img_son.size[0], img_son.size[1])
#     return False