from os import listdir
from os.path import isfile, join
import chardet
import codecs
import csv
import sys
# read in the EBSCONet file for actual holdings
# then go through Serials Solutions file to activate only those that are our holdings based on EBSCONet file
    # activate here means to accurately indicate our holdings by re-creating the Serials Solutions file with Status either Active or Not Tracked
    # activate also means for our holdings, create Custom URL.  
#  
class Holding:
    ezprefix = 'ezp.bentley.edu'
    def __init__(self, title, identifier, content_type, status, default_dates, title_id, publisher, display_public_note, display_location_note, default_url, custom_date_from=None 
        , custom_date_to=None, pub_date=None, edition=None, public_note=None
        , location_note=None, custom_url=None):
        self.title = title
        self.identifier = identifier
        self.type = content_type
        self.status = status
        self.default_dates = default_dates
        self.custom_date_from = custom_date_from
        self.custome_date_to = custom_date_to
        self.title_id = title_id
        self.pub_date = pub_date
        self.edition = edition
        self.publisher = publisher
        self.public_note = public_note
        self.display_public_note = display_public_note
        self.location_note = location_note
        self.display_public_note = display_location_note
        self.default_url = default_url
        self.custom_url = custom_url
        


collection = sys.argv[1]
path = "./"+collection
download = path + "/Download"
holdings = sys.argv[2]

holdings_issn = []

if holdings == "EBSCONet":
    print("got ebsco")
    path = "./"+collection
    EBSCONet_holdings = path + "/EBSCONet"
    for f in listdir(EBSCONet_holdings):
        print ("ebsconet file...")
        print(f)
        my_file = join(EBSCONet_holdings, f)
        print(my_file)
        with open(my_file, 'r') as contents:
            rows = csv.reader(contents, delimiter="\t", quotechar='"')
            for cnt, line in enumerate(rows):
                if cnt > 0:
                    holdings_issn.append(line[1])


knowledgebase_issn = []
kb_rows = []
for f in listdir(download):
    print("file...")
    print(f)
    my_file = join(download, f)
    with codecs.open(my_file, 'r', 'utf-16') as contents:
        rows = csv.reader(contents, delimiter="\t", quotechar='"')        
        # readlines creates a list of all lines
        for cnt, line in enumerate(rows):
            if cnt >= 15:
                kb_rows.append(line)
                knowledgebase_issn.append(line[1])


print(kb_rows[0])

# match loop
count = 0
for i in holdings_issn:
    if i in knowledgebase_issn:
        row_number = knowledgebase_issn.index(i)
        # print(kb_rows[row_number])


            

       
   