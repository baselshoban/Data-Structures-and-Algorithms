def bubble_sort(list):
	loopCount = len(list)-1
	for i in range(loopCount):
		for j in range(loopCount -i):
			if list[j] > list[j+1]:
				holder = list[j]
				list[j] = list[j+1]
				list[j+1] = holder
	return list