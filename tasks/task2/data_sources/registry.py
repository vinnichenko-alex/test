from io import StringIO

from .data_source import DataSource
from .csv_data_source import CsvDataSource
from .input_data_source import InputDataSource

registry = {'csv': CsvDataSource, 'input': InputDataSource}


def get_data_source(kind, file: StringIO | None | str = None) -> DataSource:
    if isinstance(file, str):
        with open(file) as file:
            return registry[kind](file)
    return registry[kind](file)

