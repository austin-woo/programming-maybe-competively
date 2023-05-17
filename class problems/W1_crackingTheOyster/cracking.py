
BITS_PER_WORD = 32  
BITS_PER_PHONE_NUM = 7 
MAX_PHONE_NUM = 9999999 
NUM_WORDS = (MAX_PHONE_NUM // BITS_PER_WORD) + 1  


bit_array = [0] * NUM_WORDS

with open('programming-maybe-competively\class problems\W1_crackingTheOyster\input.txt', 'r') as f:
    for line in f:
        phone_num = int(line.strip())
        word_index = phone_num // BITS_PER_WORD
        bit_index = phone_num % BITS_PER_WORD
        bit_array[word_index] |= (1 << bit_index)

with open('programming-maybe-competively\class problems\W1_crackingTheOyster\output.txt', 'w') as f:
    for i in range(MAX_PHONE_NUM + 1):
        word_index = i // BITS_PER_WORD
        bit_index = i % BITS_PER_WORD
        if bit_array[word_index] & (1 << bit_index):
            f.write(str(i).zfill(BITS_PER_PHONE_NUM) + '\n')
