
class Mobiles():
    def __init__(self,comp,ram,rom,camera,battery):
        self.comp=comp
        self.ram=ram
        self.rom=rom
        self.camera=camera
        self.battery=battery
    def display(self):
        print("brand:",self.comp)
        print("ram",self.ram)
        print("rom:",self.rom)
        print("camera:",self.camera)
        print("battery:",self.battery)
obj=Mobiles("apple","8GB","266GB","64MP","4500MAH")
obj.display()

