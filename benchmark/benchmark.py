"""
Simple system benchmarking tool.
"""

# Modules.
import time

# Functions.
def divide(a, b):
    return a / b

# Set benchmark difficulty.
difficulty = 5000
diff_short = round(difficulty / 1000)

# Set number of tests.
test_count = 5

# Initialize test number.
test_num = 1

# Benchmark starts.
print("{}K benchmark in progress... Please wait.".format(diff_short))

# Start the cycle of tests.
while test_num <= test_count:
    # Set divident.
    divident = 1

    # Get starting time.
    start_time = time.time()

    # Start main loop based on difficulty.
    while divident <= difficulty:
        # Set divisor.
        divisor = 1

        while divisor <= divident:
            divide(divident, divisor)

            # Increase divisor.
            divisor += 1

        # Increase divident.
        divident += 1

    # Calculate and round execution time.
    exec_time = round(time.time() - start_time, 2)

    # Print result.
    print("Result #{}: {} s".format(test_num, exec_time))

    # Increase test number.
    test_num += 1

    # Sleep between testing cycles (skip the last one).
    if test_num < 4:
        time.sleep(5)
