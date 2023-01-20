import wikipedia


def main():
    search_title = input("Enter a phrase: ")
    while search_title != "":
        try:
            result = wikipedia.page(search_title, auto_suggest=False)
            if result:
                print("Title:", result.title)
                print("Summary:", result.summary)
                print("Url:", result.url)
        except Exception:
            print("Disambiguation Page")
        search_title = input("Enter a phrase: ")


main()
