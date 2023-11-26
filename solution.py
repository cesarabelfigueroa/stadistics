class DataCapture:
    def __init__(self):
        self.data = []
        self.count_less = {}
        self.count_greater = {}
    
    def add(self, value):
        self.data.append(value)

        if value not in self.count_less:
            self.count_less[value] = 0
        self.count_less[value] += 1

        if value not in self.count_greater:
            self.count_greater[value] = 0
        self.count_greater[value] += 1
    
    def less(self, value):
        if value not in self.count_less:
            return 0
        return self.count_less[value]

    def greater(self, value):
        if value not in self.count_greater:
            return 0
        return self.count_greater[value]

    def between(self, lower, upper):
        count = 0
        for value in self.data:
            if lower <= value <= upper:
                count += 1
        return count
