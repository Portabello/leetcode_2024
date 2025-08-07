import random
import string
class Solution:

    def encode(self, strs: List[str]) -> str:

        self.encoding = {}
        alphabet = []
        for s in strs:
            for c in s:
                if c not in alphabet:
                    alphabet.append(c)

        while len(alphabet)>0:
            randint = random.randint(1000,9999)
            if randint not in self.encoding:
                self.encoding[randint] = alphabet[0]
                alphabet.pop(0)

        encoded_string = ""
        for s in strs:
            encoded_string = encoded_string + '#'
            for c in s:
                for x in self.encoding:
                    if self.encoding[x] == c:
                        encoded_string = encoded_string + str(x)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strings = s.split('#')
        strings.pop(0)
        decoded_strings = []
        for s in strings:
            decoded_string = ""
            for i in range(len(s)//4):
                print(s[i*4:(i*4)+4])
                decoded_string = decoded_string + self.encoding[int(s[i*4:(i*4)+4])]
            decoded_strings.append(decoded_string)
        return decoded_strings
