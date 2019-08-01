# 73  -> 75
# 71 -> 75
# 

value = 73
value2 = 71

print(value % 10)

if value % 10 < 5 :
    value = value - value % 10 + 5
else :
    value = value - value % 10 + 10

print(value)