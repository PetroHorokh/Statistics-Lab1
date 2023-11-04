# Libraries
import funcs
import const
import configuration

# Config
configuration.config()

# Task1
print('Task1')
random_v = funcs.random_variable()
print(random_v)

# Task2
print('Task2')
print("M[x_i] = M[(12 * M[r] - 6) * 3.6 - 4] = M[(12 * (1 / 2) - 6) * 3.6 - 4] = M[-4] = -4\nD[x_i] = 3.6^2 = 12.96")

# Task3
print('Task3')
test_data = funcs.data_collector(12)

for i in range(len(test_data)):
    print(test_data[i])

# Task4
print('Task4')
data = funcs.data_collector(const.n)
print(funcs.interval_diagram(data))

# Task5
print('Task5')
funcs.histogram(data)

# Task6
print('Task6')
funcs.valuation(data)

# Task7
print('Task7')
funcs.approximation(data)
