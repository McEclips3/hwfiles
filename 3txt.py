from pprint import pprint
with open('1.txt', 'rt', encoding='utf-8') as one:
    text_one = one.readlines()
    one_len = f'{str(len(text_one))}\n'
    one_name = f'{one.name}\n'
    text_one.insert(0, one_name)
    text_one.insert(1, one_len)
    text_one.append('\n')


with open('2.txt', 'rt', encoding='utf-8') as two:
    text_two = two.readlines()
    two_len = f'{str(len(text_two))}\n'
    two_name = f'{two.name}\n'
    text_two.insert(0, two_name)
    text_two.insert(1, two_len)
    text_two.append('\n')


with open('3.txt', 'rt', encoding='utf-8') as three:
    text_three = three.readlines()
    three_len = f'{str(len(text_three))}\n'
    three_name = f'{three.name}\n'
    text_three.insert(0, three_name)
    text_three.insert(1, three_len)
    text_three.append('\n')

text = []
text.append(text_one)
text.append(text_two)
text.append(text_three)
text.sort(key=len)

with open('fulltext.txt', 'w', encoding='utf-8') as full:
    for ind, textt in enumerate(text):
        full.writelines(text[ind])

pprint(text)
