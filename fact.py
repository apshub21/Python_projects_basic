def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
    

if __name__=='__main__':
    number=int(input("enter number : "))
    fac=factorial(number)
    print(f"Factorial is {fac}")