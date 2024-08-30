import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

def parse_query(query):
    """
    Parse the user's query to extract important components and intent.

    Parameters:
    query (str): The user's query as a string.

    Returns:
    dict: A dictionary containing extracted actions (verbs), entities, and tokens.
    """
    doc = nlp(query)
    
    # Extract verbs (actions) from the query, focusing on more relevant actions
    actions = [token.lemma_ for token in doc if token.pos_ == "VERB" and token.lemma_ not in ["need", "want", "help", "be", "tell"]]
    
    # Extract named entities (like programming languages, specific objects)
    entities = [ent.text for ent in doc.ents]
    
    # Extract all tokens (individual words or symbols)
    tokens = [token.text for token in doc]
    
    # Determine the primary intent if the statement is very general
    if not actions and not entities:
        if "explain" in tokens or "describe" in tokens:
            actions.append("explain")
        elif "create" in tokens or "generate" in tokens:
            actions.append("create")
        else:
            actions.append("discuss")
    
    return {
        "actions": actions,
        "entities": entities,
        "tokens": tokens
    }


# Example usage:
if __name__ == "__main__":
    # Example query
    query = "I need help writing a Python function to sort a list of dictionaries by a specific key."
    
    # Parse the query
    parsed_query = parse_query(query)
    
    # Output the parsed components
    print("Actions:", parsed_query["actions"])
    print("Entities:", parsed_query["entities"])
    print("Tokens:", parsed_query["tokens"])
