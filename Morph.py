import time
import os

def morph_text(text1, text2, delay=0.1):
    max_len = max(len(text1), len(text2))
    text1 = text1.ljust(max_len)
    text2 = text2.ljust(max_len)

    current = list(text1)

    for i in range(max_len):
        for j in range(max_len):
            if j <= i:
                current[j] = text2[j]
        print("".join(current), end="\r")
        time.sleep(delay)

    print("".join(current))


# Example
morph_text("Hello World", "Python Rocks!", 0.2)
