countries = ['united states','brazil','china','russia','canada','mexico','iceland','new zealand'] #the list of coutries that you'll take from

points = 107 #us=8ec,7pop,8mil china=7ec,8pop,7mil russia=6ec,8pop,7mil canada=6ec,5pop,6mil brazil=4ec,6pop,8mil mexico=3ec,4pop,3mil new zealand=2ec,2pop,2mil ice land=1ec,1pop,1mil

yourPoints = 0

picks = 4

yourList=[]

print('this is the totally scientific war simulator. \nit calculates which countries would win if they teamed up for a world war. you will pick 4 countries from a list of 8 and the program will calculate if your four teams would win. \nhere is the list of countries ', countries,'\ndo not start with a space and use all lowercase letters when picking countries')

def howManyLeft():
        print('you have ',picks, 'picks')

howManyLeft()


def pickCountry():
                pick= str(input('what country do you want?' ))
                if pick not in countries:
                        print('not on list')
                        pickCountry()
                else:
                        countries.remove(pick)
                        yourList.append(pick)
                        print('picked')
for x in range(4):
        pickCountry()
        picks-=1
        howManyLeft()

if 'united states' in yourList:
        points-=23
        yourPoints+=23

if 'china' in yourList:
        points-=22
        yourPoints+=22

if 'russia' in yourList:
        points-=17
        yourPoints+=17

if 'canada' in yourList:
        points-=13
        yourPoints+=13

if 'brazil' in yourList:
        points-=14
        yourPoints+=14

if 'mexico' in yourList:
        points-=10
        yourPoints+=10

if 'new zealand' in yourList:
        points-=6
        yourPoints+=6

if 'ice land' in yourList:
        points-=3
        yourPoints+=3

print('\nyou picked ',yourList,' and your team has this many points: ',yourPoints,'\n\nto go against ',countries,' who have this many points: ',points)

if yourPoints > points:
        print('\n\nyour team of countries won')
else:
        print('\n\nyour team lost')