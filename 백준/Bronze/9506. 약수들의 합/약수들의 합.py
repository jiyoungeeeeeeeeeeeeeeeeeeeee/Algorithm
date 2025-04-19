while True:
    n = int(input())

    if n == -1:
        break

    perfect = []

    for i in range(1,n+1):
        if n%i == 0:
            perfect.append(i)
    # print(perfect)

    perfect = perfect[:-1]
    total = sum(perfect)
    # print(total)
    if total == n:
        print(f"{n} = {' + '.join(map(str, perfect))}")    
    else:
        print(f"{n} is NOT perfect.")