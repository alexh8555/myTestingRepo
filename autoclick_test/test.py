import pyautogui
import time
from playsound import playsound
import os
import cv2

pyautogui.PAUSE = 0.5
breakflag = False
files = os.listdir('image')
count = len(files)

target = 'db\\cv2_02700.png'
# gray_target = cv2.cvtColor(np.float32(target), cv2.COLOR_BGR2GRAY)

# digits = pyautogui.screenshot(region=(1423, 70, 70, 20))
# gray_target = cv2.cvtColor(np.float32(digits[0]), cv2.COLOR_BGR2GRAY)
# for i,g in enumerate(gray[0]):
# 	if g >= 140:
# 		print(g, i)

while True:
	sure = pyautogui.screenshot(region=(1435, 270, 167, 57))
	# digits = pyautogui.screenshot(region=(1423, 70, 70, 20))
	# gray = cv2.cvtColor(np.float32(digits), cv2.COLOR_BGR2GRAY)
	im1 = pyautogui.screenshot(region=(1371, 64, 324, 107))

	find_sure = pyautogui.locate('sure.png', sure)
	if find_sure is not None:
		im1.save('image\\' + str(count) + '.png', 'png')
		count += 1
		find_chara = pyautogui.locate(target, im1)
		print(str(find_chara) + '\n' + str(count))
		if find_chara is not None:
			print('gotcha!')
			playsound('rush.mp3')
			breakflag = True
		else:
			pyautogui.click(1769, 300, button='left')
			playsound('unconvinced.mp3')
			time.sleep(1)
			pyautogui.moveTo(x=1542, y=494)
			pyautogui.mouseDown(button='left')
			pyautogui.moveTo(x=1752, y=486, duration=0.2)
			pyautogui.moveTo(x=1649, y=690, duration=0.2)
			pyautogui.mouseUp(button='left')
	time.sleep(3)
	if breakflag:
		break
