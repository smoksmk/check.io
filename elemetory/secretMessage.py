def find_message(text):
    """Find a secret message"""

    result = ''
    data = [ch in text.upper() for ch in text]
    i = 0
    while i < len(text) <= 1000:
        if data[i] and text[i].isalpha():
            result += text[i]
        i+=1
    return result

if __name__ == '__main__':
    pass
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    # assert find_message("hello world!") == "", "Nothing"
    # assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
