from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
excel_name = "书籍.xlsx"
wb = Workbook()
ws1 = wb.active
ws1.title='书籍'


def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    html = requests.get(url, headers=header).content
    return html


def get_con(html):
    soup = BeautifulSoup(html,'html.parser')
    book_list = soup.find('div', attrs={'class': 'article'})
    page = soup.find('div', attrs={'class': 'paginator'})
    next_page = page.find('span', attrs={'class': 'next'}).find('a')
    name_list = []
    for i in book_list.find_all('table'):
        book_name = i.find('div', attrs={'class': 'pl2'})
        intro_name = i.find('p', attrs={'class': 'quote'})
        m = list(book_name.find('a').stripped_strings)
        if (intro_name):
            n = list(intro_name.find('span').stripped_strings)
        else:
            n = ['no intro']
        if len(m)>1:
            x = m[0]+m[1]
        else:
            x = m[0]

        if len(n)>1:
            y = n[0]+n[1]
        else:
            y = n[0]
        #print(x)
        name = []
        name.append(x)
        name.append(y)
        name_list.append(name);
    if next_page:
        return name_list, next_page.get('href')
    else:
        return name_list, None


def main():
    url = 'https://book.douban.com/top250'
    name_list=[]
    while url:
        print("visited:"+url)
        html = get_html(url)
        name, url = get_con(html)
        if url != None:
            print("return url:"+url)
        print(name)
        name_list += name;
    for i in name_list:
        ws1.append(i)
    wb.save(filename=excel_name)


if __name__ == '__main__':
    main()

