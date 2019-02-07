#coding: cp949

'''
#TFF=T
is_cash = 1
is_card = 0
is_coin = 0
#FTF=T
is_cash = 0
is_card = 1
is_coin = 0
#FFT=T
is_cash = 0
is_card = 0
is_coin = 1
#TTF=T
is_cash = 1
is_card = 1
is_coin = 0
#TFT=T
is_cash = 1
is_card = 0
is_coin = 1
#FTT=T
is_cash = 0
is_card = 1
is_coin = 1
#FFF=F
is_cash = 0
is_card = 0
is_coin = 0
#TTT=T
is_cash = 1
is_card = 1
is_coin = 1
'''


if is_cash or is_card or is_coin:
    print("택시를 타고 가세요")
else:
    print("걸어가세요")
