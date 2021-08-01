class Person():
    def __init__(self) -> None:
        self.worklocation=""
        self.homeaddress=""

    def __str__(self) -> str:
        return "worklocation is {}\nhomeaddress is {}".format(self.worklocation, self.homeaddress)

    def __repr__(self) -> str:
        return "worklocation is {}\nhomeaddress is {}".format(self.worklocation, self.homeaddress)


class personBuilder:
    def __init__(self, p=Person()) -> None:
        self.person = p
    
    @property
    def works(self):
        return buildWork(self.person)

    @property
    def lives(self):
        return buildHome(self.person)


    def build(self):
        return self.person

    
class buildWork(personBuilder):

    def __init__(self, p=Person()) -> None:
        super().__init__(p)

    def updatework(self, location=str):
        self.person.worklocation = location
        return self


class buildHome(personBuilder):
    def __init__(self, p=Person()) -> None:
        super().__init__(p)
    
    def updatehome(self, location=str):
        self.person.homeaddress = location
        return self




if __name__=="__main__":
    p1 = personBuilder()
    p = p1.works.updatework("123 NY").lives.updatehome("789 NJ").build()
    print(p)
    p2 = personBuilder()
    p2.works.updatework("465 CT").lives.updatehome("098 VA").build()
    print(p2)
    