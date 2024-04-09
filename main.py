class A:
    def a(self):
        print(__class__)
        print(self.__class__)
class B(A): (...)


B().a()