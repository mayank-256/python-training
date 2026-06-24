import time
def execution_time(func):
    """tell the execution time"""
    def wrapper():
        start=time.time()
        # print(start)
        # print(func())
        result = func()
        end=time.time()
        # print(end)
        exec_time = end-start
        print(f"function calculate executed in {round(exec_time,5)}s")
        return result
    return wrapper


@execution_time
def hello():
    for i in range(10):
        print(i)
    return "hello"

hello()
