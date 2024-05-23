import sys
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = []
for i in range (len(upper)):
    lower.append((upper[i]).lower())
class ROT_13:
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
def otput_rot13(s:str):
    m = ROT_13()
    if (m.ROT13(m.ROT13(s))) == s:
        sys.stderr.write("Starting process...\n")
        sys.stdout.write("The output is: ")
        sys.stdout.write(m.ROT13(s))
        sys.exit(0)
    else:
        sys.stderr.write("Process terminated: function does not work.")
        sys.exit(1)
