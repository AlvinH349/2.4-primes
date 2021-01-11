def primes(n):
 for i in range(1,n+1):
    d = 0
    for j in range(2, i):
        # If i is divisible by j
        if (i % j) == 0:
            d += 1
    
    if d > 0:
      continue
    else:
      print(i, "is a prime number")

num = int(input("What is your n?"))
primes(num)
 
   