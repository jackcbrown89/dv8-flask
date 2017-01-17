from py_bing_search import PyBingNewsSearch
import codecs
import pprint

def getScore(search_term):
    bing_news = PyBingNewsSearch('/kTKVdRbZwkXtIWdbGVGpOO1rm8s8GSA9rypv4T1+hA', search_term)

    with codecs.open('positive-words.txt', 'rU', encoding='utf-8') as f: #'f = open('positive-words.txt', 'r')
        results20 = bing_news.search(limit=10, format='json')
        score = 0
        j = 0

        for line in f:
            if '\n' in line:
                line = line.replace('\n', '')
            j += 1
            for result in results20:
                sresult = result.description
                if line in sresult:
                    if score < 100:
                        #print result.url
                        score += 1
                        #print score
                        #print line

    with codecs.open('negative-words.txt', 'rU', encoding='ISO-8859-1') as f:  # 'f = open('positive-words.txt', 'r')
        results20 = bing_news.search(limit=10, format='json')
        j = 0

        for line in f:
            if '\n' in line:
                line = line.replace('\n', '')
            j += 1
            for result in results20:
                sresult = result.description
                if line in sresult:
                    if score < 100:
                        score -= 1
                        #print score
                        #print line
    print score
    return score