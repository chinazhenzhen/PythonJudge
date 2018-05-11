import time,random
import queue,threading,pymysql #引入队列模块和线程模块

from work import  work

q = queue.Queue()#队列，全局作用，至少覆盖生产者和消费者函数

MAX_THREAD = 30
dblock = threading.Lock()

def Producer():  #生产者，将待处理XX提取或者生成，存到队列中
    while True:
        time.sleep(0.5)
        print("3")
        q.join()
        print("1")
        db = pymysql.connect(host="127.0.0.1", user="root", password="12345678", db="oj", port=3306)
        cursor = db.cursor()
        dblock.acquire()
        cursor.execute("select * from problem_status  WHERE result = 0")
        dblock.release()
        print("2")
                #db.commit()

        db.commit()
        cursor.close()
        db.close()

        for i in cursor.fetchall():
            q.put(i)  #入队



def Consumer(): # 消费者，使用队列中的生产者所生产的东西
    while True:
        if not q.empty():       # 只要盘子里有包子，顾客就要吃。
            data = q.get()    #出队

            work(data)

            q.task_done()


        else:           # 盘子里没有包子
            time.sleep(0.5)

p = threading.Thread(target=Producer) #设置生产线程
#c2 = threading.Thread(target=Consumer,args=('C',)) #设置消费线程
p.start() #开启线程

for i in range(0,MAX_THREAD):
    onethread = threading.Thread(target=Consumer)
    onethread.start()
#c2.start() #开启线程
#Producer()