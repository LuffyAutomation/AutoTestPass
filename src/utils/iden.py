#
# import os
# import platform
# import tempfile
# import shutil
# import math
# import operator
# from PIL import Image
# PATH = lambda p: os.path.abspath(p)
# TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")
# class Appium_Extend(object):
#     def __init__(self, driver):
#         self.driver = driver
#         def get_screenshot_by_element(self, element):
#             self.driver.get_screenshot_as_file(TEMP_FILE)
#             location = element.location
#             size = element.size
#             box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])
#             image = Image.open(TEMP_FILE)
#             newImage = image.crop(box)
#             newImage.save(TEMP_FILE)
#             return self
#         def get_screenshot_by_custom_size(self, start_x, start_y, end_x, end_y):
#             self.driver.get_screenshot_as_file(TEMP_FILE)
#             box = (start_x, start_y, end_x, end_y)
#             image = Image.open(TEMP_FILE)
#             newImage = image.crop(box)
#             newImage.save(TEMP_FILE)
#             return self
#         def write_to_file( self, dirPath, imageName, form = "png"):
#             if not os.path.isdir(dirPath):
#                 os.makedirs(dirPath)
#                 shutil.copyfile(TEMP_FILE, PATH(dirPath + "/" + imageName + "." + form))
#                 def load_image(self, image_path):
#                     if os.path.isfile(image_path):
#                         load = Image.open(image_path)
#                         return load
#                     else:
#                         raise Exception("%s is not exist" %image_path)
#                             #http://testerhome.com/topics/202
#         def same_as(self, load_image, percent):
#
#             image1 = Image.open(TEMP_FILE)
#             image2 = load_image
#             histogram1 = image1.histogram()
#             histogram2 = image2.histogram()
#             differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2,
#                                                              histogram1, histogram2)))/len(histogram1))
#             if differ <= percent:
#                 return True
#             else:
#                 return False