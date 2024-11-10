def word_count(text):
    return len(text.split())

def character_count(text):
    return len(text)

def sentence_count(text):
    sentences = text.replace('!', '.').replace('?', '.').split('.')
    return len([s for s in sentences if s.strip()])

def paragraph_count(text):
    paragraphs = text.split('\n\n')
    return len([p for p in paragraphs if p.strip()])

def main():
    print("\nWelcome to the Text Master Tool!")
    
    while True:
        print("\nChoose an option:")
        print("1. Word Count")
        print("2. Character Count")
        print("3. Sentence Count")
        print("4. Paragraph Count")
        print("5. All Counts")
        print("0. Exit")
        
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from the menu.")
            continue

        if option == 0:
            print("Thank you for using the Text Master Tool!")
            break
        
        if option in [1, 2, 3, 4, 5]:
            text = input("\nEnter your text:\n")
            
            if option == 1:
                result = f"Word Count: {word_count(text)}"
            elif option == 2:
                result = f"Character Count: {character_count(text)}"
            elif option == 3:
                result = f"Sentence Count: {sentence_count(text)}"
            elif option == 4:
                result = f"Paragraph Count: {paragraph_count(text)}"
            elif option == 5:
                result = (
                    f"Word Count: {word_count(text)}\n"
                    f"Character Count: {character_count(text)}\n"
                    f"Sentence Count: {sentence_count(text)}\n"
                    f"Paragraph Count: {paragraph_count(text)}"
                )
            
            print("\n" + "-"*50)
            print(result)
            print("-"*50)

        else:
            print("Invalid option. Please try again.")
main()
