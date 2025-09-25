import math
import time
import matplotlib.pyplot as plt

def my_function(n):
    total_sum = 0
    j = 5
    while j < math.log2(n):
        k = 5
        while k < n:
            total_sum += j * k
            k = k ** 1.5
        j = 1.2 * j
    return total_sum

n_values = [10**10, 10**20, 10**30, 10**40, 10**50, 10**60, 10**70, 10**80, 10**90, 10**100] 

experimental_times = []
for n in n_values:
    time_taken = 0
    start_time = time.perf_counter_ns()
    my_function(n)
    end_time = time.perf_counter_ns()
    time_taken = end_time - start_time
    experimental_times.append(time_taken)

# raw theoretical values
theoretical_raw = [(math.log2(math.log2(n)))**2 for n in n_values]

# normalization
mid_index = len(n_values) // 2
c = experimental_times[mid_index] / theoretical_raw[mid_index]
theoretical_scaled = [c * val for val in theoretical_raw]

print(f"Scaling constant c = {c:.6f}")
print(experimental_times)
print(theoretical_raw)
print(theoretical_scaled)

# graph
plt.figure(figsize=(8,5))
plt.plot(n_values, experimental_times, 'o-', label="Experimental Time")
plt.plot(n_values, theoretical_scaled, 's-', label="Theoretical Time (scaled)")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("n (log scale)")
plt.ylabel("Time (ns, log scale)")
plt.title("Experimental vs Theoretical Complexity")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()
