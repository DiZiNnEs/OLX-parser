class Urls:
    def __init__(self):
        pass

    def __str__(self):
        ...

    def __copy__(self):
        a = 5

    def return_urls(self):
        last = ...
        with open('urls_opened.txt', 'r') as read_file:
            last = read_file.read()


        print(last)

        with open('urls_opened.txt', 'w') as file:
            last += last
            file.write(last)

        with open('urls_opened.txt', 'r') as read_file_:
            last2 = read_file_.read()
            print(last2)



test = Urls()
test.return_urls()