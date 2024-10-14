def count_words_in_file(filename):
    # Open the specified file in read mode
    with open(filename, 'r') as file:
        # Read the entire content of the file
        content = file.read()
        # Split the content into words based on whitespace and store in a list
        words = content.split()
        # Return the number of words in the list
        return len(words)

# Prompt the user to enter the filename
filename = input("Enter file name: ")
try:
    # Call the function to count words and store the result
    word_count = count_words_in_file(filename)
    # Print the total word count
    print(f"Number of words in {filename}: {word_count}")
except FileNotFoundError:
    # Handle the case where the file does not exist
    print(f"File {filename} not found!")
