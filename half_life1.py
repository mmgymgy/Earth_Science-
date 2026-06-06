import matplotlib.pyplot as plt
import math

x = []
y = []

e = ["우라늄-235","칼륨-40","우라늄-238 ","토륨-232","루테튬-176","레늄-187","루비듐-87"]
t = [ 7.04,12.51,44.68, 140.5, 378,412,492]

def half_life(element, amount,time):
    for i in range(0, 10000):
        x.append(i)
        y.append(amount*(0.5** (i/time)))




element = input("원소의(모원소) 이름을 입력하세요: ")
for i in e:
    if element == i:
        amount = int(input("원소의(모원소) 양을 입력하세요: "))
        time = t[e.index(i)]
        half_life(element, amount,time)
        break
    else:
        print("해당 원소는 없습니다.")
        break:
#붕괴가 활발하여 지질학적 연대 측정에 쓰이는 핵심 동위원소 7개

plt.plot(x,y)
plt.xlim(0, time*4)    
plt.ylim(0, amount)  
plt.grid()
plt.show()
