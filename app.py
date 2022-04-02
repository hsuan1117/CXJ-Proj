from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    import csv
    reader = csv.reader(open('data/data.csv', 'r',encoding="utf-8"))
    for i, line in enumerate(reader):
        print(i)
        # i == 0: title
        # i == 1: 小標 (台北、台中、新北....)
        # i == 2 開始資料
        # line[0]: 年分
        # line[1]: 開始資料
        # line[2~n]: 每個小標的資料
        print(line[1])

        # 剩下加油


if __name__ == '__main__':
    app.run()
