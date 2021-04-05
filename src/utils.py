import threading

def set_interval(interval):
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop(): # executed in another thread
                while not stopped.wait(interval): # until stopped
                    function(*args, **kwargs)

            thread = threading.Thread(target=loop)
            thread.daemon = True # stop if the program exits
            thread.start()
            return stopped
        return wrapper
    return decorator
