year = 2019
month = 3
day = 25
monthlist = [31,28,31,30,31,30,31,30,31,30,31,30]
sum = 0
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    monthlist[1] = 29
for i in range(month-1):
    sum += monthlist[i]
sum = sum + day
print(sum)