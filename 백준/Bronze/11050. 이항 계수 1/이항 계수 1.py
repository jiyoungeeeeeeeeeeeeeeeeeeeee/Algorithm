#   (n k) = n! / (k! * (n-k)!) 

n , k = map(int,input().split())
n_factorial = 1
k_factorial = 1
n_k_factorial = 1

for N in range(1,n+1):
    n_factorial *= N

for K in range(1,k+1):
    k_factorial *= K

for n_k in range(1, n-k+1):
    n_k_factorial *= n_k

binomial_coefficient = n_factorial / (k_factorial * n_k_factorial)

print(int(binomial_coefficient))
