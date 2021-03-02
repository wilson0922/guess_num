import random
r = random.randint(1,100)
while True:
	num = input('請猜一個1~100的數字:')
	num = int(num)
	if num == r:
		print('終於猜對了')
		break
	elif num > r:
		print('你猜的比答案大')
		continue
	elif num < r:
		print('你猜的比答案小')
		continue
