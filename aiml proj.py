import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load('en_core_web_sm')

# Define a function to process natural language and calculate the result
def ai_calculator(text):
    # Process the text
    doc = nlp(text)
    
    # Variables to store numbers and the operation
    numbers = []  # List to store multiple numbers
    operation = None
    
    # Iterate over tokens to find numbers and the operation
    for token in doc:
        if token.like_num:  # Check if the token is a number
            numbers.append(token.text)  # Append number to the list
        
        # Check for keywords for operations
        if token.text.lower() in ['add', 'plus']:
            operation = 'add'
        elif token.text.lower() in ['subtract', 'minus']:
            operation = 'subtract'
        elif token.text.lower() in ['multiply', 'times']:
            operation = 'multiply'
        elif token.text.lower() in ['divide', 'by']:
            operation = 'divide'
        elif token.text.lower() in ['circumfix', 'circum', 'concatenate']:
            operation = 'circumfix'
    
    # Perform the operation
    if numbers and operation:
        if operation == 'add':
            return sum(float(num) for num in numbers)
        elif operation == 'subtract':
            result = float(numbers[0])
            for num in numbers[1:]:
                result -= float(num)
            return result
        elif operation == 'multiply':
            result = 1
            for num in numbers:
                result *= float(num)
            return result
        elif operation == 'divide':
            result = float(numbers[0])
            for num in numbers[1:]:
                if float(num) == 0:
                    return "Error: Division by zero."
                result /= float(num)
            return result
        elif operation == 'circumfix':
            return ''.join(numbers)  # Concatenate as strings
    else:
        return "Error: Could not understand the input."

# Example usage
while True:
    query = input("Enter a math expression (or type 'exit' to quit): ")
    if query.lower() == 'exit':
        break
    result = ai_calculator(query)
    print(f"Result: {result}")
