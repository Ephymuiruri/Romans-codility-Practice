import timeit

def TimeChecker(A, B, C, D):
    from collections import Counter
    
    lowestTime = sorted([A, B, C, D])
    lowestTimeCounter = Counter(lowestTime)
    
    result = int(''.join(map(str, lowestTime)))
    times = 0
    
    for i in range(result, 2360):
        if i % 100 < 60:
            str_i = str(i).zfill(4)  # Ensure the string has 4 digits (e.g., "0023" instead of "23")
            str_i_counter = Counter(map(int, str_i))
            
            if str_i_counter == lowestTimeCounter:
                times += 1
                # Uncomment the following line to see detailed output
                #print(f"okay numbers {i}, times: {times}")
    
    return times

# Define the number of repetitions and setup code
number_of_repeats = 10
setup_code = """
from __main__ import TimeChecker
"""

# Measure the time
execution_time = timeit.timeit('TimeChecker(1,8,3,2)', setup=setup_code, number=number_of_repeats)

print(f"Average execution time over {number_of_repeats} runs: {execution_time / number_of_repeats} seconds")


print(TimeChecker(1,8,3,2))
print(TimeChecker(6, 2, 4, 7))