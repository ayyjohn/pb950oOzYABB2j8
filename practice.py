class Ayyjohn:
    """practice class"""
    def __init__(self):
        self.ayy = "ayy"
        self.john = "john"
        self.name = self.ayy + self.john

    def grow(self):
        self.name = self.name.upper()


alec = Ayyjohn()
print(alec.ayy)
print(alec.name)
alec.grow()
print(alec.name)
