import sys
from multiprocessing import Process
import io
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
input = 'Hello world!'
in_stream = io.BytesIO(input.encode('utf-8'))
sys.stdin = io.TextIOWrapper(in_stream, encoding='utf-8')
def test():
    if ROT13(ROT13(input)) == input:
        return "correct"
        exit(0)
    else:
        return "incorrect"
        exit(1)
def stdout_stderr():
    if test() == "correct":
        temp = sys.stdout                        
        sys.stdout = open('ouput.txt', 'w')
        print(ROT13(input))
        print(ROT13(ROT13(input)))
        sys.stdout.close()
        sys.stdout = temp
    else:
        sys.stderr.write(f"The function does not work\n")
stdout_stderr()
if __name__ == '__main__':
    test_process = Process(target=test)
    test_process.start()
    test_process.join()
    code = test_process.exitcode
    print(f'Exit code: {code}')

