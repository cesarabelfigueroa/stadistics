from typing import List, Optional

class DataCapture:
    """
    A class for capturing and analyzing data within a given range of values.
    """

    def __init__(self):
        """
        Initializes a DataCapture instance with an empty data list.
        """
        self.data: List[int] = [0] * 1000  # Assuming all values are less than 1000

    def add(self, value: int) -> None:
        """
        Add a value to the data list.

        Args:
            value (int): The value to be added.

        Raises:
            ValueError: If the input value is not within the range [0, 999].
        """
        if 0 <= value < 1000:
            self.data[value] += 1
        else:
            raise ValueError("Input value must be within the range [0, 999].")

    def build_stats(self) -> 'DataCapture':
        """
        Build cumulative statistics for the data.

        Returns:
            DataCapture: The DataCapture instance for method chaining.
        """
        total_count = 0
        self.less_than: List[int] = [0] * 1000
        self.greater_than: List[int] = [0] * 1000

        for i in range(1000):
            self.less_than[i] = total_count
            total_count += self.data[i]

        total_count = 0
        for i in reversed(range(1000)):
            self.greater_than[i] = total_count
            total_count += self.data[i]

        return self

    def less(self, value: int) -> int:
        """
        Get the cumulative count of values less than or equal to the input value.

        Args:
            value (int): The input value.

        Returns:
            int: The cumulative count.
        """
        if 0 <= value < 1000:
            return self.less_than[value]
        else:
            return 0

    def greater(self, value: int) -> int:
        """
        Get the cumulative count of values greater than or equal to the input value.

        Args:
            value (int): The input value.

        Returns:
            int: The cumulative count.
        """
        if 0 <= value < 1000:
            return self.greater_than[value]
        else:
            return 0

    def between(self, start: int, end: int) -> int:
        """
        Get the count of values falling within the range [start, end].

        Args:
            start (int): The start of the range.
            end (int): The end of the range.

        Returns:
            int: The count of values within the specified range.
        """
        if 0 <= start <= end < 1000:
            return self.less_than[end + 1] - self.less_than[start]
        else:
            return 0
