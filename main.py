import requests
from bs4 import BeautifulSoup
import webbrowser
from random import randint
import time


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

    # extract only the text from html file
    soup = BeautifulSoup(page.content, 'html.parser')
    onlytxt = [text for text in soup.stripped_strings]

    # write it to txt
    with open('br.txt', "w") as file:
        file.write(str(onlytxt))


def openandformat():
    with open('br.txt') as data:
        # remove the not needed characters
        data_list = data.read()
        data_list = data_list.replace("[", "").replace("'", "").replace(" ", "").replace("'", "")
        data_list = data_list.split(",")

        # put the required information onto new list
        start = data_list.index('Actions') + 1
        end = data_list.index('©2014-2016BoostRoyal.comAllRightsReserved')
        mylist = data_list[start:end]

        # remove another useless element
        mylist = [item for item in mylist if item != 'Waitingforbooster']

        # if there is order with txt "gameswith" add an extra element
        # to it's list so the number of arguments match with other orders
        k = 0
        for i in range(len(mylist)):
            if "gameswith" in mylist[i]:
                k = i
        if k != 0:
            mylist.insert(k, "dog")

        # make list of lists so 1 list represents 1 order
        number = 0
        finallist = []
        for i in range(6, (len(mylist) + 6), 6):
            finallist.append(mylist[number:i])
            number = i

        # check if order is good, then get it
        url = 'https://www.boostroyal.com/MembersArea/order/'
        for item in finallist:
            if item[3] == "NA":

                print("Coindions are met")
                goodurl = url
                goodurl += item[0] + '/lockIn'
                # webbrowser.open_new(goodurl)

        for item in finallist:
            print(item)
gethtml()
openandformat()
# def main():
#     counter = 0
#     while counter <= 100:
#         gethtml()
#         openandformat()
#         counter += 1
#         time.sleep(randint(0, 5))


# if __name__ == '__main__':
#     main()

# removes all multiply-customer duo orders, since they have less argumentum and fcks the script
# finallist = [item for item in finallist if "gameswith" not in item[1]]
