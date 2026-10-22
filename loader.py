import csv
from card import Card


def load_data(file_path):
    with open(file_path, encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        word_list = []
        for row in reader:
            card = Card(
                row['english'].strip(), row['hungarian'].strip(), row['tag'].strip()
            )
            word_list.append(card)

        return word_list
