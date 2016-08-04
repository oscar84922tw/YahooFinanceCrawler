import requests
import csv
import os


class CsvDownloader:
    def __init__(self, fileName, url):
        self.fileName = fileName
        self.url = url

    def download(self):
        return requests.get(self.url)

    def saver(self):
        with open(self.fileName, 'w') as temp_file:
            temp_file.writelines(self.download().content)

        # with open(self.fileName, 'rU') as temp_file:
        #     csv_reader = csv.reader(temp_file, dialect=csv.excel_tab)
        #     for line in csv_reader:
        #         print(line)
        print("============= " + self.fileName + "is done =============")
