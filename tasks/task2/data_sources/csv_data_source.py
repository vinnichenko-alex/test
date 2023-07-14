from itertools import chain

from .data_source import DataSource
import pandas as pd


class CsvDataSource(DataSource):

    def load_data(self) -> list[int]:
        return list(chain.from_iterable(pd.read_csv(self.file, header=None).values.tolist()))
