import xml.etree.ElementTree
import datetime

#Select how many days ahead to search for forthcoming publications.
daysAhead = 7

today = datetime.datetime.now().date()
todayUntil = today + datetime.timedelta(days=daysAhead)

#Import the feed that was downloaded
e = xml.etree.ElementTree.parse('forthcomingFeed.xml').getroot()

for all in e.findall('.//DataReturnComponent'):
    UID = all.find('.//UniqueId');

for each in e.findall('.//Series'):
    SeriesName = each.find('.//SeriesName');
    for edition in each.findall('.//Editions'):
        EditionName  = edition.find('.//EditionName');
        PublicationFullDate=edition.find('.//PublicationFullDate')
        Theme=edition.find('.//Theme')
        IsPublished=edition.find('.//IsPublished')
        
        #Only select publication editions that haven't been released and for which an exact date has been announced
        if IsPublished.text == "0" and PublicationFullDate.text != None:
            PublicationFullDateFormat = datetime.datetime.strptime(PublicationFullDate.text, "%Y-%m-%d").date()
            if PublicationFullDateFormat > today and PublicationFullDateFormat < todayUntil:
                print(SeriesName.text, " will be released on ", PublicationFullDateFormat)
            else:
                pass
        else:
            pass
            