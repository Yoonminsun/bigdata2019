import random

def calc_bmi(h,w):
    bmi = w/(h/100)**2
    if bmi <18.5: return 'thin'
    elif bmi < 25 : return 'normal'
    else: return 'fat'

fp = open('bmi.csv','w',encoding='utf-8',newline='')
fp.write('height,weight,label\r\n')

for num in range(30000):
    h = random.randint(120,200)
    w = random.randint(35,80)
    label = calc_bmi(h,w)
    fp.write('{0},{1},{2}\r\n'.format(h,w,label))
fp.close()