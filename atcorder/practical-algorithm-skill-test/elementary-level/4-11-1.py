from collections import Counter

# input
S = list(input())

# counter dictionary
c = Counter(S)

# extract most common alphabet
ans = c.most_common()[0][0]

# print answer
print(ans)
