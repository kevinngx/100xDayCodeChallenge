from riotwatcher import LolWatcher, ApiError
import discord
from datetime import datetime

api_key = "RGAPI-17143338-a471-4265-bcba-599097bc623e"
my_region = 'OC1'
client = discord.Client()

def main():
    print("Starting bot...")
    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('Recent Wins:'):
            contents = str(message.content).split(":")
            await message.channel.send("Finding stats, please wait...")
            await message.channel.send(getUserStats(contents[1]))

        if message.content.startswith('Give me justin quotes'):
            await message.channel.send("\"Women aint shit\"")

        if message.content.startswith("Games Today:"):
            contents = str(message.content).split(":")
            summoner = contents[1]
            await message.channel.send("Getting number of games " + summoner + " played today, please wait...")
            await message.channel.send(getTodaysGamesSingle(summoner))
            
        if message.content.startswith("Games Everyone:"):
            await message.channel.send("Getting number of games everyone played today, please wait...")
            await message.channel.send(getTodaysGamesEveryone())

    client.run("ODc2MDc0NDI5NTM5NTgxOTgz.YRex5A.VUrdeUfhQZhRIDIgEmxMV7b4acE")

def getTodaysGamesEveryone():
    watcher = LolWatcher(api_key)
    summoners = ["engagingraging", "gillette", "anotherasian96", "shizzukani", "katastrophically", "lucians in paris", "kris wu did it",  "Ekkos In Paris", "Joisugoi"]
    result = ""
    for summoner in summoners:
        result = result + getTodaysGamesSingle(summoner) + "\n"
    return result

def getTodaysGamesSingle(summoner):
    watcher = LolWatcher(api_key)
    call = watcher.summoner.by_name(my_region, summoner)
    summoner_puuid = call["puuid"]
    print("Summoner Name = " + summoner)
    print("Summoner Level = " + str(call["summonerLevel"]))
    return ( summoner + " played " + str(getTodaysGames(summoner_puuid, summoner)) + " games today!")

def getTodaysGames(summoner_puuid, summoner):
    match_watcher = LolWatcher(api_key, default_match_v5=True)
    match_list = match_watcher.match.matchlist_by_puuid('AMERICAS', summoner_puuid, 0, 10) # max 100 --> bottleneck occurs here, needs to call for each match
    games_played_today = 0
    print(match_list)
    for match in match_list:
        match_details = match_watcher.match.by_id('AMERICAS', match)
        if (checkDateOfMatch(match_details) == datetime.today().date()):
            games_played_today = games_played_today + 1
    return games_played_today

def checkDateOfMatch(match_details):
    milis_ts = int(match_details["info"]["gameCreation"])
    ts = datetime.fromtimestamp(milis_ts/1000)
    print(ts)
    return ts.date()

def getUserStats(summoner_name):
    watcher = LolWatcher(api_key)
    summoner = summoner_name
    call = watcher.summoner.by_name(my_region, summoner)
    summoner_puuid = call["puuid"]
    print("Summoner Name = " + summoner)
    print("Summoner Level = " + str(call["summonerLevel"]))
    return "Wins in last 10 games = " + str(getRecentWins(summoner_puuid, summoner))
    
def getRecentWins(summoner_puuid, summoner):
    match_watcher = LolWatcher(api_key, default_match_v5=True)
    match_list = match_watcher.match.matchlist_by_puuid('AMERICAS', summoner_puuid, 0, 10) # max 100 --> bottleneck occurs here, needs to call for each match
    index = 1
    wins = 0
    for match in match_list:
        index = index + 1
        match_details = match_watcher.match.by_id('AMERICAS', match)
        if ( getSummonerTeam(summoner, match_details) == getGameResult(match_details) ):
            wins = wins + 1
    return wins

def getGameResult(match_details):
    for team in match_details["info"]["teams"]:
        if (team["win"] == True):
            return team["teamId"]

def getSummonerTeam(summoner, match_details):
    for participant in match_details["info"]["participants"]:
        if (participant["summonerName"].lower() == summoner.lower()):
            return participant["teamId"]

if __name__ == "__main__":
    main()
   


