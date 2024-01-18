import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        self.value = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance


def worker():
    obj = Singleton.get_instance()
    print(obj.value)


threads = []
for _ in range(5):
    thread = threading.Thread(target=worker)
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()




