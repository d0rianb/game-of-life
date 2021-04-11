import time

class Stats:
    @staticmethod
    def frame_start():
        Stats.start_time = time.time()

    @staticmethod
    def frame_end():
        if not hasattr(Stats, 'start_time'): raise Exception('Stats.frame_start() has not been called before Stats.frame_end()')
        Stats.frame_time = time.time() - Stats.start_time

    @staticmethod
    def get_frame_time():
        if not hasattr(Stats, 'frame_time'): raise Exception('Stats.frame_end() has not been called before Stats.get_frame_time()')
        return Stats.frame_time

    @staticmethod
    def get_frame_rate():
        return 1000 / Stats.frame_time

