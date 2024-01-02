import csv,random



def get_dict_word():
    # Open the CSV file
    with open('dict.csv', 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Skip the header if it exists
        next(csv_reader, None)
        
        # Create a list to store words and weights
        words_and_weights = []
        
        # Read each row and store the word and weight in the list
        for row in csv_reader:
            word, weight = row
            words_and_weights.append((word, int(weight)))
        
        # Choose a random word based on weights
        chosen_word = random.choices(words_and_weights, weights=[w[1] for w in words_and_weights])[0][0]
        
        return chosen_word

    

for i in range(1,200):
    print(get_dict_word())

    
    
    
    
    
    
