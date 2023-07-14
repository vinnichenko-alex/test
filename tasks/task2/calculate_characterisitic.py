from data_sources import get_data_source

client = input('write ')
file = input('write')
data_source = get_data_source(client, file)
print(data_source.data)
print(data_source.mean)


