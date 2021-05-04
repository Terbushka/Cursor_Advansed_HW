"""
4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
and create an HPLaptop class by using your interface.
"""
from abc import abstractmethod, ABC


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError

class Laptop(Laptop):
    def __init__(self, model, screen_diag, keyboard_type, touchpad_type, webcam_type, ports_type, dynamics_type):
        self.model = model
        self.screen_diag = screen_diag
        self.keyboard_type = keyboard_type
        self.touchpad_type = touchpad_type
        self.webcam_type = webcam_type
        self.ports_type = ports_type
        self.dynamics_type = dynamics_type

    def screen(self):
        print(f'Screen: {self.screen_diag}')

    def keyboard(self):
        print(f'Keyboard language: {self.keyboard_type}')

    def touchpad(self):
        print(f'Touchpad: {self.touchpad_type}')

    def webcam(self):
        print(f'Webcam: {self.webcam_type}')

    def ports(self):
        print(f'Ports: {self.ports_type}')

    def dynamics(self):
        print(f'Dynamics: {self.dynamics_type}')


laptop = Laptop("MacBook Pro 2019 ", "13,3(2560 x 1600)", "English, Russian", "Yes", "Yes",
                  "Two Thunderbolt 4 ports", "Yes")

laptop.screen()
laptop.keyboard()
laptop.touchpad()
laptop.webcam()
laptop.ports()
laptop.dynamics()