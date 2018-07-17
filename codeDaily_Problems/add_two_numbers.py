# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?




def add_two_nums(nums, target):
	d = {}
	for i in range(len(nums)):
		if nums[i] in d:
			d[nums[i]] += 1
		else:
			d[nums[i]] = 1
	for i in range(len(nums)):
		if target-nums[i] in d.keys():
			if target-nums[i] == nums[i]:
				if d[nums[i]] > 1:
					return True
			else:
				return True
	return False	



def main():
	x = input("Enter the list ")
	t = input("Enter the target ")
	print add_two_nums(list(x), t)
	 
	


if __name__ == '__main__':
	main()