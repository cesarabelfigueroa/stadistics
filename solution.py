class DataCapture:
    def __init__(self):
        self.data = [0] * 1000  # Assuming all values are less than 1000

    def add(self, value):
        if 0 <= value < 1000:
            self.data[value] += 1

    def build_stats(self):
        total_count = 0
        self.less_than = [0] * 1000
        self.greater_than = [0] * 1000

        for i in range(1000):
            self.less_than[i] = total_count
            total_count += self.data[i]

        total_count = 0
        for i in reversed(range(1000)):
            self.greater_than[i] = total_count
            total_count += self.data[i]

        return self

    def less(self, value):
        if 0 <= value < 1000:
            return self.less_than[value]
        return 0

    def greater(self, value):
        if 0 <= value < 1000:
            return self.greater_than[value]
        return 0

    def between(self, start, end):
        if 0 <= start <= end < 1000:
            return self.less_than[end + 1] - self.less_than[start]
        return 0