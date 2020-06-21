# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    """
    Parse a CSV file into a list of records.
    """
    if type(filename) == str:
        raise ValueError("Você deve passar um objeto interavel, não um nome de arquivo.")
    rows = csv.reader(filename, delimiter=delimiter)
    # Read the file headers
    records = []
    headers = []
    indices = []
    if has_headers:
        headers = next(rows)
    if select and has_headers:
        indices = [headers.index(rotulo) for rotulo in select] 
        headers = [headers[indice] for indice in indices]
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    for n_row, row in enumerate(rows, start=1):
        if not row:  # Skip rows with no date
            continue
        try:
            if select and has_headers:
                row = [row[indice] for indice in indices]
            if types:
                row = [func(coluna) for func, coluna in zip(types, row)]
            if has_headers:
                records.append(dict(zip(headers, row)))
            else:
                records.append(tuple(row))
        except ValueError as erro:
            if silence_errors:
                continue
            print(f"Row {n_row}: Couldn't convert {row}")
            print(f"Row {n_row}: {erro}")
    return records
