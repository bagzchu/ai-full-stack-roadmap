import time

class SimpleTimer:

    def __enter__(self):
        self.start = time.perf_counter()
        print("Stopwatch Started!!")
        return self

    def __exit__(self, exec_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        total_time = self.end - self.start
        print("Stopwatch Stopped!!")


with SimpleTimer():
    print("The computer is running heavy task")
    time.sleep(2)