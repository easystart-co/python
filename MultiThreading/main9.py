# 用队列进行多线程数据传递
import threading 
import time


def threading1():
    global numA,numB
    add_times = 100
    time.sleep(1)
    for  i in range(add_times):
        lockR.acquire()  #获取锁
        numA = numA+1
        thread_name = threading.current_thread().getName()
        print(thread_name+'-numA:'+str(numA))
        
        lockR.acquire()  #获取锁
        numB = numB+1
        thread_name = threading.current_thread().getName()
        print(thread_name+'-numB:'+str(numB))
        lockR.release()  #释放锁
        lockR.release()  #释放锁
def threading2():
    global numA,numB
    add_times = 100
    time.sleep(1)
    for  i in range(add_times):
        lockR.acquire()  #获取锁
        numA = numA+1
        thread_name = threading.current_thread().getName()
        print(thread_name+'-numA:'+str(numA))
        

        lockR.acquire()  #获取锁
        numB = numB+1
        thread_name = threading.current_thread().getName()
        print(thread_name+'-numB:'+str(numB))
        lockR.release()  #释放锁
        lockR.release()  #释放锁

if __name__ == "__main__":  # 主线程

  
    lockR = threading.RLock()  #递归锁
    numA = 0
    numB = 0
    th1 = threading.Thread(target=threading1,args=())   #子线程1 
    th2 = threading.Thread(target=threading2,args=())   #子线程2
    th1.setName('TH1')
    th2.setName('TH2')
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    # print(num)
    print('main threading end')
