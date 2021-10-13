import threading
import time
import queue

message_queue = queue.Queue()


def thread1():
    for i in range(4):
        message_queue.put(i*3)
        time.sleep(2)
    message_queue.put(-1)


def thread2():
    while True:
        value = message_queue.get()
        if value >= 0:
            print(f'Got the value {value} from Thread 1')
        else:
            break



def main():
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    t1.start()
    t2.start()

    print("Main thread is now here")
    # Main thread continues
    t1.join()
    t2.join()
    print('All threads are now done')

if __name__ == '__main__':
    main()
