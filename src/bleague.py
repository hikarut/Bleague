import requests
import pprint
import csv
# import pandas as pd
from bs4 import BeautifulSoup

class Bleague:
    # page_url = 'https://www.bleague.jp/attendance/?year=2019'
    # B1
    page_url = 'https://www.bleague.jp/attendance/?tab=1&year=2019&club=&event=2&setuFrom=1&setuTo=36'
    # B2
    # page_url = 'https://www.bleague.jp/attendance/?tab=2&year=2019&club=&event=7&setuFrom=1&setuTo=36'
    arena_max = {
        '横アリ': 17000,
        'CNA': 4556,
        '立川立飛': 3000,
        '青山学院': 2500,
        '松江総体': 4700,
        'ハンアリ': 5000,
        '富山市総': 4650,
        '沖縄市': 3200,
        '北海きた': 8000,
        'とどろき': 6500,
        '横浜文体': 5000,
        'YMIT': 3500,
        'WA刈谷': 2400,
        'ドルアリ': 7515,
        'おおきに': 7056,
        'アオーレ': 5100,
        '横浜国プ': 11000,
        '大阪府立': 8000,
        '船橋': 4368,
        '墨田区': 6000,
        '豊橋': 2011,
        'ブレアリ': 2900,
        '浜松': 8000,
        'ウカル': 4896,
        '福知山': 8000,
        '富山西部': 2628,
        'RP上越': 1504,
        'カミアリ': 3552,
        '北ガス': 2504,
        '県北': 2000,
        '鹿島総体': 2000,
        '島津': 8000,
        '島根県立': 2000,
        '駒沢': 3474,
        '千葉': 7512,
        '秋田県体': 6000,
        'トッ平総': 800,
        '住吉SC': 3500,
        '能代総体': 2000,
        '守山市民': 3000,
        '豊見城': 2100,
        '東総合': 3120,
        'SH豊田': 6500,
    }

    def parse(self):
        print(self.page_url)

        response = requests.get(self.page_url)
        if (response.status_code != 200):
            print("request error:" + self.page_url)
            return

        soup = BeautifulSoup(response.text, "html.parser")

        file = open('src/b1.csv', 'w')
        w = csv.writer(file)
        # ヘッダー
        w.writerow([
            'setu',
            'date',
            'home_team',
            'home_victory',
            'home_score',
            'away_team',
            'away_score',
            'home_away',
            'attendance',
            'arena',
            'arena_rate',
        ])

        for i in soup.find_all(class_='data-content__blocks'):
            # 節
            setu = i.find(class_='setu').text

            # 日付
            date = i.find(class_='date').text

            # チーム
            teams = i.find_all(class_='team')
            home_team = teams[0].text
            away_team = teams[1].text

            # スコア
            score = i.find(class_='score').text
            split_score = score.split('-')
            home_score = split_score[0].replace(' ', '')
            away_score = split_score[1].replace(' ', '')

            # 勝敗(※引き分けはなし)
            home_victory = 'win' if home_score > away_score else 'lose'
            away_victory = 'win' if away_score > home_score else 'lose'

            # 入場者
            attendance = i.find(class_='attendance').text

            # 会場
            arena = i.find(class_='arena').text

            # 集客率
            arena_max_count = self.arena_max[arena]
            arena_rate = round((int(attendance) / arena_max_count) * 100)

            # csv書き込み
            # ホームチーム
            w.writerow([
                setu,
                date,
                home_team,
                home_victory,
                home_score,
                away_team,
                away_score,
                'home',
                attendance,
                arena,
                arena_rate,
            ])
            # アウェイチーム
            w.writerow([
                setu,
                date,
                away_team,
                away_victory,
                away_score,
                home_team,
                home_score,
                'away',
                attendance,
                arena,
                arena_rate,
            ])

        file.close()

main = Bleague()
main.parse()
