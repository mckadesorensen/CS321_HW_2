import time


class Status:
    def __init__(self):
        self.l1_cache = 0
        self.l2_cache = 0
        self.ram = 0
        self.tbl_miss = 0
        self.start_time = time.time()
        self.finish_time = self.calculate_time()

    def calculate_time(self):
        end_time = time.time()
        return end_time - self.start_time

    def update_status(self, _time):
        if .00001 <= _time < .0000999999:
            print(f"Time {_time}")
            self.l2_cache += 1
        elif _time < .0000099999:
            print(f"Time {_time}")
            self.l1_cache += 1
        elif .00599999 > _time >= .0001:
            print(f"Time {_time}")
            self.ram += 1
        elif _time >= .006:
            print(f"Time {_time}")
            self.tbl_miss += 1

    def print_stats(self):
        print(f"L1 hits: {self.l1_cache}")
        print(f"L2 hits: {self.l2_cache}")
        print(f"Ram hits: {self.ram}")
        print(f"TBLMiss hits: {self.tbl_miss}")
        print(f"Total time: {self.finish_time}")
        print(f"Total: {self.l1_cache + self.l2_cache + self.ram + self.tbl_miss}")