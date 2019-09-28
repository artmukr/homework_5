nums = [75, 55, 66, 44, 98, 54, 67]
summ = sum(nums)


while summ > 200:
    del nums[-1]
    summ = sum(nums)
print(nums)
