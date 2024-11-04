import urllib.request

def read_input_file(url: str, number: int) -> list[list[str]]:
    """
    Preconditions: 0 <= number <= 77
    
    Return list of strings lists from url

    >>> read_input_file('https://rb.gy/97llc',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://rb.gy/97llc',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], \
['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    with urllib.request.urlopen(url) as file:
        for _ in range(2): #skipping first two lines
            file.readline()

        students = []
        while len(students) < number:
            line = file.readline().decode("utf-8")
            info = line.strip().split("\t")[:4]
            info[2] = "+" if info[2] == "До наказу" else "-"
            for _ in range(2): 
                file.readline()
            line = file.readline().decode("utf-8")
            info.append(line.strip().split("\t")[-1])
            students.append(info)

            while line[0] != "–":
                line = file.readline().decode("utf-8")
        return students
        


def write_csv_file(url: str):
    '''write info to csv file with the path total.csv'''
    pass

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())