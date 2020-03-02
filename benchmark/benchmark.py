# Simple system benchmarking tool.

# Modules.
import time

# Functions.
def header(title):
    # Create a nice header.
    # params: str(title)
    # return: str(header)

    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header

def divide(a, b):
    # Simple division of two numbers.
    # params: int(a), int(b)
    # return: float(result)

    result = a / b

    return result


# Print header.
print(header("Simple System Benchmark"))

# User input.

# Difficulty level of benchmark.
while True:
    try:
        difficulty = int(input("Difficulty level (>=1): ").strip())
        break
    except ValueError:
        print("Please enter a positive integer number!")
        continue

# Sleep time and testing cycles.
sleep_time = 10
test_count = 3

# Initialize test number.
test_num = 1

# Benchmark starts.
print("\n{}K BENCHMARK in progress...".format(difficulty))

# Start the cycle of tests.
while test_num <= test_count:
    # Set divident.
    divident = 1

    # Get starting time.
    start_time = time.time()

    # Start main loop based on difficulty.
    while divident <= difficulty * 1000:
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
    print("Test %d of 3: %.2f s" % (test_num, exec_time))

    # Increase test number.
    test_num += 1

    # Sleep between testing cycles (skip the last one).
    if test_num < 4:
        time.sleep(sleep_time)
