#import the requests library
import pubgapi
import requests

#PUBG API
#apiurl = "https://api.pubg.com/shards"
#apikey = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmN2Y1MWVlMC0wNTdkLTAxMzgtNThiOS0xNTY5OGE1NTgzYjciLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTc2ODYzNzI4LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Im11c2l4aGluZS1nbWFpIn0.-K6O_A78jShq3le6F_ih0-CxpvGjhY8tlyGchfBp51Y"

#API Auth Parameters
#apiauth = {'Authorization': apikey,
#           'Accept': "application/vnd.api+json"}

#Platform
gameplatform = "/steam"

#Game Mode
gamemode = "/squad-fpp"
#Player Name
playername = "Big-V-Brother"
playerid = "account.e3d597fe3f8c44d2968c421e2f930115"
                 
##Get List of Matches, now it's a function in "matchlist.py"

#matchlisturl = "{}{}/players?filter[playerNames]={}"
#matchlistrequest = requests.get(url = matchlisturl.format(apiurl, gameplatform, playername), headers = apiauth)
#matchlist = matchlistrequest.json() #work in progress. This needs to be parsed
#matchid = "/df900f46-9a05-4e90-a668-91ff3e554b0d"

#Get Match Data
matchdataurl = "{}{}/matches{}"
matchdatarequest = requests.get(url = matchdataurl.format(apiurl, gameplatform, matchid), headers = apiauth)

##Get List of Seasons
#seasonlistURL = "{}{}{}"
#seasonlistrequest = requests.get(url = seasonlistURL.format(apiurl, gameplatform, "/seasons"), headers = apiauth)
seasonid = "/division.bro.official.pc-2018-05"

#Get Season Stats
seasonstatsurl = "{}{}/seasons{}/gameMode{}/players?filter[playerIds]={}"
seasonstatsrequest = requests.get(url = seasonstatsurl.format(apiurl, gameplatform, seasonid, gamemode, playerid), headers = apiauth)
seasonstats = seasonstatsrequest.json() #work in progress. This needs to be parsed

#Get Lifetime Stats
lifetimestatsurl = "{}{}/seasons/lifetime/gameMode{}/players?filter[playerIds]={}"
lifetimestatsrequest = requests.get(url = lifetimestatsurl.format(apiurl, gameplatform, gamemode, playerid), headers = apiauth)
lifetimestats = lifetimestatsrequest.json() #work in progress. This needs to be parsed

print (seasonstats)