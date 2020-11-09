import math

domains = [[-7,-4],[4,7]]

def function(x):
    return 2 - math.sqrt(math.asin((abs(x)-4)/3))

sum_val = 0
sum_domain = 0
for domain in domains:
    for i in range(domain[0],domain[1]+1):
        sum_val += function(i)
        sum_domain += i
print(sum_val)
print(sum_domain)
