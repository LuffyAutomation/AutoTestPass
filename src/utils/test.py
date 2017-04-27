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

#import xmlrunner

# def run_suite_output_xml_report(suite, **args):
#     '''
#     :param suite: 已组装好的测试套
#     :param args: 可设置的参数及说明如下：
#          TEST_OUTPUT_DESCRIPTIONS: 输出描述
#          TEST_OUTPUT_DIR：测试报告输出路径，默认为根目录
#          TEST_OUTPUT_FILE_NAME：测试报告输入文件名，默认为hsplatform_ut_testreport.xml
#     :return:
#     '''
#     descriptions = args.get('TEST_OUTPUT_DESCRIPTIONS', True)
#     output_dir = args.get('TEST_OUTPUT_DESCRIPTIONS', 'c:\\')
#     single_file = args.get('TEST_OUTPUT_FILE_NAME', 'hsplatform_ut_testreport.xml')
#     kwargs = dict(verbosity=1, descriptions=descriptions, failfast=False)
#     if single_file is not None:
#         file_path = os.path.join(output_dir, single_file)
#         with open(file_path, 'wb') as xml:
#             return xmlrunner.XMLTestRunner(output=xml, **kwargs).run(suite)
#     else :
#         return xmlrunner.XMLTestRunner(output=output_dir, **kwargs).run(suite)
# @abstractmethod
# def getAndroidSDK(self, uuid=None):
#     pass
#
# @abstractmethod
# def getBuildInMobileLanguage(self, uuid=None):
#     pass
#
# @abstractmethod
# def getProjectName(self):
#     pass
#
# @abstractmethod
# def getProjectPath(self):
#     pass
#
# @abstractmethod
# def updateCurrentElementStatus(self, element_name):
#     pass
#
# @abstractmethod
# def setCurrentElementName(self, element_name):
#     pass
#
# @abstractmethod
# def getCurrentElementName(self):
#     pass
#
# @abstractmethod
# def setCurrentPage(self, page):
#     pass
#
# @abstractmethod
# def getCurrentPage(self):
#     pass
#
# @abstractmethod
# def setCurrentElementObject(self, element):
#     pass
#
# @abstractmethod
# def getCurrentElementObject(self):
#     pass