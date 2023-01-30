# RUNNING SUM
while 1:
    try:
        num = float(input('Type a  Positive number to start: '))
        if num >= 0:
            num = num
            break
        else:
            print('Cannot calculate negative numbers!')
            raise ValueError
    except ValueError:
        print('Please enter a positive number to start')

while 1:
    try:
        num1 = float(input('Type a number: '))
        if num1 >= 0:
            num = num + num1
            print(f'Sum of numbers = {num}')

        else:
            print(f'Final sum of numbers = {num}')
            print('Cannot calculate negative numbers! Finished!!')
            break
    except ValueError:
        print('Please enter a number')
    # except NameError:
    #     print(f'Final sum of numbers = {num}')
    #     break


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
