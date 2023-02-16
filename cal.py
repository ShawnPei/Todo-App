sum = 0

for i in range(2,10):
    for j in range(2,i):
        if(i % j ==0):
            break
        else:
            print(i)
            sum+=i
print(sum)

# def sumOfGP(a, r, n):
#     sum = 0
#     i = 0
#     while i < n:
#         sum = sum + a
#         a = a * r
#         i = i + 1
#
#     return sum
#
#
# # driver function
#
# a = 1  # first term
# r = -3 # common ratio
# n = 5  # number of terms
#
# print("%.5f" % sumOfGP(a, r, n)),


