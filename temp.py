with open('/Users/ija/Desktop/ucu1/op/week7/exmpl.txt', 'r', encoding='utf-8') as file:
    # content = file.read(5)
    # # lstrip() or rstrip()
    # print(repr(content))
    # content = file.read(8)
    # print(repr(content))
    # # курсор рухається
    # content = file.readline()
    # print(repr(content))
    # content = file.readline(5)
    # print(repr(content))
    for line in file:
        print(repr(line))