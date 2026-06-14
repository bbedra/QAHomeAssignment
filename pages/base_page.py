from communication.ui.driver_wrapper import DriverWrapper


class BasePage:
    def __init__(self, driver_wrapper: DriverWrapper):
        self.driver = driver_wrapper
