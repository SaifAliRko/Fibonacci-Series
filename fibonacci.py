from functools import lru_cache   # importing built in function too store the cache ie to speed up our program
#to store values of previous functions in the new one

@lru_cache(maxsize = 1000)  #lru Least Recently Used cache with a max size of 1000 values
def fibonacci(n):

    # Check if the input is positive

    if type(n) != int and type(n) < n:

        raise TypeError("n must be a positive number")


    #compute the Nth term

    if n == 1:
        return 1

    elif n==2 :
        return 1

    elif n>2 :
        return fibonacci(n-1) + fibonacci(n-2)


x = int(input("Enter a number  "))

print(fibonacci(x))
