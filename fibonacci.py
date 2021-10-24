def Fibonacci(num):
        if(num == 0):
            return 0
        elif(num == 1):
            return 1
        else:
            return (fibonacci(num-2) + fibonacci(num-1))
      num = int(input("enter the range of numbers-"))
            for n in range(0, num):
            print(Fibonacciseries(n))
