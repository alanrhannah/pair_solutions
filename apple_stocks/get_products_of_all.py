def get_products_of_all_ints_except_at_index(input_list):
    output = []
    for i in range(0, len(input_list)):
        temp_list = input_list
        import ipdb; ipdb.set_trace()
        del temp_list[i]
        output.append(reduce(lambda x, y: x*y, temp_list))

    return output

if __name__ == '__main__':
    foo = [6, 7, 8]
    print get_products_of_all_ints_except_at_index(foo)
