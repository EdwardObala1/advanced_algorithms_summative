text = "Plain text"
import itertools

def encryption(text, key):
    matrix = [[] for i in range(key)] # o(n) time to generate each list
    counter = 0
    encryped_text = ''
    for i in range(0, len(text)): #o(n) time to add each encyption to  a list
        if counter < key:
            matrix[counter].append(text[i])
            counter += 1
        else:
            counter = 0
            matrix[counter].append(text[i])
            counter += 1
    encryped_text = ''.join(itertools.chain(*matrix))
    return encryped_text
    

def decryption(encypted, key):
    counter = 0
    decrypted = ''
    group_length = len(encypted) / key
    firstpointer = 0
    secondpointer = firstpointer + int(group_length)
    # if the length matches th
    if group_length % 1 == 0:
        for i in range(0, (int(group_length))):
            decrypted += encypted[firstpointer:secondpointer][i] + encypted[secondpointer:][i]
        return decrypted
    else:
        print(group_length)
        pass




print(encryption("Plain text", 2),' for str - Plain text')
print(encryption("Edward", 3),' for str - Edward')
print(encryption("Edwarde", 3),' for str - Edwarde')
print(encryption("Edwardel", 3),' for str - Edwardel')

print(decryption("Pantxli et", 2),' for str - Pantxli et')
print(decryption("Eaedrwd", 3),' for str - Edwarde')
print(decryption("Eaedrlwd", 3),' for str - Edwardel')