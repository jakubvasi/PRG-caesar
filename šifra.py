abc = "abcdefghijklmnopqrstuvwxyz"

text = "IVKJXVOFPWTGVDIAJMHVXZOVDIAJMHVXZWTGJPWJCVOVDIAJMHVXZWTGVWPCOJWTGJIVKJXVOFPPWJCVQNZXCIJKJQNOVGJNFMUZIDVWZUIDIZKJQNOVGJIDXXJEZNOQIDWTGUDQJOVUDQJOWTGNQZOGJGDYDOJNQZOGJQZOHZNQDODVOHVEZIZKJCGODGVJYWJCVWTGKJNGVIXGJQZFEHZIZHEVIOZIKMDNZGKMJOJVWTQTYVGNQZYZXOQDJOJHNQZOGZVWTQNDXCIDPQZMDGDNFMUZIZCJEVINVHIZWTGODHNQZOGZHVGZKMDNZGVWTJOJHNQZOGZQTYVGNQZYZXOQDWTGJOPKMVQZNQZOGJFOZMZJNQZXPEZFVUYZCJXGJQZFVOJKMDXCVUZGJYJNQZOVIVNQZOZWTGNQZONFMUZIZEKJQNOVGVGZNQZOCJIZKJUIVGKMDNZGYJNQZCJQGVNOIDCJVGZEZCJQGVNOIDCJIZKMDEVGDOZHKVFFOZMDCJKMDEVGDVQZMDQEZCJEHZIJYVGHJXNOVONZWJUDHDYZOHD"
text = text.lower()

def code(text, index):
    global abc
    coded = []
    
    for char in text:
        position = abc.index(char)
        char = abc[(position + index)%len(abc)]
        coded.append(char)
        
    coded = "".join(coded)
    return coded

def decode(text, index):
    global abc
    decoded = []
    
    for char in text:
        position = abc.index(char)
        char = abc[(position - index)%len(abc)]
        decoded.append(char)
    
    decoded = "".join(decoded)    
    return decoded
    
for index in range(len(abc)):
    print(decode(text, index))
    print()

