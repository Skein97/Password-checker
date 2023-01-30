# RUNNING SUM
try:
    num1 = float(input('Type a number: '))
except ValueError:
    print('Please enter a number')

while 1:
    try:
        num2 = float(input('Type a number: '))
    except ValueError:
        print('Please enter a number')
    if num2 >= 0:
        sum_nums = num2 + num1
        print(f'Sum of numbers = {sum_nums}')
        num1 = sum_nums
    else:
        print(f'Final sum of numbers = {sum_nums}')
        print('Cannot calculate negative numbers! Finished!!')
        break

# NUMBER SORTER
# # Collect inputs
# num1 = input('Num 1: ')
# num2 = input('Num 2: ')
# num3 = input('Num 3: ')
# list_of_num = [num1, num2, num3]
# sorted_list = ['first', 'second', 'third']
# # Sort inputs (descending)
# for num in list_of_num:
#     if num is max(list_of_num):
#         sorted_list[0] = num
#     elif num is min(list_of_num):
#         sorted_list[2] = num
#     else:
#         sorted_list[1] = num
#
# # Write results
# print(sorted_list)

# SUM OF SQUARES
# list_of_inputs = []
# while 1:
#     try:
#         num = int(input('Input a number: '))
#         list_of_inputs.append(num)
#     except ValueError:
#         break
#
# print(list_of_inputs)
# squares = [i ** 2 for i  in list_of_inputs]
# print(squares)
# sum_of_inputs = sum(squares)
# print(sum_of_inputs)
