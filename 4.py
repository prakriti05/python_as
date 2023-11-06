input_str = input("Enter a sequence of comma-separated numbers: ")

numbers_list = input_str.split(',')

numbers_tuple = tuple(numbers_list)

print(numbers_list)
print(numbers_tuple)