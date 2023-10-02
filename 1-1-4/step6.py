#   a114_divisible.py

# get two numbers from user
num = input("List a Number")
num2 = input("List another Number")

start_loop = 'num'
start_loop2 = 'num2'

rem = int(num) % int(num2)
# loop while the numbers are not divisible (the remainder is not 0)
while (rem != 0):
    print("Not divisible")
    num = input("List a Number")
    num2 = input("List another Number")
    rem = int(num) % int(num2)
if (rem == 0):
    print('Divisible')
# inform user of result

# gather user input again

# inform user of result