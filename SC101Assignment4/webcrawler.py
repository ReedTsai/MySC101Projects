"""
File: webcrawler.py
Name: DK
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tbody = soup.find("tbody")
        male_number = 0
        female_number = 0
        for line in tbody:
            if len(line.text.split(" ")) == 4:
                male_number_str = str(line.text.split(" ")[1])  # 每列的第二個element是男生的數量
                female_number_str = str(line.text.split(" ")[3])  # 每列的第四個element是女生的數量
                male_number += int("".join(male_number_str.split(",")))  # 把逗號移除後重新合併轉成int
                female_number += int("".join(female_number_str.split(",")))  # 把逗號移除後重新合併轉成int
        print(f"Male Number: {male_number}")
        print(f"Female Number: {female_number}")


if __name__ == '__main__':
    main()
