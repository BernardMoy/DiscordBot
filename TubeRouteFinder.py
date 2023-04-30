import discord
client = discord.Client()



@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))




@client.event
async def on_message(msg):

    if msg.author == client.user:
        return


    class Station:
        def __init__(self, name, line):
            self.name = name
            self.line = line
            self.next = {}

        def addNext(self, station, travelTime):  # key = station object
            self.next[station] = travelTime


    # Internal methods
    # Add a new link of the second station to the first station, with a travel time
    # It is not needed to specify the lines since the route method wil do that for us
    # sID1 and sID2 are station objects, time is a int object (minute)
    async def addLink(sID1 : Station, sID2 : Station, time : int):
        sID1.addNext(sID2, time)
        sID2.addNext(sID1, time)



    mar = Station("Marylebone", "Bakerloo")
    basb = Station("Baker street", "Bakerloo")
    rep = Station("Regent's park", "Bakerloo")
    oxcb = Station("Oxford circus", "Bakerloo")
    picb = Station("Piccadilly circus", "Bakerloo")
    chcb = Station("Charing cross", "Bakerloo")

    grpv = Station("Green park", "Victoria")
    oxcv = Station("Oxford circus", "Victoria")
    wasv = Station("Warren street", "Victoria")

    basj = Station("Baker street", "Jubilee")
    bosj = Station("Bond street", "Jubilee")
    grpj = Station("Green park", "Jubilee")

    maa = Station("Marble arch", "Central")
    bosc = Station("Bond street", "Central")
    oxcc = Station("Oxford circus", "Central")
    tcrc = Station("Tottenham court road", "Central")
    holc = Station("Holborn", "Central")

    wasn = Station("Warren street", "Northern")
    gdg = Station("Goodge street", "Northern")
    tcrn = Station("Tottenham court road", "Northern")
    lsqn = Station("Leicester square", "Northern")
    chcn = Station("Charing cross", "Northern")

    hpc = Station("Hyde park corner", "Piccadilly")
    grpp = Station("Green park", "Piccadilly")
    picp = Station("Piccadilly circus", "Piccadilly")
    lsqp = Station("Leicester square", "Piccadilly")
    holp = Station("Holborn", "Piccadilly")

    # Add stations to data
    allStations = [mar, basb, rep, oxcb, picb, chcb, grpv, oxcv, wasv, basj, bosj, grpj, maa, bosc, oxcc, tcrc, holc,
                   wasn, gdg, tcrn, lsqn, chcn, hpc, grpp, picp, lsqp, holp]

    availableStationsList = []

    for key in allStations:
        if (key.name not in availableStationsList):
            availableStationsList.append(key.name)
    availableStations = ", ".join(availableStationsList)


    # Add links to stations. The addLink function is undirected,
    # i.e. does not require both addLink (a,b, _) and addLink (b,a,_)

    #Bakerloo
    await addLink(mar, basb, 1)
    await addLink(basb, rep, 1)
    await addLink(rep, oxcb, 2)
    await addLink(oxcb, picb, 2)
    await addLink(picb, chcb, 2)

    #Victoria
    await addLink(wasv, oxcv, 2)
    await addLink(oxcv, grpv, 1)

    #Jubilee
    await addLink(basj, bosj, 2)
    await addLink(bosj, grpj, 1)

    #Central
    await addLink(maa, bosc, 1)
    await addLink(bosc, oxcc, 1)
    await addLink(oxcc, tcrc, 2)
    await addLink(tcrc, holc, 2)

    #Northern
    await addLink(wasn, gdg, 1)
    await addLink(gdg, tcrn, 2)
    await addLink(tcrn, lsqn, 1)
    await addLink(lsqn, chcn, 1)

    #Piccadilly
    await addLink(hpc, grpp, 2)
    await addLink(grpp, picp, 2)
    await addLink(picp, lsqp, 2)
    await addLink(lsqp, holp, 2)

    #Interchanges
    await addLink(basb, basj, 1)
    await addLink(bosj, bosc, 2)
    await addLink(oxcc, oxcv, 3)
    await addLink(oxcc, oxcb, 2)
    await addLink(oxcb, oxcv, 2)
    await addLink(grpj, grpp, 2)
    await addLink(grpp, grpv, 2)
    await addLink(grpj, grpv, 1)
    await addLink(picb, picp, 1)
    await addLink(chcb, chcn, 1)
    await addLink(lsqn, lsqp, 1)
    await addLink(tcrc, tcrn, 1)
    await addLink(holc, holp, 1)
    await addLink(wasv, wasn, 1)




    # find the corresponding station objects when given name
    async def findStation(name):
        result = []

        for s in allStations:
            if (s.name.lower() == name.lower()):
                result.append(s)

        return result

    # determine the shortest route between two stations (start and end).
    # Dictionary distance[station] represents the current distance between that station and the starting station
    # Dictionary parent[station] stores the parent (The station which lead to the current station).
    async def route(start, end):

        # a dictionary storing lists of parents
        parent = {}
        parent[start] = None

        unvisited = []
        for i in allStations:
            unvisited.append(i)

        # a dictionary storing distance between a station and start (where =0)
        distance = {}
        for s in allStations:
            distance[s] = float('inf')

        distance[start] = 0

        # start exploring while there are unvisited nodes
        current = start

        while (unvisited):

            # update distance of unvisited neighbors
            for key, value in current.next.items():
                if (distance[current] + value < distance[key]):
                    distance[key] = distance[current] + value

                    # store (node, predecessor) pair in the parent{} dictionary if the distance updates
                    parent[key] = current

            unvisited.remove(current)

            # find the unvisited node with the smallest distance.
            minDistance = float('inf')
            unvisitedNodeMinDistance = None

            for key, value in distance.items():
                if key in unvisited and value < minDistance:
                    minDistance = value
                    unvisitedNodeMinDistance = key

            current = unvisitedNodeMinDistance

        # Retrieve the route by backtracking
        route = []

        currentStation = end
        route.append(end)

        while (parent[currentStation] != None):
            route.append(parent[currentStation])
            currentStation = parent[currentStation]

        route.reverse()
        route.append(distance[end])
        return route

    def getColor(line):
        colors = {
            'Bakerloo': 0x996633,
            'Central': 0xCC3333,
            'Circle': 0xFFCC00,
            'District': 0x006633,
            'Hammersmith and City': 0xCC9999,
            'Jubilee': 0x868F98,
            'Metropolitan': 0x660066,
            'Northern': 0x000000,
            'Piccadilly': 0x000099,
            'Victoria': 0x0099CC,
            'Waterloo and City': 0x66CCCC
        }
        hex = colors.get(line, None)
        return hex



    async def findPath(startInput, endInput):

        startStationList = await findStation(startInput)
        endStationList = await findStation(endInput)

        minTime = float('inf')
        finalRoute = []
        finalStart = None

        for i in startStationList:
            for j in endStationList:

                currentRoute = await route(i, j)
                if currentRoute[-1] < minTime:
                    minTime = currentRoute[-1]
                    finalRoute = currentRoute
                    finalStart = i

        # Output the result.
        currentLine = finalStart.line
        prevStation = None

        accumulatedTime = 0  # time spend on a single line
        accumulatedStationCount = 0  # stations on a single line

        totalTime = 0  # total time

        details = ""


        for station in finalRoute[:-1]:
            # Line changed
            if station.line != currentLine:
                #Print previous line log
                footer = (str(accumulatedStationCount) + " stations (" + str(accumulatedTime) + " mins)" + '\n')

                embed = discord.Embed(title=(currentLine +' line'), description=details, color=getColor(currentLine))
                embed.set_footer(text=footer)
                await msg.channel.send(embed=embed)

                #Reset data
                details = ""
                accumulatedTime = 0
                accumulatedStationCount = 0

                #Print walking info
                time = prevStation.next[station]
                title = ("Walk for " + str(time) + " mins")
                totalTime += time
                currentLine = station.line

                embed = discord.Embed(title=title, description="Change to "+ currentLine + " line at " + station.name, color=getColor(currentLine))
                await msg.channel.send(embed=embed)


            # start
            if (prevStation == None):
                details += (station.name + " (Start)" + '\n')

            # interchanging station
            elif station.name == prevStation.name:
                details += (station.name + '\n')

            else:
                time = prevStation.next[station]
                accumulatedTime += time
                accumulatedStationCount += 1
                totalTime += time
                details += (station.name + " (" + str(time) + " mins)" + '\n')

            prevStation = station

        # end of journey
        footer = (str(accumulatedStationCount) + " stations (" + str(accumulatedTime) + " mins)" + '\n' + "Total travelling time: " + str(totalTime) + " mins")

        embed = discord.Embed(title=(currentLine + ' line'), description=details, color=getColor(currentLine))
        embed.set_footer(text=footer)
        await msg.channel.send(embed=embed)


    #User command
    if (msg.content.lower() == '-go'):
        embed = discord.Embed(title="Please enter your starting station",
                              description="This tool will find the (theoretical) shortest path between any two available stations below:"
                                          +'\n\n'+availableStations,
                              color=0x040273)
        await msg.channel.send(embed=embed)

        station1Message = await client.wait_for('message')
        station1 = station1Message.content

        # Starting station
        await msg.channel.send(f"You entered: {station1}")


        embed = discord.Embed(title="Please enter your destination station",
                              description="This tool will find the (theoretical) shortest path between any two available stations below:"
                                          +'\n\n'+availableStations,
                              color=0x040273)
        await msg.channel.send(embed=embed)

        station2Message = await client.wait_for('message')
        station2 = station2Message.content

        # Destination station
        await msg.channel.send(f"You entered: {station2}")

        try:
            #Print the list of stations to the destination (shortest route)
            await findPath(station1, station2)

        except:
            embed = discord.Embed(title="Invalid parameters",
                                  description="Start: "+station1 + '\n' + "End: "+station2,
                                  color=0xe64915)
            await msg.channel.send(embed = embed)





client.run('token_goes_here')