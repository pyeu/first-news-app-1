import csv


def get_la_riot_deaths():
    csv_path = './static/data/la-riots-deaths.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list
