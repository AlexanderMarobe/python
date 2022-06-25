nums = [23,5,123,521]
swart = True



while swart:
	swart = False
	for i in range(len(nums)-1):
		if nums[i]>nums[i+1]:
			swart = True
			nums[i], nums[i+1]=nums[i+1], nums[i]


print(nums)
