from bs4 import BeautifulSoup
import csv

with open('PHHCTH243201473_106_20240813T045153+0700.html', 'r') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')

tables = soup.find_all('table')


csv_file = 'output.csv'

with open(csv_file, 'w', newline= '', encoding='utf-8')as file:
    writer = csv.writer(file)
    for table in tables:
        headers = []
        data = []
        rows = table.find_all('tr')  

        if rows:
            header_row = rows[0]
            headers = [th.text.strip() for th in rows[0].find_all('th')] 
            

            if not headers : 
                headers = [td.text.strip() for td in rows[0].find_all('td')]

            if headers:
                writer.writerow(headers)
            
            for row in rows[1:]:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                if cols:
                    writer.writerow(cols)

print(f'Data has been written to {csv_file}')
