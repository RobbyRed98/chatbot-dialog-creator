class Counter:

    def __init__(self, name: str, initial_count: int):
        self.name = name
        self.count = initial_count

    def inc(self, by: int = 1) -> int:
        self.count = self.count + by
        return self.count

    def get(self):
        return self.count
