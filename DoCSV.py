#coding=utf-8
import csv
import requests

class getMP3:
    def __init__(self, param_word):
        self.query_word = param_word

    def get_and_save(self):
        # 访问百度翻译接口
        url = "http://tts.baidu.com/text2audio"
        header = {
            "Host": "tts.baidu.com",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch"
        }

        query = {
            "lan": "en",
            "pid": "101",
            "ie": "UTF-8",
            "text": word,
            "spd": 2
        }
        audio = requests.get(url, params=query, headers=header)
        with open('./words/' + self.query_word + '.mp3', 'wb') as f:
            f.write(audio.content)
        print self.query_word+" has been saved"


#读取CSV文件信息
csvReader = csv.reader(open('YourLife3000.csv', 'rU'))
for row in csvReader:
    word = row[0]
    word_object = getMP3(word)
    word_object.get_and_save()


