
#Then, write a program that takes two integer numbers from the keyboard and calculates their arithmetic mean.

# takes two numbers from keyboard
n1 = int(input('input first number: '))
n2 = int(input('imput second number: '))

# define an anonymous function
mean = lambda x,y: int(x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean of {mean(n1,n2)}")