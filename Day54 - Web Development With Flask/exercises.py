import time
#
# current_time = time.time()
# print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function):
    def time_checker():
        current_time = time.time()
        function()
        time_after = time.time()
        time_past = time_after - current_time
        f_name = function.__name__
        print(f"{f_name} run time is {time_past} seconds")
        return time_past
    return time_checker

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


time_diff = slow_function() - fast_function()
print(time_diff)
