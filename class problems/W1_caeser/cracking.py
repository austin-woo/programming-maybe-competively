ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def decode(input_file):
    with open(input_file, 'r') as f:
        # read M and N
        M, N = map(int, f.readline().strip().split())
        
        # read the dictionary
        dictionary = set()
        for _ in range(M):
            dictionary.add(f.readline().strip().lower())
        
        # read the cipher text and decode it
        for _ in range(N):
            cipher_text = f.readline().strip().lower()
            for shift in range(26):
                decoded_message = ''
                for letter in cipher_text:
                    if letter in ALPHABET:
                        index = (ALPHABET.index(letter) - shift) % 26
                        decoded_message += ALPHABET[index]

                    else:
                        decoded_message += letter
                words = decoded_message.split()
                if all(word in dictionary for word in words):
                    print(decoded_message)
decode('programming-maybe-competively\class problems\W1_caeser\dictionary.txt')