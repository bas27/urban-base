def all_variants(text):

    for k in range(1, len(text)+1):
        for j in range(len(text)):
            if j + k <= len(text):
                yield text[j:j + k]

a = all_variants("abc")
for i in a:
    print(i)
