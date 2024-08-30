from query_parser import parse_query
from prompt_generator import classify_query, generate_prompt

def main():
    # Define a list of general test queries
    queries = [
        "Tell me about Python.",
        "I need help with functions.",
        "Explain sorting algorithms.",
        "Create a tutorial on loops.",
        "Discuss modern AI techniques."
    ]
    
    # Process each query
    for query in queries:
        print(f"\nOriginal Query: {query}")
        
        # Parse the query
        parsed_query = parse_query(query)
        
        # Classify the query
        classification = classify_query(parsed_query)
        
        # Generate the prompt based on classification
        prompt = generate_prompt(classification, parsed_query)
        
        # Output the generated prompt
        print("Generated Prompt:", prompt)

if __name__ == "__main__":
    main()
