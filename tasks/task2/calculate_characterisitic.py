import statistics as stats

# Have 3 types how we can get a data
# U writes yourself in code
data_source_1 = [1, 2, 3, 4, 5]
# U writes yourself in console
data_source_2 = list(int(value) for value in input('Write nums with space-separate ').split())
# data_source_2 = [int(value) for value in input('Write nums with separate " " ').split()]

print(f'Find characteristics for Data:\n{data_source_1}\nMean - {stats.mean(data_source_1)},'
      f' median - {stats.median(data_source_1)}, mode - {stats.mode(data_source_1)}')
print(f'Find characteristics for Data:\n{data_source_2}\nMean - {stats.mean(data_source_2)},'
      f' median - {stats.median(data_source_2)}, mode - {stats.mode(data_source_2)}')
