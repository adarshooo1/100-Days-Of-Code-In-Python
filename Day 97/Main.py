import threading # import threading module for multi-threading support
import time # import time module to calculate time intervals
from concurrent.futures import ThreadPoolExecutor

# function that sleeps for the specified number of seconds
def fun(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds) # sleep for the specified number of seconds
    return seconds

# normal sequential execution
time1 = time.perf_counter() # record the current time
fun(4)    # call fun with a sleep time of 4 seconds
fun(3)    # call fun with a sleep time of 3 seconds
fun(10)   # call fun with a sleep time of 1 0 seconds
print("ENDED")
time2 = time.perf_counter() # record the time after all three calls to fun have finished

print(time2 - time1) # calculate and print the total execution time

def main():

    # multi-threaded execution
    time3 = time.perf_counter() # record the current time

    # create three threads, each running the fun function with a different sleep time
    t1 = threading.Thread(target=fun ,args=[4])
    t2 = threading.Thread(target=fun ,args=[10])
    t3 = threading.Thread(target=fun ,args=[2])

    # start the threads running
    t1.start()
    t2.start()
    t3.start()

    # wait for each thread to finish before continuing
    t1.join()
    t2.join()
    t3.join()

    time4 = time.perf_counter() # record the time after all threads have finished

    print(time4 - time3) # calculate and print the total execution time of the threaded block

def poolingdemo():
    with ThreadPoolExecutor() as executor:

         # Way 1
        future1 = executor.submit(fun, 3)
        future2 = executor.submit(fun, 2)
        future3 = executor.submit(fun, 5)

        print(future1.result())
        print(future2.result())
        print(future3.result())

        # Way 2
        url_list = [2, 4, 3, 1, 5, 6, 7]
        for result in executor.map(fun, url_list):
            print(result)


poolingdemo()







