import csv 

def anagrams(word):
    match = sorted(word)
    matches = []

    with open('word_list.csv', 'rb') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if match == sorted(''.join(row)) and ''.join(row) != word:
                matches.append(''.join(row))

        word_and_matches = 'Word: {} | Anagrams: {}'.format(
            word, ', '.join(matches))

        return word_and_matches

if __name__ == "__main__":

    print anagrams('train')
    print '--'
    print anagrams('drive')
    print '--'
    print anagrams('python')
    print '---'
    print anagrams('parse')
