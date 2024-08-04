def main():
    while True:
        words = input('Enter the words to create an abbreviation (or type "exit" to quit): ').split()

        if words[0].lower() == 'exit':
            break

        abbreviation = ''.join(word[0] for word in words).upper()
        print(f'The abbreviation is: {abbreviation}\n')


if __name__ == '__main__':
    main()