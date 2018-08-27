from indeed import Indeed
from dice import Dice
from monster import Monster
from careerbuilder import CareerBuilder
import glob

class AllWebs:

    def found_file(self):
        """
        return the path with file name: first file in list of files
        in the foler with resumes
        /Users/olegbushmelev/PycharmProjects/updateresume/files/
        """
        target_fdr = '/Users/olegbushmelev/PycharmProjects/updateresume/files/*.pdf'
        return glob.glob(target_fdr)[0]

    def indeed(self):
        ff = Indeed(self.found_file())
        ff.update_resume()

    def dice(self):
        ff = Dice(self.found_file())
        ff.update_resume()

    def monster(self):
        ff = Monster(self.found_file())
        ff.update_resume()

    def careerbuiler(self):
        ff = CareerBuilder(self.found_file())
        ff.update_resume()

ff = AllWebs()

# ff.indeed()
# ff.dice()
# ff.monster()
ff.careerbuiler()
