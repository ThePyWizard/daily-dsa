#Adding factorials

n = int(input("Enter the limit of series: "))
sum = 0
for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum += fact
print(sum)
