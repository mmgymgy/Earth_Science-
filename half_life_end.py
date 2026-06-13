import matplotlib.pyplot as plt

x = []
y = []

e = ["우라늄-235","칼륨-40","우라늄-238","토륨-232","루테튬-176","레늄-187","루비듐-87"]
t = [7.04, 12.51, 44.68, 140.5, 378, 412, 492]

def half_life(amount, time):
    max_time = time * 10
    samples = 1000           

    for i in range(samples + 1):
        current_time = max_time * i / samples
        x.append(current_time)
        y.append(amount * (0.5 ** (current_time / time)))

element = input("원소의(모원소) 이름을 입력하세요: ").strip()

for i in e:
    if element == i:
        amount = int(input("원소의(모원소) 양을 입력하세요: ").strip())
        
        if amount <= 0:
            print("양은 양수여야 합니다.")
            exit()
            
        time = t[e.index(i)]
        print(time)
        half_life(amount, time)
        break
else:
    print("해당 원소는 없습니다.")
    exit()
plt.rc('font', family='Malgun Gothic')
plt.plot(x, y)
plt.xticks([round(time * i, 2) for i in range(11)])
plt.ylim(0, amount)
plt.title(f"{element}의 반감기 그래프")
plt.ylabel("모\n원\n소\n양",rotation=0, labelpad=25)
plt.xlabel("                                                                                                      억년")
plt.grid()
plt.show()
