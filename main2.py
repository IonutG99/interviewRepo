# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizzbuzz
# 16

def fizzBuzz(n,k):
    if n>k:
        return
    if n%15==0:
        print("fizzbuzz")
    elif n%5==0:
        print("buzz")
    elif n%3==0:
        print("fizz")
    else:
        print(n)
    fizzBuzz(n+1,k)
    
k=16
fizzBuzz(1,k)