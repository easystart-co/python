# 用队列进行多线程数据传递
import threading
import time
import queue

def threading1(num):
    
    while num > 0:
        tx_str = 'th1:'+ str(num)
        tx_quene.put(tx_str)
        # rx_quene.empty()
        if ~rx_quene.empty():
            rx_str = rx_quene.get()
            print(rx_str)
        num = num-1
    print('threading1 end')

def threading2(num):
    
    while num > 0:
        if ~tx_quene.empty():
            rx_str = tx_quene.get()
            print(rx_str)

        tx_str = 'th2:'+ str(num)
        rx_quene.put(tx_str)

        num = num-1
    print('threading2 end')


if __name__ == "__main__":  # 主线程
    
    num = 20
    tx_quene = queue.Queue()
    rx_quene = queue.Queue()
    th1 = threading.Thread(target=threading1,args=(num,))   #子线程1 
    th2 = threading.Thread(target=threading2,args=(num,))   #子线程2
    th1.start()
    th2.start()
    print('main threading end')
