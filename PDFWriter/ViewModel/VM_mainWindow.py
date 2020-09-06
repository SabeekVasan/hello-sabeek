import subprocess
import pandas as pd
import xml.etree.ElementTree as ET
from pip._internal import self_outdated_check
class VM_maindwindow():
    def __init__(self):
        # List of names, widgets are stored in a dictionary by these keys.
        self.emp_df = pd.read_json('data/empData.json')
        self.widget_names = self.emp_df['Name'].to_numpy()
        
        #loading config file in XML 
        tree = ET.parse('config.xml')
        xml_data = tree.getroot()
        self.template = xml_data[0].text        
    
    def getNames(self):
        return self.widget_names
    
    
    def getRecords(self,empname):
        i = 0
        for rec in self.emp_df['Name']:
            if empname == rec:
                return self.emp_df.loc[i]
            i = i + 1   
    def process4Report(self, sDay,sMonth,sYear,eDay, eMonth,eYear):
        print(self.template)
        var = "/hoem/sabeek/Practice/Perl"
        retcode = subprocess.Popen(["/usr/bin/perl", "hello.pl",var])
        if retcode == 0:
            print("Passed!")
        else:
            print("Failed!")