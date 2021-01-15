def val_mayor(arr):
	if len(arr)<=2:
		return False
	output = []
	for i in arr:
		if i > arr[1]:
			output.append(i)
	print(len(output))
	return output

print(val_mayor([5,2,3,2,1,4])