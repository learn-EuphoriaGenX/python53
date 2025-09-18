# 1. loop initialization
# 2. loop condition check
# 3. loop updation

# range(1, 10) 1 2 3 4 5 6 7 8 9
# simple loop
start = 1
stop = 10
for i in range(start, stop + 1):
    # print(i, end=", ")
    pass

# nested loop
# line = 5
# for i in range(1, line+1):
#     print(f"{i} ->", end=" ")
#     for j in range(i, line+1):
#         print(f"{j}", end=" ")
#     print("")

n = int(input("Enter No of Lines: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print("")