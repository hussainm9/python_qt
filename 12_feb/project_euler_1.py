# Problem 1
# If we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

# Find the sum of all the multiples of  or  below .

result = 0
max = 1000
multiple = 1
while multiple < max:
    if(multiple%3 ==0 or multiple%5 ==0):
        result = result + multiple
    multiple = multiple + 1

print(result,'result') #233168 result