import time


def bar():
    for i in range(10):
        print("Tick")
        time.sleep(1)


bar()
