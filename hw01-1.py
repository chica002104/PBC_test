full_t = int(input())
full_p = int(input())
half_t = int(input())
half_p = int(input())
budget = int(input())

total = full_t * full_p + half_t * half_p
change = budget - total

if change < 0:
    print(-1)
else:
    print("$" + str(change))
