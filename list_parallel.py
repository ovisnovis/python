while True:
	y = 0
	print("Parallelrechner (Widerstände mit + addieren):")
	someList = input().split("+")
	for i in someList:
		x = float(i)
		y += 1/x
	print("Gesamtwiderstand:")
	print(1/y)
	pass
	