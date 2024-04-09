from appliances import Appliance

class CanOpener(Appliance):

    def __init__(self, color):
        super(color).__init__(color)

    def open_can(self):
        print("Tuna smells bad")
