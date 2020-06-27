import requests
import pprint
import csv
# import pandas as pd
from bs4 import BeautifulSoup

class Bleague:
    page_url = 'https://www.bleague.jp/attendance/?year=2019'

    def parse(self):
        print(self.page_url)

        response = requests.get(self.page_url)
        if (response.status_code != 200):
            print("request error:" + url)
            return

        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup)

        file = open('src/bleague.csv', 'w')
        w = csv.writer(file)
        for i in soup.find_all(class_='data-content__blocks'):
            # print(i)
            # 節
            setu = i.find(class_='setu')

            # 日付
            date = i.find(class_='date')
            # チーム
            # 勝敗
            # スコア
            # 得点
            # 失点
            # ホームorアウェイ
            # 入場者
            # 会場
            # 集客率

            # csv書き込み
            w.writerow([setu, date])

        file.close()

        # output = pd.DataFrame(data=result, index=index)
        # print(output)

        # 日付を取得
        # number1 = 0
        # for i in soup.find_all(class_='centerarticle-entry-data'):
        #     date = i.find(class_='entry-contents-date').text.replace('/', '')
        #     result[number1] = {}
        #     result[number1]['date'] = date
        #     number1 += 1
        #
        # # タイトルとURLを取得
        # number2 = 0
        # for i in soup.find_all(class_='centerarticle-entry-title'):
        #     url = i.a.get("href")
        #     title = i.a.text
        #     result[number2]['title'] = title
        #     result[number2]['url'] = url
        #     number2 += 1
        #
        # # 画像を取得
        # number3 = 0
        # for i in soup.find_all(class_='centerarticle-entry-contents'):
        #     img = ''
        #     if i.img is not None:
        #         img = i.img.get("src")
        #
        #     result[number3]['img'] = img
        #     number3 += 1
        #
        # for data in result.values():
        #     # 複業(副業)ワードが入っていないものはスキップ
        #     if not FukugyouWord().isFukugyou(data['title']):
        #         continue
        #
        #     # 対象日でないものはスキップ
        #     if not data['date'] == self.checkDate:
        #         continue
        #
        #     # pprint.pprint(data)
        #     key = data['title']
        #     value = self.firebase.getValue(data['title'], data['url'], data['img'], data['date'], self.serviceName)
        #     print(value)
        #     print('----')
        #     self.firebase.set(key, value)


main = Bleague()
main.parse()
