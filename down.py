#-*-coding:utf-8-*-
import urllib
import urllib2

url = 'http://hotels.ctrip.com/hotel/hong%20kong58/t1b1p'

if __name__ == '__main__':
    for j in range(8, 9):
        print 'page',j
        urls = url + str(j)
        pt = urllib2.urlopen(urls)
        op = open(str(j)+'.html', 'wb')
        while True:
            s = pt.read()
            if not s:
                break
            op.write(s)
        op.close()
        pt.close()
