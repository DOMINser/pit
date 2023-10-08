#С помощью анонимной функции извлеките из списка числа, делимые на 15.
nums = [45, 55, 60, 37, 100, 105, 220]
o=lambda x: x%15
for i in range(len(nums)):
    if o(nums[i])==0:
        print(nums[i])
