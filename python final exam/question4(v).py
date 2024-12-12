class car():
    def __init__(self,brand,name,color):
        self.brand=brand
        self.name=name
        self.color=color
    def start_engine(self):
        print('the engine of the car has started')
car1=car('harrier','harrier1','white')
car1.start_engine()
        
        