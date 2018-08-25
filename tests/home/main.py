from indeed import Indeed
from dice import Dice
from monster import Monster
from careerbuilder import CareerBuilder

class AllWebs:

    def indeed(self):
        ff = Indeed()
        ff.update_resume()

    def dice(self):
        ff = Dice()
        ff.update_resume()

    def monster(self):
        ff = Monster()
        ff.update_resume()

    def careerbuiler(self):
        ff = CareerBuilder()
        ff.update_resume()

ff = AllWebs()

ff.indeed()
ff.dice()
ff.monster()
ff.careerbuiler()
