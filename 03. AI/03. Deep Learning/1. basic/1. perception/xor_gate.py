# 목적: 퍼셉트론 가중치와 편향 도입
# coding: utf-8
# XOR 은 1차 방정식으로는 classifier를 그릴 수 없다.
# 따라서 아래와 같은 다층 퍼셉트론 방식 이용
from and_gate import AND
from or_gate import OR
from nand_gate import NAND

def XOR(x1,x2):      # 0110
    s1 = NAND(x1,x2) # 1110
    s2 = OR(x1,x2)   # 0111
    y = AND(s1,s2)   # 0001
    return y

if __name__ == '__main__':
    print('>> XOR gate')
    for xs in [(0,0),(1,0),(0,1),(1,1)]:
        y = XOR(xs[0],xs[1])
        print(str(xs)+'->'+str(y))