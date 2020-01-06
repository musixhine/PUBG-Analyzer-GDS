import requests
import pubgapi

def matchlist(playername):
    #Get List of Matches
    matchlisturl = "{}{}/players?filter[playerNames]={}"
    matchlistrequest = requests.get(url = matchlisturl.format(apiurl, gameplatform, playername), headers = apiauth)
    print (matchlistrequest.json()) #work in progress. This needs to be parsed