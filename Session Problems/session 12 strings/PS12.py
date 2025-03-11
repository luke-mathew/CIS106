"""
String Processing Programs

1. Name Formatting: Converts 'Firstname Lastname' to 'Lastname, F.'
2. Reverse Text with Trimmed Spaces
3. Parse and Print Comma-Separated Values
4. Text Scrolling Animation

Author: [Your Name]
References: [Any resources used]
"""

def get_input(prompt):
    """Gets user input with a given prompt."""
    return input(prompt).strip()

def format_name(name):
    """Formats a name from 'Firstname Lastname' to 'Lastname, F.'"""
    parts = name.split()
    if len(parts) != 2:
        return "Invalid input. Please enter 'Firstname Lastname'."
    return f"{parts[1]}, {parts[0][0].upper()}."

def clean_and_reverse(text):
    """Removes extra spaces and reverses the text."""
    words = text.split()
    return " ".join(words)[::-1]

def parse_csv(line):
    """Parses a comma-separated line and prints each item on a new line."""
    items = [item.strip() for item in line.split(",")]
    return "\n".join(items)

def scroll_text(text, width, lines, direction):
    """Scrolls text left or right as per the given number of lines."""
    text = (text + " ") * ((width // len(text)) + 1)
    output = []
    for _ in range(lines):
        output.append(text[:width])
        text = text[1:] + text[0] if direction == "left" else text[-1] + text[:-1]
    return "\n".join(output)

def main():
    """Main function to execute all tasks."""
    # Task 1: Name Formatting
    name = get_input("Enter 'Firstname Lastname': ")
    print(format_name(name))
    
    # Task 2: Reverse Text
    text = get_input("Enter a line of text: ")
    print(clean_and_reverse(text))
    
    # Task 3: CSV Parsing
    csv_text = get_input("Enter comma-separated values: ")
    print(parse_csv(csv_text))
    
    # Task 4: Scrolling Text
    scroll_text_input = get_input("Enter a line of text: ")
    width = int(get_input("Enter the number of characters per line: "))
    lines = int(get_input("Enter the number of lines to print: "))
    direction = get_input("Enter scroll direction (left/right): ").lower()
    if direction not in ["left", "right"]:
        print("Invalid direction. Use 'left' or 'right'.")
    else:
        print(scroll_text(scroll_text_input, width, lines, direction))

if __name__ == "__main__":
    main()
