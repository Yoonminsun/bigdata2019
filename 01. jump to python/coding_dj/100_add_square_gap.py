square=0
add=0
for num in range(1,101):
    square+=(num*num)
    add+=num

print((add*add)-square)