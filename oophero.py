



from random import Random


class person:
    def __init__(self,job,sociallife,fortitude: int): 
        self.job=job
        self.social_life=sociallife
        self.food_needness=True
        self.fortitude=fortitude
    def savingThrow(self,difficulty):
        SavingThrow=Random.randint(1,21)+self.fortitude-self.__unluckyDay()
        return SavingThrow>difficulty

    def __getattribute__(self, __name: str): return __name.upper()
    def __setattr__(self, __name: str, __value): self.__name=__value
    def __delattr__(self, __name: str): del self.__name

    def __unluckyDay(): return Random.randint(1,3)
class superhero(person):
    def __init__(self, job, sociallife, fortitude: int, superpower):
        self.Personality=person(job, sociallife, fortitude)
        self.superpower=superpower
    def usingPower(self, how:str):
        return 'using '+self.superpower+' for '+how

batman=superhero('billioner', 'Bruce Wayne', 5,'money')
batman.__unluckyDay()


