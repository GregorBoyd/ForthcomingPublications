import xml.etree.ElementTree
import datetime
import twitter
import requests

#Select all Scottish Government Areas publishing official stats
OrganisationList="ASD001,ASD002,ASD003,ASD004,ASD005,ASD006,ASD007,ASD008,ASD009,ASD010,ASD011,ASD012,ASD013,ASD014,ASD015,ASD016,ASD017,ASD018,ASD019"
URL = "https://procxed.scotxed.net/procxedwebservice/ProcXedDataReturn.asmx/GetForthcomingPublications?OrganisationIDList="+OrganisationList

response = requests.get(URL)
with open('forthcomingFeed.xml', 'wb') as file:
    file.write(response.content)
    
# set up twitter credentials
api = twitter.Api(consumer_key='XXX',
                  consumer_secret='XXX',
                  access_token_key='XXX',
                  access_token_secret='XXX')

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
            if PublicationFullDateFormat >= today and PublicationFullDateFormat < todayUntil:
                Days = (PublicationFullDateFormat - today).days
                TweetSeriesName=SeriesName.text
                TweetDate=PublicationFullDate.text
                if Days == 0:
                    tweetText=(TweetSeriesName+ " released today")
                elif Days == 1:
                    tweetText=(TweetSeriesName+ " will be released tomorrow")
                else:    
                    tweetText=(TweetSeriesName+ " will be released in "+ str(Days) + " days on "+ TweetDate)
                #print(tweetText)
                api.PostUpdate(tweetText)
            else:
                pass
        else:
            pass
            
