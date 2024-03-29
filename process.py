import numpy, time, re, urllib, urllib2, xml.etree.cElementTree as ElementTree
import datetime
from datetime import tzinfo, timedelta, date
#day (top to bottom = today to 1 month ago), open, high, low, close, volume
from bs4 import BeautifulSoup

#declare constants
url = 'http://ws.nasdaqdod.com/v1/NASDAQAnalytics.asmx/GetSummarizedTrades'

def compileArray(ticker):
    params = []
    dailyval = []

    dayZero = datetime.datetime.now() - timedelta(2)
    dayZero = dayZero.strftime('%m/%d/%Y 00:00:00.000')
    #print time.strftime('%m/%d/%Y %H:%M:%S')
    #print dayZero
    #timedelta(30)
    for i in range(0, 30):

        thatDay = datetime.datetime.now() - timedelta(30-i)
        nextDay = datetime.datetime.now() - timedelta(29-i)
        thatDay = thatDay.date()
        nextDay = nextDay.date()

        print thatDay
        #print thatDay.isoformat()
        values = {'_Token': 'BCBCB14207A44BCA83F27AAC98ACCB00',
                      'Symbols': ticker,
                      'StartDateTime': '%s 9;30;00' % thatDay,
                      'EndDateTime': '%s 16;0;0' % nextDay, #time.strftime('%m/%d/%Y %H:%M:%S.001'),
                      'MarketCenters': '',
                      'TradePrecision': 'Hour',
                      'TradePeriod': '30'}

        # Build HTTP request
        request_parameters = urllib.urlencode(values)
        req = urllib2.Request(url, request_parameters)

        # Submit request
        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            print(e.code)
            print(e.read())

        #print thatDay

        day = thatDay

        # Read response
        the_page = response.read()

        # Parse page XML from string
        soup = BeautifulSoup(the_page, 'lxml')
        if soup.find('volume') is not None:
            open = soup.first.string
            high = soup.high.string
            low = soup.low.string
            close = soup.last.string
            volume = soup.volume.string
            #params.append((close, volume, open, high, low))
            dailyval.append(close)

        else:
            print dailyval
            # print '\n'
            # print i
            # print '\n'
            if dailyval == []:
                dailyval.append(0)

            else:
                dailyval.append(dailyval[i-1])
                print dailyval            #params.append(params[i-1])
    #def collectInfo(ticker):
    return dailyval