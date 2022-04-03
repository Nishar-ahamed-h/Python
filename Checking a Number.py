def NumberCheck(N):        
    if N > 0:   
        print("Number given by you is Positive")   
    elif N < 0:   
        print("Number given by you is Negative")   
    else:   
        print("Number given by you is zero")  
N = float(input("Enter a number as input value: "))   
NumberCheck(N)  