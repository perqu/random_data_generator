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

col_vars = {
    'int': ['f', 't'],
    'float': ['f', 't', 'd'],
    'date': ['f', 't'],
    'email': ['l', 'd'],
    'phone': ['c']
}

#20[int]-f(10)-t(20)[float]-f(10)-t(20)-d(2)[date]-f(2023-03-06)-t(2024-03-05)[email]-l(7)-d(wp.pl)[phone]-c(poland)
