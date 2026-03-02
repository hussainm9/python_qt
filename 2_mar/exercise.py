# I want to ask user to enter some value what builtin function can be used
number =    input("enter a number")
print(number)
print(type(number))
# I have a variable which is string has a value '10', i want to convert that into int which builtin function can help me
int_num = int(number)
print(int_num)
print(type(int_num))
# Change the prime number python ocde to ask the value from user
start = 2
is_prime = True
while start < int_num:
    if int_num % start == 0:
        is_prime == False
    start = start + 1
if int_num > 0 and  is_prime == True :
    print(f'${int_num} is prime number')
else:
    print(f'${int_num} is not prime number')
