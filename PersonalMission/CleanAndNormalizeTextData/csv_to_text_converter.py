import csv

# csv 파일을 읽어서 txt 파일로 저장하는 함수
def csv_to_txt(csv_filename, txt_filename):
    with open(csv_filename, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open(txt_filename, 'w', newline='', encoding='utf-8') as txt_file:
            txt_writer = csv.writer(txt_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                txt_writer.writerow(row)

csv_to_txt('netflix_titles.csv', 'raw_data.txt')
