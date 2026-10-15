#inherarchical inheritance
class device:
    def power_on(self):
        print("device switched on")
class phone(device):
    def call(self):
        print("making a phone call")
class computer(device):
    def run_program(self):
        print("running a python program")
samsung=phone()
samsung.call()
samsung.power_on()
hp=computer()
hp.power_on()
hp.run_program()