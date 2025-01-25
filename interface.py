from abc import ABC, abstractmethod

class Interface(ABC):
    def __init__(self):
        pass
   
    @abstractmethod
    def do_something(self):
        pass

class ConcreteInterfaceA(Interface):
    def __init__(self):
        super().__init__()

    def do_something(self):
        print('Concrete Implementation A')

class ConcreteInterfaceB(Interface):
    def __init__(self):
        super().__init__()

    def do_something(self):
        print('Concrete Implementation B')

class InterfaceUser:

    def use_interface(self, interface: Interface):
        interface.do_something()


# APP Code
interface_user = InterfaceUser()
concrete_interface_a = ConcreteInterfaceA()
interface_user.use_interface(concrete_interface_a)

concrete_interface_b = ConcreteInterfaceB()
interface_user.use_interface(concrete_interface_b)
