import connect
import download
import csv
import time
cn = connect.Connecter()

listPage1 = cn.getFirstPage("https://tw.money.yahoo.com/fund/domestic")
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
}

for urls in listPage1:
    urllist = cn.getFileTag(urls)
    print(urllist)
    for tag in urllist:
        url = "https://tw.money.yahoo.com/fund/download/" + tag + "?startDate=1911-01-01&endDate=2016-07-22"
        
        dn = download.CsvDownloader(tag[:10]+".csv",url)
        time.sleep(0.5)
        dn.saver()
        # print(cn.getContent(url, headers))
        # print(url)
