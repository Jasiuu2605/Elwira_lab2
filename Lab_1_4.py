from datetime import datetime
# ZADANIE 1


class Singleton:
    _instance = None
    creation_time = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.init_singleton()
        return cls._instance

    def init_singleton(self):
        self.creation_time = datetime.now()

    def get_creation_time(self):
        return self.creation_time


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
print("Data utworzenia singletona:", s1.get_creation_time())


# ZADANIE 2

class SingletonWithArgs:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SingletonWithArgs, cls).__new__(cls)
            cls._instance.init_singleton(*args, **kwargs)
        return cls._instance

    def init_singleton(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def get_args(self):
        return self.args

    def get_kwargs(self):
        return self.kwargs


s1 = SingletonWithArgs(42, name="John")
s2 = SingletonWithArgs(99, name="Alice")

print('Zadanie 2')
print(s1 is s2)

print("Argumenty s1:", s1.get_args())
print("Keyword arguments s1:", s1.get_kwargs())

print("Argumenty s2:", s2.get_args())
print("Keyword arguments s2:", s2.get_kwargs())


# ZADANIE 3


class LazySingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(LazySingleton, cls).__new__(cls)
            cls._instance.init_lazy_singleton()
        return cls._instance

    def init_lazy_singleton(self):
        if not hasattr(self, 'initialization'):
            self.creation_time = datetime.now()
            self.initialized = True

    def get_creation_time(self):
        return self.creation_time

# PRZYKŁAD


ls1 = LazySingleton()
ls1.init_lazy_singleton()

ls2 = LazySingleton()
ls2.init_lazy_singleton()

print('Zadanie 3')
print(ls1 is ls2)
print("Data utworzenia LazySingletona", ls1.get_creation_time())



