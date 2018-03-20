import requests

#Select all Scottish Government Areas publishing official stats
OrganisationList="ASD001,ASD002,ASD003,ASD004,ASD005,ASD006,ASD007,ASD008,ASD009,ASD010,ASD011,ASD012,ASD013,ASD014,ASD015,ASD016,ASD017,ASD018,ASD019"
URL = "https://procxed.scotxed.net/procxedwebservice/ProcXedDataReturn.asmx/GetForthcomingPublications?OrganisationIDList="+OrganisationList

response = requests.get(URL)
with open('forthcomingFeed.xml', 'wb') as file:
    file.write(response.content)

    