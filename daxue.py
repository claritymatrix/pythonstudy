import requests


from bs4 import BeautifulSoup
import bs4

# what:获取指定url网页

# why:用于筛选出指定数据

# who: url

# when:当调用这个函数的时候

# where:适用于数据都在一页上


# how: 使用requests 库 获取response类数据获取整个网页html代码


# how much: 可以使用r.text[0:500] 之类的限定看看取的数据怎么样。

def getHtmlText(url):

    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

#what: 解析html 网页

# why: 选出需要的数据

# who: beautifulSoup 类

# when:当调用这个函数的时候

# how: 使用 html.parser

# where: 所有数据在一个页面中

# how much: 目标数量可以控制，复杂程度有限
def fillUnivList(ulist,html):

    soup = BeautifulSoup(html,"html.parser")

    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

# 格式化输出数据


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
