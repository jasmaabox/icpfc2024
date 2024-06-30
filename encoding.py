
def decode_integer(encoded_text: str) -> int:
    if len(encoded_text) > 0 and encoded_text[0] == "I":
        digits = [ord(c) - ord("!") for c in encoded_text[1:]]
        acc = 0
        m = 1
        for d in digits[::-1]:
            acc += m * d
            m *= 94
        return acc
    else:
        raise Exception("not a valid integer")


def encode_integer(value: int) -> str:
    v = value
    digits = []
    while v >= 94:
        digits.append(v % 94)
        v = v // 94
    digits.append(v)
    encoded_content = "".join([chr(d + ord("!")) for d in digits[::-1]])
    return f"I{encoded_content}"


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`|~ \n"
char2idx = {}
for i, c in enumerate(chars):
    char2idx[c] = i


def decode_string(encoded_text: str) -> str:
    if len(encoded_text) > 0 and encoded_text[0] == "S":
        return "".join([chars[ord(c) - ord("!")] for c in encoded_text[1:]])
    else:
        raise Exception("not a valid string")


def encode_string(text: str) -> str:
    encoded_content = "".join([chr(char2idx[c] + ord("!")) for c in text])
    return f"S{encoded_content}"
