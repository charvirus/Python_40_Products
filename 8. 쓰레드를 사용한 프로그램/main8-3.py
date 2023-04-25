import threading


def threadSum(name, value):
    for i in range(0, value):
        print(f"{name} : {i}")


t1 = threading.Thread(target=threadSum, args=('1번 쓰레드', 10))
t2 = threading.Thread(target=threadSum, args=('2번 쓰레드', 10))

t1.start()
t2.start()

print("Main Thread")