'''
########################################################################################

                        Automatic Selenium Command Generator

    Version:            Version 1.0  
    Author:             Mingrui Yang
    Functionality:      html => this script => list of commands
                        This script returns the possible tag attribute "id" of the 
                        input fields on the career webpage that will later be used in 
                        the auto_fill script
    Matching Mechanism:  
                        (ver 1.0)  : regex / other matching 
    Issue Remaining
        1. Cannot fill in tag that can only be activated through clicking other tags

########################################################################################
'''

# Imports 
from bs4 import BeautifulSoup 
import re 

# Main Scripts 
class AutoExtract(object):  
    def __init__(self): 
        '''
        Later, the path of index2.html should not be absolute, 
        instead, should be replaced by the output of another 
        script that gets the page html dynamically and accordingly.
        '''
        self.file = open('index2.html','rb') 
        self.html = self.file.read() 
        self.bs = BeautifulSoup(self.html, "html.parser") 
        # There should be a better way of using a dictionary containing all
        # possible attribute names. Perhaps using ML? 
        self.item_dict = {'firstname' : ['firstname', 'firstName', 'givenname'], 
                          'lastname' :  ['lastname', 'firstName', 'familyname'], 
                          'phone' : ['phone','tel'], 
                          'email' : ['mail', 'email'], 
                          } # 'resume' : ['file', 'upload', 'resume']
        self.app_fields = dict() 

    def filterMethod(self, tag): 
        criteria_1 = tag.name == "input" 
        criteria_2 = False 
        for item in self.item_dict: 
            if tag.has_attr("id"): 
                for word in self.item_dict[item]: 
                    if re.search(word, tag["id"]) != None: 
                        criteria_2 = True
                        self.app_fields[item] = tag["id"]    
        return criteria_1 and criteria_2

    def printExtracted(self): 
        print(f"The fields extracted:")
        for elem in self.app_fields: 
            print('\t', elem, '\t', self.app_fields[elem])

    def extract(self):    
        self.inputList = self.bs.find_all(self.filterMethod)
        for i in range(len(self.inputList)): 
            self.inputList[i] = self.inputList[i]["id"]
        self.printExtracted() # for testing 
        return self.app_fields 
        




