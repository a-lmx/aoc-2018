import sys

def find_hamming_distance_letters(word1, word2):
    diff_letters = set()
    word1 = word1.strip()
    word2 = word2.strip()
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_letters.add(word1[i])
    return len(diff_letters), diff_letters


def find_minimal_pair(filename):
    ids = list(open(filename))

    for i, box_id in enumerate(ids):
        for j in range(i+1, len(ids)):
            ham, letters = find_hamming_distance_letters(box_id, ids[j])
            if ham == 1:
                print('minimal pair: ', box_id, ids[j])
                different_letter = letters.pop()
                id_as_list = list(box_id)
                id_as_list.remove(different_letter)
                stripped_word = ''.join(id_as_list)
                print(f'shared chars: {stripped_word}')
                return
                    

find_minimal_pair(sys.argv[1])
