from io import StringIO
from statistics import mean, mode, median


class DataSource:
    def __init__(self, file: StringIO | None = None):
        self.file = file
        self.data = self.load_data()

    def load_data(self) -> list[int]:
        pass

    @property
    def mean(self):
        return mean(self.data)

    @property
    def mode(self):
        return mode(self.data)

    @property
    def median(self):
        return median(self.data)
