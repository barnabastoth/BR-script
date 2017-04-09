import requests
from bs4 import BeautifulSoup
import webbrowser


def gethtml():
    # logging into the site
    with requests.Session() as c:
        url = 'https://www.boostroyal.com/login'
        USERNAME = 'vigyor99@gmail.com'
        PASSWORD = 'Projector94'
        c.get(url)
        login_data = {"email":USERNAME, "password": PASSWORD, "_token":"G5WLdtCq7CJuarSwbyTuqjkbJpeNTzqRkGZ1bWCG"}
        c.post(url, data=login_data, headers={"Referer": "https://www.boostroyal.com/MembersArea/orders"})
        page = c.get("https://www.boostroyal.com/MembersArea/orders")


    soup = BeautifulSoup(page.content, 'html.parser')
    q = [text for text in soup.stripped_strings]


    with open('br.txt', "w") as file:
        file.write(str(q))


def openandformat():
    with open('br.txt') as data:
        # remove the not needed characters
        data_list = data.read()
        data_list = data_list.replace("[", "")
        data_list = data_list.replace("'", "")
        data_list = data_list.replace(" ", "")
        data_list = data_list.replace("[", "")
        data_list = data_list.replace("'", "")
        data_list = data_list.replace("|", "")
        data_list = data_list.split(",")

        # put the required information onto new list
        start = data_list.index('Actions') + 1
        end = data_list.index('©2014-2016BoostRoyal.comAllRightsReserved')
        mylist = data_list[start:end]

        # get how many orders are there
        numberoforder = 0
        for i in mylist:
            if len(i) == 4:
                if i.isdigit:
                    numberoforder += 1

        # remove another useless data
        for i in range(numberoforder * 2):
            mylist.remove('Waitingforbooster')
        
        #add | to every element then split them into string basod on | pos
        for i in range(6, len(mylist), 7):
            mylist.insert(i, "|")
        finallist = "".join(mylist)
        finallist = finallist.split('|')

        # check if order is good, then get it
        url = 'https://www.boostroyal.com/MembersArea/order/'
        for item in finallist:
            if 'EUW' or 'EUNE' in item:
                goodurl = url
                goodurl += item[0:4] + '/lockIn'
                # webbrowser.open_new(goodurl)

        # print(w)
        print (finallist)
gethtml()
openandformat()


# list with index of order ids
        # indexlist = []
        # for i in mylist:
        #     if len(i) == 4:
        #         if i.isdigit:
        #             indexlist.append(mylist.index(i))