def thousands_with_commas(i):
    list_of_comps = []
    str_num = str(i)
    rev_str_num = str_num[::-1]

    for i, digit in enumerate(rev_str_num):
      if (i % 3 == 0) and (i != 0):
        digit = ','+ digit
      list_of_comps.append(digit)
    
    with_commas = ''.join(list_of_comps)[::-1]
    return with_commas

if __name__ == '__main__':

    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789'
    assert thousands_with_commas(12) == '12'
