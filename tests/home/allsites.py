from tests.home.indeed import Indeed
from tests.home.dice import Dice
from tests.home.monster import Monster
from tests.home.careerbuilder import CareerBuilder
import sys
import glob
import json


class AllSites(Dice, Monster, CareerBuilder, Indeed):

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

        self.resume_file = glob.glob( folder_t )[0]
        self.credentials = self.data["credentials"]


        # Reffernce to classes for inheritance.
        Dice.__init__(self, self.resume_file, self.credentials)
        Monster.__init__(self, self.resume_file, self.credentials)
        CareerBuilder.__init__(self, self.resume_file, self.credentials)
        Indeed.__init__(self, self.resume_file, self.credentials)


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
        print("You may enter only letter from the list:  a, d, m, c, i")
        select_site(obj)

def main():
    # select the letter via interface dialog.

    res = AllSites() # Init. class object

    site = select_site(res)

    if site == 'c':
        res.update_careerb()
    elif site == 'i':
        res.update_indeed()
    elif site == 'd':
        res.update_dice()
    elif site == 'm':
        res.update_monster()
    else:
        res.update_dice()
        res.update_monster()
        res.update_careerb()
        res.update_indeed()


    # Fullfill in accordance with choice.




if __name__ == '__main__': sys.exit(main())
