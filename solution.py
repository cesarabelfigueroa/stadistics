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