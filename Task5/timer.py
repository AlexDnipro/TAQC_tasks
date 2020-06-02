# timer.py

import time

class Timer:
    def __init__(self, quiz_part_name: str, file_name: str):
        """
        Constructor initializes timer start time, delta time, specifies quiz part name (quiz or its section)
        and file name to record time reports.
        """
        self._start_time = None
        self.delta_time = None
        self.quiz_part_name = quiz_part_name # It can be either whole "quiz" or "section name"
        self.file_name = file_name

    def start(self):
        """Start a new timer"""
        self.delta_time = None
        self._start_time = time.perf_counter()


    def stop(self):
        """Stop the timer, and report the delta time"""
        self.delta_time = round(time.perf_counter() - self._start_time)
        self._start_time = None
    
    def update_timer_file(self):
        """
        This function will open the time report file and record the measured delta time
        for how long it took to complete all quiz and its individual sections.
        """
        timer_file = open(self.file_name, 'a+')
        try:
            timer_file.write(f'{self.quiz_part_name} was performed in {self.delta_time} seconds\n')
        except IOError as IO:
            print(repr(IO))
        finally:
            timer_file.close()
    
    def __enter__(self):
        """Start a new timer as a context manager"""
        self.start()
        return self

    def __exit__(self, *exception_info):
        """Stop the context manager timer and report measured delta time"""
        self.stop()
        self.update_timer_file()
