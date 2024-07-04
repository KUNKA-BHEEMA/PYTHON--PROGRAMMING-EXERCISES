#mean.py
#program to find mean, median, and mode in a list
import math
mylist=[7,1,2,2,3,4,7,1,9,8,12,67,23,99,5,7, 7, 6,1,22, 7,3,7,9,10,12,90, 7]

print('Original list...')
print(mylist)
mylist.sort()
print('Sorted list...')
print(mylist)

def find_MeanMedianMode():
	mylist_count=len(mylist)
	mean=0
	median=0
	mode=0
	sum=0
	for i in mylist:
		sum=sum+i
	mean=round(sum/mylist_count, 2)

	median_index=int(math.floor(mylist_count/2))
	if median_index%2==1:
		median=mylist[median_index]
	else:
		median=(mylist[median_index]+mylist[median_index+1])/2
	mode_value=mylist.count(mylist[0])
	for i in range(1, mylist_count):
		m=mylist.count(mylist[i])
		if m>=mode_value:
			mode=mylist[i]	
			mode_value=mylist.count(mylist[i])
	print('Mean: '+str(mean))
	print('Median: '+str(median))
	print('Mode: '+str(mode))

find_MeanMedianMode()