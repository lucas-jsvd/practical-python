# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    """
    Parse a CSV file into a list of records.
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        # Read the file headers
        records = []
        headers = []
        indices = []
        if has_headers:
            headers = next(rows)
        if select and has_headers:
            indices = [headers.index(rotulo) for rotulo in select] 
            headers = [headers[indice] for indice in indices]
        for row in rows:
            if not row:  # Skip rows with no date
                continue
            if select and has_headers:
                row = [row[indice] for indice in indices]
            if types:
                row = [func(coluna) for func, coluna in zip(types, row)]
            if has_headers:
                records.append(dict(zip(headers, row)))
            else:
                records.append(tuple(row))

    return records
