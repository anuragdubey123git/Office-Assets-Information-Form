class Candle:
    def __init__(self,color,scent):
        self.color=color
        self.scent=scent

    def burn(self):
        return f"The {self.color} candle with {self.scent} is burning."

candle1= Candle("red", "lavender")
candle2= Candle("Green","vanilla")
print(candle1.burn())
print(candle2.burn())