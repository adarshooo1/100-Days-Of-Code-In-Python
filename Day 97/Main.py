import threading # import threading module for multi-threading support
import time # import time module to calculate time intervals

# function that sleeps for the specified number of seconds
def fun(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds) # sleep for the specified number of seconds

# normal sequential execution
tim1 = time.perf_counter() # record the current time
fun(4)    # call fun with a sleep time of 4 seconds
fun(3)    # call fun with a sleep time of 3 seconds
fun(10)   # call fun with a sleep time of 10 seconds
print("ENDED")
tim2 = time.perf_counter() # record the time after all three calls to fun have finished

print(tim2 - tim1) # calculate and print the total execution time

# multi-threaded execution
tim3 = time.perf_counter() # record the current time

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

tim4 = time.perf_counter() # record the time after all threads have finished

print(tim4 - tim3) # calculate and print the total execution time of the threaded block
