from functools import lru_cache
import csv


@lru_cache
# the easy way
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return [dict for dict in jobs_reader]

# the hard way
# def read(path):
#     result = []
#     with open(path) as file:
#         jobs_reader = csv.reader(file, delimiter=",", quotechar='"')
#         header, *data = jobs_reader
#         rows = [row for row in data]
#         for row in rows:
#             dict_to_append = {}
#             for index, row_data in enumerate(row):
#                 dict_to_append[header[index]] = row_data
#             result.append(dict_to_append)
#     return result
