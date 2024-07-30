
# input_file = input("Enter file paths: ")
input_file = input("Введите путь к первому файлу: ")

nums = []
with open(input_file) as file:
    nums = file.readlines()
nums = [int(i) for i in nums] #Convert str to int

#Find the magic number:
min_diff = sum(nums) #Initialization of the difference variable
for curr_num in nums:
    nums_diff = [abs(num_i - curr_num) for num_i in nums] #Substract curr_num from each value in nums list
    curr_diff = sum(nums_diff)
    if curr_diff <= min_diff:
        min_diff = curr_diff
        magic_num = curr_num

#Calculate the number of steps:
steps = 0
for curr_num in nums:
    steps+=abs(curr_num-magic_num)

#Output steps to console:
print(steps)