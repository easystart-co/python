import threading
import time

def threading1():
    global num  #main里面定义的变量都为全局变量，对全局变量进行写操作需要 进行声明
    while num > 0:
        print('th1:'+ str(num))
        num = num-1
    print('threading1 end')

def threading2():
    global num
    while num > 0:
        print('th2:'+ str(num))
        num = num-1
    print('threading2 end')


if __name__ == "__main__":  # 主线程
    
    num = 20
    
    th1 = threading.Thread(target=threading1,args=())   #子线程1 
    th2 = threading.Thread(target=threading2,args=())   #子线程2
    th1.start()
    th2.start()
    print('main threading end')
