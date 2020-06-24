import threading
import time
def threading1(input_num):
    current_thread_name = threading.current_thread().getName()
    print(current_thread_name+'  start')
    while input_num > 0:
        print(current_thread_name+'——'+ str(input_num))
        input_num = input_num-1
    print(current_thread_name+'  end')


if __name__ == "__main__":  # 主线程
   
    num = 3
    thread_num = 3
    for i in range(thread_num):
        th1 = threading.Thread(target=threading1,args=(num,))   #子线程
        th1.setName('线程：'+str(i))
        th1.start()

        th1.join()  #主线程和子线程同步

    print('main threading end')
    