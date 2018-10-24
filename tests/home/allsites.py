from indeed import Indeed
from dice import Dice
from monster import Monster
from careerbuilder import CareerBuilder
import glob
import sys
import json


class AllSites:

    def __init__(self):
        """
        return the path with file name: first file in list of files
        in the foler with resumes
        /Users/olegbushmelev/PycharmProjects/updateresume/files/
        """
        # Read json file and get SITES, TRGT_FGR target files folder;
        # credentials: crdls;
        # path self.crdls with self.files to modules of pages.
        self.data = json.load(open("../../files/data.json"))

        folder_t = self.data["TRGT_FGR"]
        self.files = glob.glob( folder_t )[0]
        self.crednls = self.data["crednls"]
        self.args = [ self.files, self.crednls]

    def indeed(self):
        ff = Indeed(*self.args)
        ff.update_resume()

    def dice(self):
        ff = Dice(*self.args)
        ff.update_resume()

    def monster(self):
        ff = Monster(*self.args)
        ff.update_resume()

    def careerbuiler(self):
        ff = CareerBuilder(*self.args)
        ff.update_resume()

    def getSites(self):
        return self.data["sites"]

def select_site(obj):
    """
    It takes object of class as arg,
    ask in command line the letter from res.getSites()/self.sites/SITES
    :return: the letter from site that eqal web site for search.
    """
    print( "\nYour list of webs for submitting: \n" )

    # print the names
    for item in obj.getSites().items():
        print("For submitting:", item[1], "chose:", item[0])

    # Create string of choice.
    string_choice = ""

    for item in obj.getSites():
        string_choice += (item+", ")
    string_choice = "Chose: " + string_choice[:-2] + ": "

    res = str(input(string_choice))
    sites = obj.getSites()

    if res in sites.keys():
        print('Chosen for processing:', sites[res])
        return res
    else:
        print("Enter letter from the list:  a, d, m, c, i")
        select_site()

def main():

    # select the letter via interface dialog.

    res = AllSites() # Init. class object

    site = select_site(res)

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
