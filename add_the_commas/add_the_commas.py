def add_the_commas(i):
    splits = []
    list_number = list(str(i))

    first_split_index = len(list_number) % 3
    if not first_split_index:
        first_split_index = 3

    first_split = ''.join(list_number[:first_split_index])
    splits.append(first_split)

    for n in range(0, len(list_number[first_split_index:]), 3):
        additional_splits = ''.join(list_number[first_split_index:][n:n+3])
        splits.append(additional_splits)

    i = ','.join(splits)

    return str(i)

if __name__ == '__main__':

    assert add_the_commas(1234) == '1,234'
    assert add_the_commas(123456789) == '123,456,789'
    assert add_the_commas(12) == '12'
