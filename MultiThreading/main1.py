import threading
import time
def threading1(num):
    while num > 0:
        print('th1:'+ str(num))
        num = num-1
    print('threading1 end')
def threading2(num1):
    while num1 > 0:
        print('th2:'+ str(num1))
        num1 = num1-1
    print('threading2 end')


if __name__ == "__main__":  # 主线程
    # 多线程
    # start_time = time.perf_counter()
    num = 10
    th1 = threading.Thread(target=threading1,args=(num,))   #子线程1 
    th2 = threading.Thread(target=threading2,args=(num,))   #子线程2
    th1.start()
    th2.start()
    # end_time = time.perf_counter()
    # use_time = end_time-start_time
    # print(use_time)
    print('main threading end')
    

    # 主线程和子线程1、子线程2 并行执行