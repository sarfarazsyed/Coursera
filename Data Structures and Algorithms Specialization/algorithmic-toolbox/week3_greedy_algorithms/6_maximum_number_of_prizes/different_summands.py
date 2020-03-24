n = int(input())
if n == 1 or n == 2:
    print(1)
    print(n)
    quit()
W = n
prizes = []
for i in range(1, n):
    if W>2*i:
        prizes.append(i)
        W -= i
    else:
        prizes.append(W)
        break

print(len(prizes))
print(' '.join([str(i) for i in prizes]))