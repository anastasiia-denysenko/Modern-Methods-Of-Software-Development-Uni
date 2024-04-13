import sys
from multiprocessing import Process
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = []
for i in range (len(upper)):
    lower.append((upper[i]).lower())
def ROT13(the_text):
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
print("Input: Hello world!")
print("Applying ROT13:", ROT13('Hello world!'))
print("Applying ROT13 for the second time:", ROT13(ROT13('Hello world!')))
def test():
    test_text = 'Hello world!'
    if ROT13(ROT13(test_text)) == test_text:
        return "correct"
        exit(0)
    else:
        return "incorrect"
        exit(1)
if test() == "incorrect":
    print("An error occured", file=sys.stderr)
if __name__ == '__main__':
    test_process = Process(target=test)
    test_process.start()
    test_process.join()
    code = test_process.exitcode
    print(f'Exit code: {code}')

