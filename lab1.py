import random
import math



symbols = ["a", "b", "c"]
alphabet = "abcdefghijklmnopqrstuvwxyz"

def create_file1():
    with open("file1.txt", "w") as file:
        for i in range(10240):
            file.write(random.choice(symbols))
        file.close()

def create_file2():
    with open("file2.txt", "w") as file:
        for i in range(10240):
            file.write(random.choices(symbols, weights=[0.2, 0.3, 0.5])[0])
        file.close()

def create_file3():
    with open("file3.txt", "w") as file:
        text = ""
        text += "The United Kingdom of Great Britain has the excellent transport infrastructure. Not only the " \
                "huge tourist flow, but also the development of the country itself and, in particular, " \
                "the business sphere contributed there. The total length of all roads is at least 399 thousand " \
                "kilometers. At the same time, there are relatively few highways in the country. They make only " \
                "about three and a half thousand kilometers. You can travel by car in any region of the " \
                "country. Don’t forget that the UK has the left-hand traffic. In London, there is a metro or a " \
                "tube that embraces 12 underground, land and mixed lines. It is worth noting that the lines are " \
                "often split into separate small branches, so you should always follow the transport route. " \
                "There are also taxi services in the country. The most expensive vehicles are black cabs. They " \
                "can be stopped simply on the street. Cars are always upscale, with a clean and comfortable " \
                "interior. Drivers use a meter. The less expensive taxi should be called on the phone. In this " \
                "case, you need to clarify the price, since there is no meter in the cabin. Large cities have " \
                "trams. In London, you can even find two-story trams. However, buses are considered the most " \
                "popular way of traveling around the city. They run from 4-5 am until 1 am. There are some " \
                "night routes. As a rule, they only cruise around major cities and the most popular " \
                "destinations. Tickets for public transport can be bought at roadside kiosks, at stops and " \
                "railway stations, as well as directly from the driver. Locals don’t move between cities by " \
                "buses; they use trains instead. It will be much more comfortable, although the ticket price " \
                "for trains is much higher. About 50 years ago, the railway line across the territory of the " \
                "modern kingdom was in a very poor state. However, the authorities took action, and now the " \
                "railway network in the UK is one of the best in Europe. The cost of the ticket depends on the " \
                "class of the train and the length of the way. It is worth noting that you can get even to the " \
                "most remote villages. Between the regions of the kingdom and between coastal cities, " \
                "one can travel by means of water transport. In particular, you can use ferries. Special boats, " \
                "water taxis, yachts and a variety of sightseeing small ships cruise the Thames. Air transport " \
                "is also decent in the UK. The country has a lot of domestic and international airports, " \
                "so moving between the most remote points of the state will be quick and comfortable. In " \
                "addition, the cost of air tickets is quite acceptable. It is possible to move around the city " \
                "by bicycles. Authorities zealously support this trend, so they constantly expand the network " \
                "of bicycle lanes. You can rent a two-wheeled vehicle in any town. This is especially true in " \
                "larger cities, where the ancient streets are very narrow, and the traffic jams can be as long " \
                "as several kilometers. You can also rent a car, but only with an international driver's " \
                "license. Such an option will cost you at least $60 per day."
        text += "The air transport network in Great Britain is simply superb. In total, about 450 airports " \
                "operate in the country. Some of them are used not only for passenger transportation but also for " \
                "freight. The main airports serve domestic and international flights. Heathrow Airport is the " \
                "largest air harbor in the country. It is located twenty kilometers from London. It has no equal " \
                "on the territory of the kingdom. Heathrow holds a decent 4th place in the world. There are five " \
                "terminals at the airport. Everything there is arranged for the comfortable rest of passengers, " \
                "including bank offices, cafes and restaurants, various shops, lounges, business centers and baby " \
                "care rooms. You can get to the city by bus or by train. You can also book a transfer and a taxi " \
                "in advance, or rent a car. Gatwick Airport is on a second place in the country. Although, " \
                "it is the busiest airport in the world by its capacity. It has two terminals, between which a " \
                "line of underground trains lies. An infrastructure of the air harbor is nice. Here, you can find " \
                "souvenir shops and boutiques, nurseries and meeting rooms, restaurants and cafes. It should be " \
                "noted that hotels are located right on the territory. This airport is situated 46 kilometers " \
                "from London. On the opposite side, at the same distance from the capital, there is Stansted " \
                "Airport. It is famous for its unusual architecture and high-quality service. Manchester Airport " \
                "is located near the city of the same name. Its scale is not very impressive if compared to the " \
                "first three air harbors. Still, the quality of service is also great. There are a railway " \
                "station and a bus station on the territory of the airport. Scottish Edinburgh Airport is just 12 " \
                "kilometers from the city of the same name. This harbor has recently become international. This " \
                "direction is very popular today. Gibraltar Airport serves not only civilian but military forces. " \
                "The Bristol air gate is one of the ten busiest airports in the whole kingdom. There is only one " \
                "international airport on the territory of Wales, Cardiff. It is located only 20 kilometers from " \
                "the city. You can get there by bus or by train."
        text += "The UK is characterized by a rather developed transport infrastructure. It is comfortable to " \
                "travel by any mean of transport. The state monitors the condition of the fleet, trains, planes, " \
                "and sea transport. Therefore, the cost of a journey is quite comparable to the quality of service " \
                "and comfortable roads. Very few travelers choose a car as the main mean of transportation around " \
                "the country. The traffic is left-handed, and most tourists are simply not accustomed to this. It " \
                "can be a problem to drive in the largest tourist cities by car because all the ancient streets " \
                "are very narrow. That is especially true for London. Nevertheless, you can rent a car in every " \
                "airport or in a large city. A bicycle can be an option. Almost all the cities of the country have " \
                "branched bike lanes. Therefore, it will be possible not only to get to the desired destination " \
                "quickly and inexpensively but also to admire the surrounding nature. The most popular public " \
                "transport in the country is a bus. Inside the city, buses run in different directions every 15-20 " \
                "minutes. There are lines working from 4 am to 1 am. There are night buses on the most popular " \
                "routes. On holidays, the amount of transport is significantly reduced. You can buy bus tickets at " \
                "roadside kiosks, at bus stops or at train stations and directly from the driver. You can buy a " \
                "one-time ticket or a travel card. In the second case, you can save a little. Long-distance buses, " \
                "as a rule, depart from bus stations every hour. Much attention is paid to the comfort. Some " \
                "companies offer their passengers drinks and light snacks. Oxford Two-story red buses are the " \
                "feature of the UK. However, few people have heard about red double-decker trams. Although they " \
                "are quite common in London. Such mean pf transport appeared in the capital 50 years ago. Later it " \
                "disappeared, and only a few years ago local authorities returned such transport to the city. It " \
                "is worth noting that you can buy a travel card, which allows traveling by bus and by tram. Also, " \
                "the metro is very popular in the capital. This one is among the oldest in the world. There are " \
                "only 12 lines. Many of them are mixed and have land and underground sections. The branches " \
                "themselves are rather confused, so when traveling, you should closely follow the route map. " \
                "Please note that hitch-hiking is common in the UK. This type of transportation is safe and " \
                "inexpensive. The UK has a very long railway network. That’s one of the best in Europe. The most " \
                "remote regions of the country can be reached by means of such transport. In order to save a " \
                "little, it is worth buying tickets one or two weeks in advance. You can also get a reusable " \
                "ticket. The speed of most of the trains in England reaches two hundred kilometers per hour. The " \
                "cars are clean and comfortable. Trains run according to the schedule. The maximum delay time is " \
                "10-20 minutes. The cost depends on the duration of the trip, the point of departure and the " \
                "class of a train or a car. To save time, many tourists travel between the most famous cities of " \
                "the kingdom by air. There are about 450 air harbors in the country. Domestic flights are " \
                "available at almost every airport. You can get there by buses, trains, transfers or by taxi. " \
                "Since the United Kingdom is an island state, there is a well-developed sea transport. You can " \
                "move between the mainland and coastal cities by ships and ferries. Moreover, the second type of " \
                "transport is more popular among tourists. Firstly, its cost is low. Secondly, it is possible to " \
                "transport any goods, and even cars or bicycles on ferries. In the midst of the tourist season, " \
                "water taxis, yachts, and excursion boats run on Thames in London. You can also take a taxi. " \
                "There are two main types of taxis - with meters and with a fixed tariff. In the first case, " \
                "such a car can be taken on the street. The second type of taxi can be called only by phone. " \
                "Don't forget to get the cost of the trip from the operator in advance."
        text += "The United Kingdom embraces several historical provinces under its flag. The mentality of the " \
                "inhabitants isn’t similar. Irish, Scots, Welsh, and English differ with traditions, temperament " \
                "and even languages. The stereotype of stiffness and indifference of the British has a reason. " \
                "They really know how to hide emotions and demonstrate an equal attitude to everything that is " \
                "happening. Locals are incredibly punctual and polite; they try to avoid contentious issues and " \
                "conflicts. The English have an incredible self-control. It is almost impossible to get them out " \
                "of their minds. They are taught from their childhood how to manage all possible difficulties. " \
                "Nevertheless, these people are characterized by the snobbery and vanity. Englishmen rarely use " \
                "denial or assertion. Most often they answer 'I think' or 'maybe'. They listen attentively " \
                "without interrupting, but even a smile can hardly mean that an interlocutor agrees. The concept " \
                "of English humor is widely known in the world. Despite their emotional stinginess, the British " \
                "like to joke. They make fun of themselves, the royal family, and the church. Their humor is " \
                "quite specific and is not understood by everyone. The British seek to preserve their identity. " \
                "They are separated from the rest of Europe not only territorially, but also culturally. This " \
                "country is the only one in Europe where cars are still moving along the left side of the road. " \
                "The UK managed to keep its currency and a measure of distance. UK, with all its cultural " \
                "versatility, has a lot of authentic traditions. The most striking of these is the traditional " \
                "tea party. A table for tea has to stand near the fireplace, which is the coziest place of the " \
                "house. It is covered with a snow-white or blue tablecloth. Utensils from one set are used; " \
                "different cups and saucers are considered bad form. There must be a tea set on the table. It " \
                "includes a teapot, a jug of boiling water, a milkman, dessert plates, forks and knives, " \
                "a strainer stand, a sugar bowl with tongs and a wool cover that is put on a jug with boiling " \
                "water. Toast, butter, eggs, sweet and unsweetened pastries, jams, and cookies are served too."
        text = text.replace("\n", "")
        text = text.replace(".", "")
        text = text.replace(",", "")
        text = text.replace(":", "")
        text = text.replace("-", "")
        text = text.replace(";", "")
        text = text.replace("", "")
        text = text.replace("  ", "")
        text = text.replace("’", "")
        text = text.replace("'", "")
        text = text.replace("$", "")
        text = text.replace("0", "")
        text = text.replace("1", "")
        text = text.replace("2", "")
        text = text.replace("3", "")
        text = text.replace("4", "")
        text = text.replace("5", "")
        text = text.replace("6", "")
        text = text.replace("7", "")
        text = text.replace("8", "")
        text = text.replace("9", "")
        text = text.lower()
        text = text[:10240]
        file.write(text)
        file.close()

def shennon(probabilities):
    res = 0.0
    for item in probabilities:
        res -= item * math.log2(item)
    return res

def firstProbability(file_name):
    file = open(file_name, "r")
    text = file.read()
    file.close()
    all_probabilities = {}
    for char in text:
        if char in all_probabilities:
            all_probabilities[char] += 1.0 / len(text)
        else:
            all_probabilities[char] = 1.0 / len(text)
    entropy = 0
    prob_list = []
    for item in all_probabilities:
        prob_list.append(all_probabilities[item])
    entropy = shennon(prob_list)
    print("First probability for " + file_name + ": " + str(entropy))

def secondProbability(file_name, alphabet):
    file = open(file_name, "r")
    text = file.read()
    file.close()
    all_probabilities = {}
    check_repeating = []
    for i in range(10239):
        if text[i] + text[i + 1] in all_probabilities:
            all_probabilities[text[i] + text[i + 1]] += 1.0 / len(text)
        else:
            all_probabilities[text[i] + text[i + 1]] = 1.0 / len(text)
    entropy = 0
    prob_list = []
    for item in all_probabilities:
        prob_list.append(all_probabilities[item])
    entropy = shennon(prob_list) / 2
    print("Second probability for " + file_name + ": " + str(entropy))

def thirdProbability(file_name, alphabet):
    file = open(file_name, "r")
    text = file.read()
    file.close()
    all_probabilities = {}
    check_repeating = []
    for i in range(10238):
        if text[i] + text[i + 1] + text[i + 2] in all_probabilities:
            all_probabilities[text[i] + text[i + 1] + text[i + 2]] += 1.0 / len(text)
        else:
            all_probabilities[text[i] + text[i + 1] + text[i + 2]] = 1.0 / len(text)
    entropy = 0
    prob_list = []
    for item in all_probabilities:
        prob_list.append(all_probabilities[item])
    entropy = shennon(prob_list) / 3
    print("Third probability for " + file_name + ": " + str(entropy))

def run():
    create_file1()
    create_file2()
    create_file3()

    firstProbability("file1.txt")
    firstProbability("file2.txt")
    firstProbability("file3.txt")

    secondProbability("file1.txt", symbols)
    secondProbability("file2.txt", symbols)
    secondProbability("file3.txt", alphabet)

    thirdProbability("file1.txt", symbols)
    thirdProbability("file2.txt", symbols)
    thirdProbability("file3.txt", alphabet)


