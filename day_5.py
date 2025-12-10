def compute(lst:list) -> tuple:
    sum_nums = 0
    for i in lst:
        sum_nums += i
    avg_num = sum_nums/len(lst)
    return sum_nums, avg_num

if __name__ == "__main__":
    nums = input("Enter a list of numbers separated by commas: ")
    nums = nums.split(",")
    nums = [float(num) for num in nums]
    print(f"The sum of the numbers of the provided list is {compute(nums)[0]}")
    print(f"The average of the numbers of the provided list is {compute(nums)[1]}")
