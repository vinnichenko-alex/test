import statistics as stats

# Have 3 types how we can get a data
# U writes yourself in code
data_source_1 = [1, 2, 3, 4, 5]
# U writes yourself in console
# data_source_2 = list(int(value) for value in input('Write nums with space-separate ').split())
# data_source_2 = [int(value) for value in input('Write nums with separate " " ').split()]
# Read file txt
with open('calculate.txt', encoding='utf-8') as file:
    data_source_3 = [int(value) for value in file.read().split(',')]

# data_source_3 = list(int(value) for value in data_source_3.split())
print(data_source_3)

# for i in range(1, 4):
#     data = "data_source_" + str(i)
#     print(f'Find characteristics for Data:\n{data}\nMean - {stats.mean(data)},'
#           f' median - {stats.median(data)}, mode - {stats.mode(data)}')