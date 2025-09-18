# conditional statement
num = 45
if num > 500:
    if num > 750:
        print("Num is gt 500 and 750")
    else:
        print("Num is only gt 500")
elif num > 100:
    if num > 250:
        print("Num id gt 100 and 250")
    else:
        print("Num is only gt 100")
else:
    print("lt 100")

# calculate fine
helmet = False
lic = False
ins = False
fine = 0

if not helmet:
    fine += 500
if not lic:
    fine += 2300
if not ins:
    fine += 410

# your logic

print(fine)