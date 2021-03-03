import random
r = random.randint(1,100)
count = 0
while True:
	count += 1

	num = input('請猜一個1~100的數字:')
	num = int(num)
	if num == r:
		print('終於猜對了')
		break
	elif num > r:
		print('你猜的比答案大')
	elif num < r:
		print('你猜的比答案小')
	print('你猜了第', count, '次')

