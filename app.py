BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
endlines = '\n\n'

try:
    from requests import get
    from bs4 import BeautifulSoup
except:
    if czy == 'y' or czy == 'yes' or czy == 'YES' or czy == 'Y':
        from subprocess import call
        from sys import executable
        import pip

        call([executable, "-m", "pip", "install", 'bs4'])
        call([executable, "-m", "pip", "install", 'requests'])
    else:
        print('\n\n{}Thanks for using.'
              '\nCatch ya later!{}'.format(GREEN, END))
        exit()

from requests import get
from bs4 import BeautifulSoup


url = "https://www.worldometers.info/coronavirus/"
r = get(url)
soup = BeautifulSoup(r.content, 'html.parser')

info = soup.find_all('div', attrs={'class':'maincounter-number'})

table = ["In Ranking", "Total Cases: ", "New Cases", "Total Deaths", "New Deaths", "Total Recovered"]

all = info[0].text
deaths = info[1].text
recovereed = info[2].text

print('{}Hi, you can learn something about {}'.format(GREEN, RED) + 'COVID-19{}'.format(WHITE) + '{}  :)\n{}'.format(YELLOW, WHITE))
print('{}ALL Cases:  {}'.format(WHITE, RED)+all)
print('{}ALL Deaths:  {}'.format(WHITE, END)+deaths)
print('{}ALL Recovered:  {}'.format(WHITE, GREEN)+recovereed)


def info(country):
    global soup
    i = 0

    try:
        for td in soup.find('td', text=str(country)).parent.find_all('td'):
            country_info = td.text
            if(country_info != country):
                print(table[i]+' : '+country_info)
                i += 1
    except:
        pass


while True:
    country = input('{}What country do you want info about?  {}'.format(YELLOW, MAGENTA))
    print('{}'.format(BLUE))

    info(country)
    print(endlines)
