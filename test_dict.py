# Initialize global variable
current_index = 0

def get_dict_word():
    global current_index
    
    # Open the text file
    with open('dict.txt', 'r', encoding='utf-8') as file:
        # Read the lines from the file
        lines = file.read().splitlines()
        
        # If the list is empty, return None
        if not lines:
            return None
        
        # Initialize variables to store the current entry
        entry = []
        
        # Iterate through lines until a blank line is encountered
        while current_index < len(lines) and lines[current_index].strip():
            entry.append(lines[current_index].strip())
            current_index += 1
        
        # Join the lines to form the complete entry
        chosen_entry = '^$'.join(entry)
        
        # Skip the blank line for the next function call
        current_index += 1
        
        return chosen_entry

# Example usage:
for _ in range(100):
    x=input()
    print(get_dict_word())

