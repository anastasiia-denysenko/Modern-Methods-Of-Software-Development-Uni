upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = []
for i in range (len(upper)):
    lower.append((upper[i]).lower())
class ROT_13:
    def get_text(self):
       return self.the_text
    def get_name(self):
        self.name = input('Hello world!')
    def ROT13(self, the_text):
        encoded = ''
        for i in the_text:
            for j in range (26):
                if i == upper[j]:
                    if j+13<=26:
                        encoded+=str(upper[j+13])
                    if j+13>26:
                        encoded+=str(upper[j+13-26])
                if i == lower[j]:
                    if j+13<=26:
                        encoded+=str(lower[j+13])
                    if j+13>26:
                        encoded+=str(lower[j+13-26])
            if (i not in upper)&(i not in lower):
                encoded+=str(i)
        return encoded
