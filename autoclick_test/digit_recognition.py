def depoint(image):  # 像素 判断一个点周围情况 4，8邻域
	"""
	降噪
	:param image:
	:return:
	"""
	pixdata = image.load()
	print(pixdata)
	w, h = image.size
	for y in range(1, h - 1):
		for x in range(1, w - 1):
			count = 0
			if pixdata[x, y - 1] > 245:
				count += 1
			if pixdata[x, y + 1] > 245:
				count += 1
			if pixdata[x - 1, y] > 245:
				count += 1
			if pixdata[x + 1, y] > 245:
				count += 1
			if count > 3:
				pixdata[x, y] = 255
	return image


def binaring(image, threshold=160):
	"""
	对传入的图像进行灰度，二值化处理
	:param image:
	:param threshold:
	:return:
	"""
	image = image.convert('L')
	# image.show()
	pixdata = image.load()
	# print(pixdata)
	w, h = image.size
	for y in range(h):
		for x in range(w):
			# print(pixdata[x,y])
			pix_l.append(pixdata[x, y])
			if pixdata[x, y] < threshold:
				pixdata[x, y] = 0
			else:
				pixdata[x, y] = 255
	return image


from pytesser3 import image_to_string
# from pytesser3 import image_file_to_string
from PIL import Image

tesseract_exe_name = 'c:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

image = Image.open('db\\qwq.png')
pix_l = []
# image.show()
# pix_l_set = sorted(list(set(pix_l)))
# print(pix_l_set[:len(pix_l_set)//2])  # 求平均数的值
image2 = binaring(image)  # 二值化
image3 = depoint(image2)  # 降噪
# image3.show()
# 识别文字
print('code: ', image_to_string(image3))
