string = input().strip()
sub_string = input().strip()
count = 0
n = -1

for i in range(0, len(string) - len(sub_string)):
    index = string.find(sub_string, i)
    if index != -1 and index > n:
        n = index
        count += 1
print(count)

# Another interesting solution
# A = input()
# # B = input()
# # LA = len(A)
# # LB = len(B)
# # cnt = 0
# # for i in range(LA-LB+1):
# #     if A[i:i+LB] == B:
# #         cnt += 1
# # print(cnt)