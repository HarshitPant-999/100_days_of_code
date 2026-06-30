import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper_function():
        start = time.perf_counter()
        result = function()
        end = time.perf_counter()
        diff = end - start
        print(f"Time is: {diff:.6f} seconds")
        return diff
    return wrapper_function

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i

@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_time = fast_function()
slow_time = slow_function()
diff = slow_time - fast_time
ratio = slow_time/fast_time 
print(diff)
print(ratio)



