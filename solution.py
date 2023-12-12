from typing import List

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
            ValueError: If the input value is not an integer or is not within the range [0, 999].
        """
        if not isinstance(value, int) or not (0 <= value < 1000):
            raise ValueError("Input value must be an integer within the range [0, 999].")
        self.data[value] += 1

    def build_stats(self):
        """
        Calculate cumulative statistics (less_than and greater_than) for the given data.

        Returns:
            self: The current instance with updated statistics.
        """
        total_count_forward = 0
        total_count_backward = 0
        self.less_than = [0] * 1000
        self.greater_than = [0] * 1000

        for i in range(1000):
            self.less_than[i] = total_count_forward
            self.greater_than[999 - i] = total_count_backward

            total_count_forward += self.data[i]
            total_count_backward += self.data[999 - i]

        return self

    def less(self, value: int) -> int:
        """
        Get the cumulative count of values less than or equal to the input value.

        Args:
            value (int): The input value.

        Returns:
            int: The cumulative count.

        Raises:
            ValueError: If the input value is not an integer or is not within the range [0, 999].
        """
        if not isinstance(value, int) or not (0 <= value < 1000):
            raise ValueError("Input value must be an integer within the range [0, 999].")
        return self.less_than[value]

    def greater(self, value: int) -> int:
        """
        Get the cumulative count of values greater than or equal to the input value.

        Args:
            value (int): The input value.

        Returns:
            int: The cumulative count.

        Raises:
            ValueError: If the input value is not an integer or is not within the range [0, 999].
        """
        if not isinstance(value, int) or not (0 <= value < 1000):
            raise ValueError("Input value must be an integer within the range [0, 999].")
        return self.greater_than[value]

    def between(self, start: int, end: int) -> int:
        """
        Get the count of values falling within the range [start, end].

        Args:
            start (int): The start of the range.
            end (int): The end of the range.

        Returns:
            int: The count of values within the specified range.

        Raises:
            ValueError: If the input values are not integers or are not within the range [0, 999].
        """
        if (
            not isinstance(start, int) or
            not isinstance(end, int) or
            not (0 <= start <= end < 1000)
        ):
            raise ValueError("Input values must be integers within the range [0, 999].")
        return self.less_than[end + 1] - self.less_than[start]
