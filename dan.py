import turtle as t
import random
X=1000
Y=800
t.setup(X,Y,0,0)
t.speed('fast')
t.ht()
t.pu()
t.goto(0,200)
t.st()
t.pd()
t.screensize(bg='#F23727')
t.pensize(32)
t.color("#B4240C")
t.right(120)
colorlist=['#BBFFFF','#FFDAB9','#FFFFF0','#FFF5EE','#F0FFF0','#E6E6FA','#FFFFFF','#2F4F4F','#778899','#6A5ACD','#4682B4',
           '#40E0D0','#5F9EA0','#2E8B57','#BC8F8F','#A0522D','#B22222','#FA8072','#FF8C00','#B03060','#DDA0DD','#D8BFD8',
           '#EEE9E9','#87CEFF']


t.forward(150)
for i in range(6):
    t.backward(100)
    t.left(95)
    t.forward(150)
    t.backward(100)
    t.right(95)
    t.forward(150)

def random_strokes():
    x=random.randint(-X/2+50,X/2+50)
    y=random.randint(-Y/2+50,Y/2+50)
    size=random.uniform(1,3)*0.8
    length=size*6
    n=random.randint(5,20)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.pensize(size)
    alpha=360/n
    c=random.choice(colorlist)
    t.pencolor(c)
    for i in range(n):
       
        t.forward(length)
        t.backward(length)
        t.left(alpha)


for i in range(33):
    t.speed('fastest')
    random_strokes()

#colors = ['red','yellow','green','blue','gray','purple','orange']

for m in range(12):  # 程序执行50次
    t.pencolor(random.choice(colorlist)) # 随机选择一种颜色
    size = random.randint(10,40)  # 10-40之间随机整数

    # 随机获得屏幕宽度和高度的值
    x = random.randrange(-t.window_width()//2,
                         t.window_width()//2)
    y = random.randrange(-t.window_height()//2,
                         t.window_height()//2)

    t.pu() # 抬笔
    t.setpos(x,y)  # 海龟从原点(0,0)移动到的位置
    t.pd() # 落笔
    for x in range(size):
        t.fd(x*2)
        t.lt(90)

t.textinput("新年提示语", "是否开启新的一年:")
t.up()
t.goto(-300,-250)
t.pencolor('yellow')
t.write('2021',True,align='left',font=("Arial", 144, "normal"))

def boom(x,y):
    t.undo()
    t.goto(-100,-250)
    t.pensize(2)
    t.pd()
    t.pencolor('#EEA2AD')
    for i in range(36):
        t.forward(150)
        t.backward(150)
        t.left(10)
    
t.onrelease(boom)
        
        
    
