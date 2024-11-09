def word_count(text):
    return len(text.split())

def character_count(text):
    return sum(1 for char in text if char != ' ')

def sentence_count(text):
    # Split by common sentence-ending punctuation and filter out empty strings
    sentences = text.replace('!', '.').replace('?', '.').split('.')
    return len([s for s in sentences if s.strip()])

def paragraph_count(text):
    paragraphs = text.split('\n\n')
    return len([p for p in paragraphs if p.strip()])

def main():
    print("Welcome to the Text Master CLI Tool!")
    print("Choose an option:")
    print("1. Word Count")
    print("2. Character Count")
    print("3. Sentence Count")
    print("4. Paragraph Count")
    print("5. All Counts")
    print("0. Exit")
    
    while True:
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from the menu.")
            continue

        if option == 0:
            print("Thank you for using the Text Master CLI Tool!")
            break
        
        if option in [1, 2, 3, 4, 5]:
            text = input("\nEnter your text (any characters or numbers are allowed):\n")
            
            if option == 1:
                result = f"Word Count: {word_count(text)}"
            elif option == 2:
                result = f"Character Count (excluding spaces): {character_count(text)}"
            elif option == 3:
                result = f"Sentence Count: {sentence_count(text)}"
            elif option == 4:
                result = f"Paragraph Count: {paragraph_count(text)}"
            elif option == 5:
                result = (
                    f"Word Count: {word_count(text)}\n"
                    f"Character Count (excluding spaces): {character_count(text)}\n"
                    f"Sentence Count: {sentence_count(text)}\n"
                    f"Paragraph Count: {paragraph_count(text)}"
                )
            print("\n" + "-"*50)
            print(result)
            print("-"*50)

        else:
            print("Invalid option. Please try again.")

        print("\nChoose another option or enter 0 to exit:")
main()