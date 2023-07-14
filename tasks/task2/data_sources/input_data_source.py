from .data_source import DataSource


class InputDataSource(DataSource):
    def load_data(self) -> list[int]:
        return [int(number) for number in input('Write numbs').split(',')]

