import time


class Timer:
    def __init__(self):
        self.timer = time.time()

    def print(self):
        print(f"{(time.time() - self.timer):.4f}s")
