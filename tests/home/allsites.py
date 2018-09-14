from indeed import Indeed
from dice import Dice
from monster import Monster
from careerbuilder import CareerBuilder
import glob
import sys

SITES = {
    "a": "All",
    "d": "Dice",
    "m": "Monster",
    "i": "Indeed",
    "c": "Careerbuiler"
}

class AllSites:

    def __init__(self):
        """
        return the path with file name: first file in list of files
        in the foler with resumes
        /Users/olegbushmelev/PycharmProjects/updateresume/files/
        """
        TRGT_FGR = '/Users/olegbushmelev/PycharmProjects/updateresume/files/*.pdf'
        self.files = glob.glob(TRGT_FGR)[0]


    def indeed(self):
        ff = Indeed(self.files)
        ff.update_resume()

    def dice(self):
        ff = Dice(self.files)
        ff.update_resume()

    def monster(self):
        ff = Monster(self.files)
        ff.update_resume()

    def careerbuiler(self):
        ff = CareerBuilder(self.files)
        ff.update_resume()

def select_site():
    """
    It takes no arg, ask in command line the letter from SITES
    :return: the letter from site that eqal web site for search.
    """
    print( "\nYour list of webs for submitting: \n" )

    # print the names
    for item in SITES.items():
        print("For submitting:", item[1], "chose:", item[0])
    res = str(input("Chose: a, d, m, i, d:")).lower()
    if res in SITES.keys():
        print('Chosen for processing:', SITES[res])
        return res
    else:
        print("Enter letter from the list:  a, d, m, i, c")
        select_site()

def main():

    # select the letter via interface dialog.
    site = select_site()
    res = AllSites() # Init. class object
    if site == 'c':
        res.careerbuiler()
    elif site == 'i':
        res.indeed()
    elif site == 'd':
        res.dice()
    elif site == 'm':
        res.monster()
    else:
        res.dice()
        res.monster()
        res.careerbuiler()
        res.indeed()


    # Fullfill in accordance with choice.




if __name__ == '__main__': sys.exit(main())
