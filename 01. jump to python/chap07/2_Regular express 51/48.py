import re

def is_decimal(num):
    p=re.compile('^\d+.\d{,2}$') # 소수점 아래 최대 2자리
    m = p.search(num)
    return m

print(is_decimal('123.11'))
print(is_decimal('123.1'))
print(is_decimal('123'))
print(is_decimal('0.21'))

print(is_decimal('123.1214'))
print(is_decimal('3.124587'))
print(is_decimal('e666.86'))

