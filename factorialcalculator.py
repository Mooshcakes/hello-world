#A program to calculate factorials(!)

factorial = 1
#input statement
x = int(input("Please enter a number: "))
#while loop
while x >= 1:
    factorial *= x
    x -= 1
#print statement
print(factorial)
