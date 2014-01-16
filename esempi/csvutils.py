#! python
# -*- coding: utf-8 -*-

import unicodecsv

def print_csv(results):
    from cStringIO import StringIO
    f = StringIO()
    csv = unicodecsv.writer(f, encoding='utf-8',delimiter=";")
    csv.writerow(results.values()[0].keys())
    for company,data in results.items():
        csv.writerow(data.values())
    print f.getvalue()

def write_csv_file(fname,content,delimiter=';'):
  try:
    with open(fname, 'wb') as csvfile:
        writer = unicodecsv.writer(csvfile, delimiter, encoding='utf-8')
        keys = content[0].keys()
        writer.writerow(keys)
        for element in content:          
          writer.writerow(element.values())
  except:
    raise
