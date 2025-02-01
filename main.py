def main():
    letters = {'a': 0, 'b': 0, 'c': 0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    def word_count(file):
        count = file.split()
        return(len(count))
    
    def letter_count(file):
        lower = file.lower()
        for word in lower:
            for letter in word:
                if letter in letters: 
                    letters[letter] += 1
    letter_count(file_contents)
    
    letter_list = []
    for char, count in letters.items():
        if char.isalpha():  # only include alphabet characters
            letter_list.append({"char": char, "num": count})
    def sort_on(dict):
        return dict["num"]
    letter_list.sort(reverse=True, key=sort_on)
   
   
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)} words found in the document")
    print("\n")
    for l in letter_list:
        print(f"the '{l["char"]}' character was found {l["num"]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
