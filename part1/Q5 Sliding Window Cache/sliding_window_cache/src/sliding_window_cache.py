class SlidingWindowException(Exception):
    pass

class SlidingWindowCache:
    def __init__(self, capacity : int):
        self.capacity = capacity
        self.buff = [None for _ in range(capacity)]
        self.pointer = 0
        self.size = 0

    def add(self, key: any, value: any):
        if self.size < self.capacity:
            self.buff[self.pointer] = (key, value)
            self.pointer = (self.pointer + 1) % self.capacity
            self.size += 1
        else:
            self.buff[self.pointer] = (key, value)
            self.pointer = (self.pointer + 1) % self.capacity

    def get_recent_windows(self, n:int, reverse:bool = False):

        # GRACEFUL error handling
        if n < 0:
            raise SlidingWindowException("requested no of windows should be positive")
        if n > self.capacity:
            raise SlidingWindowException("request exceeds cache size.")
        if reverse:
            return  (self.buff[(self.pointer - i - 1) % self.capacity] for i in reversed(range(n)))
        else:
            return (self.buff[(self.pointer - i - 1) % self.capacity] for i in range(n))


