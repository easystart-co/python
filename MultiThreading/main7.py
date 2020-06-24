# 用队列进行多线程数据传递
import threading 
import time


def threading1():
    global num
    add_times = 100
    time.sleep(1)
    for  i in range(add_times):
        lock.acquire()  #获取锁
        num = num+1
        thread_name = threading.current_thread().getName()
        print(thread_name+':'+str(num))
        lock.release()  #释放锁


if __name__ == "__main__":  # 主线程

    lock = threading.Lock() 
    
    num = 0
    th1 = threading.Thread(target=threading1,args=())   #子线程1 
    th2 = threading.Thread(target=threading1,args=())   #子线程2
    th1.setName('TH1')
    th2.setName('TH2')
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    # print(num)
    print('main threading end')
