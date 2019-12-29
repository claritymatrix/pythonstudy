import requests


from bs4 import BeautifulSoup
import bs4


def getHtmlText(url):

    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist,html):

    soup = BeautifulSoup(html,"html.parser")

    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])




def printUnivlist(ulist,num):


    tptl = "{:^10}\t{:^6}\t{:^10}"

    print(tptl.format("排名","学校名称","总分"))

    for i in range(num):
        u = ulist[i]
        print(tptl.format(u[0],u[1],u[2]))


    print("Suc" + str(num))



if __name__ == "__main__":

    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    html  = getHtmlText(url)

    print(html[0:500])
    #fillUnivList(uinfo,html)

    fillUnivList(uinfo,html)
    printUnivlist(uinfo,20)
