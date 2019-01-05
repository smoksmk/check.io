def checkio(text):
    text = text.lower()
    data = {}
    # data = {i: text.count(i) for i in text}
    for i in text:
        if i.isalpha():
            data.update({i: text.count(i)})
    data = sorted(data.items(), key=lambda x: x[0])
    res = max(data, key= lambda x: x[1])
    #replace this for solution
    return res[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
