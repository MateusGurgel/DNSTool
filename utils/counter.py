class Counter:
    def __init__(self, current, max):
        self.current = current
        self.max = max

    def count(self, i=1):
        self.current += i

    def get(self):
        return f"{self.current}/{self.max}"

    def show(self):
        print(f"{self.current}/{self.max}")
