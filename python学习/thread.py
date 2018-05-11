import time,random
import queue,threading #引入队列模块和线程模块

from main import work,set_fun

q = queue.Queue()#队列，全局作用，至少覆盖生产者和消费者函数
MAX = 50
MAX_T = 30
def Producer():  #生产者，将待处理XX提取或者生成，存到队列中
    for i in range(MAX):
        q.put(i)  #入队

def Consumer(): # 消费者，使用队列中的生产者所生产的东西
    while True:
        if not q.empty():       # 只要盘子里有包子，顾客就要吃。
            data = q.get()    #出队
            work()
        else:           # 盘子里没有包子
            print("---no task----")
            break;


@set_fun
def mywork():
    for i in range(MAX_T):
        c = threading.Thread(target=Consumer)
        c.start()

Producer()
mywork()

