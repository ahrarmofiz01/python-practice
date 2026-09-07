#def prime(n):
    #if n==0 or n==1:
     #   return False
    #for i in range(2, int(n**0.5) + 1):
       # if n%i==0:
          #  return False
    #return True
#print(prime(11))

    
def power_recursive(x, n):
    # Base case: any number to the power of 0 is 1
    if n == 0:
        return 1
        
    # Recursive step: calculate x^(n//2) once
    half = power_recursive(x, n // 2)
    
    # If n is even: x^n = x^(n//2) * x^(n//2)
    if n % 2 == 0:
        return half * half
    # If n is odd: x^n = x * x^(n//2) * x^(n//2)
    else:
        return x * half * half

print(power_recursive(2, 3))   # Output: 8
print(power_recursive(5, 4))   # Output: 625
