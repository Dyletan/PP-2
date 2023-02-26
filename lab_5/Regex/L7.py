import re
snake = "snake_case_askdkj"
capital = snake.upper()
camel = ""
i = 0
while(i!=len(snake)):
    if(snake[i]=="_"):
        camel += snake[i] + capital[i+1]
        i += 2
    else:
        camel += snake[i]
        i += 1
camel = re.sub("_", "", camel)
print(camel)

# for 
# x = re.sub(r"_\w", [1].upper(), str)
# x = str.split("_")
# print(x)
# z = x[0]
# for i in range(1, len(x)):
#     z += x[i][0].upper()
#     z += x[i][1:]
# print(z)