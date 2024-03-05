import csv

def read_phones(file_path):
    phone_lengths = {}
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            country = row['country'].lower()
            max_length = int(row['phoneNumberLengthByCountry_phLengthMax'])
            phone_lengths[country] = max_length
    return phone_lengths

phones = read_phones("data/phones.csv")
