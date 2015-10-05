#-*-coding:utf-8-*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import sys
import xlwt

reload(sys)
sys.setdefaultencoding('gb18030')

if __name__ == '__main__':
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    index = 1
    
    for j in range(1, 9):
        print 'page',j
        pt = open(str(j)+'.html')
        soup = BeautifulSoup(pt.read(), from_encoding='gb18030')
        pt.close()
        items = soup.find_all('div', class_='searchresult_list')
        #items = soup.find_all('span', class_='hotel_num')
        
        for i in range(0, 25):
            parent = items[i]
            
            ## info
            if parent('li',class_='searchresult_info_name') == []:
                continue
            child = parent('li',class_='searchresult_info_name')[0];
            
            name = child.a['title']
            nlist = name.split('(')
            cname = nlist[0]
            #print cname, ename
            sheet.write(index, 0, cname)
            if len(nlist) > 1:
                ename = nlist[1].replace(')', '')
                sheet.write(index, 1, ename)
            
            site = child('p',class_='searchresult_htladdress')[0].contents[0].strip()
            site = site[0:len(site)-1]
            #print site
            sheet.write(index, 2, site)
            
            dtl1 = child('p',class_='searchresult_htladdress')[0].contents[2].strip()
            dtl0 = child('p',class_='searchresult_htladdress')[0].contents[1].contents[0].strip()
            detail = dtl0 + dtl1[0:len(dtl1)-1]
            #print detail
            sheet.write(index, 3, detail)
            
            ## price
            childs = parent.find_all('span',class_='base_txtdiv')
            rmb = float('inf')
            hkd = float('inf')
            for child in childs:
                tmp = child['data-params']
                tmp = '{'+tmp[tmp.find("'avePrice'"):tmp.find(",'weeks'")]+'}'
                dct = eval(tmp)
                del dct['oriCurrency']
                if int(dct['oriPrice']) < rmb:
                    rmb = int(dct['oriPrice'])
                    hkd = int(dct['avePrice'])
            #print rmb, hkd
            if rmb != float('inf'):
                sheet.write(index, 4, rmb)
                sheet.write(index, 5, hkd)
            
            wbk.save('hotel.xls')
            index += 1
            
            print 'item',i
