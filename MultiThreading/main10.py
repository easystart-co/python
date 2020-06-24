import threading
import time
def threading1(num):
    while num > 0:
        time.sleep(2)
        print('th1:'+ str(num))
        num = num-1
        if num ==5:
            event.set()
            pass
        if num ==2:
            event.wait()
    print('threading1 end')
def threading2(num):
    while num > 0:
        time.sleep(2)
        print('th2:'+ str(num))
        num = num-1
        if num ==9:
            event.wait()
            event.clear()
        
            
        
    print('threading2 end')


if __name__ == "__main__":  # 主线程
    event = threading.Event()
    num1 = 10
    num2 = 10
    th1 = threading.Thread(target=threading1,args=(num1,))   #子线程1 
    th2 = threading.Thread(target=threading2,args=(num2,))   #子线程2
    th1.start()
    th2.start()
    
    print('main threading end')
    

    # 主线程和子线程1、子线程2 并行执行