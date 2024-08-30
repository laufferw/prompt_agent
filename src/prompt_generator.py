# Define prompt templates for different query types
TEMPLATES = {
    "technical": "Write a {language} function that {action}.",
    "informational": "What is {topic}?",
    "creative": "Generate a {type} based on {context}.",
    "general": "Please provide more details about {topic}."
}

def classify_query(parsed_query):
    """
    Classifies the query based on its parsed components.

    Parameters:
    parsed_query (dict): The parsed query containing actions, entities, and tokens.

    Returns:
    str: The category of the query (e.g., 'technical', 'informational', 'creative').
    """
    # Simple classification based on the presence of certain keywords
    if "function" in parsed_query["tokens"] or "code" in parsed_query["tokens"]:
        return "technical"
    elif "help" in parsed_query["tokens"] or "explain" in parsed_query["tokens"]:
        return "informational"
    elif "generate" in parsed_query["actions"] or "create" in parsed_query["actions"]:
        return "creative"
    else:
        return "general"

TEMPLATES = {
    "technical": "Write a {language} function that {action}.",
    "informational": "What is {topic}?",
    "creative": "Generate a {type} based on {context}.",
    "general": "Please provide more details about {topic}.",
    "explain": "Explain {topic} in detail.",
    "discuss": "Discuss {topic} with examples.",
    "create": "Create a comprehensive guide on {topic}."
}

def generate_prompt(classification, parsed_query):
    """
    Generates a prompt based on the query classification and parsed data.

    Parameters:
    classification (str): The classification of the query.
    parsed_query (dict): The parsed query containing actions, entities, and tokens.

    Returns:
    str: A formatted prompt string.
    """
    action = parsed_query["actions"][0] if parsed_query["actions"] else "discuss"
    topic = parsed_query["entities"][0] if parsed_query["entities"] else "the topic"

    if classification == "creative":
        # Provide default values if 'type' or 'context' are not available
        type_of_content = "piece of content"  # Default type if not specified
        context = "relevant information"      # Default context if not specified
        return TEMPLATES[classification].format(type=type_of_content, context=context)
    
    if classification in TEMPLATES:
        return TEMPLATES[classification].format(action=action, topic=topic)
    elif action in TEMPLATES:
        return TEMPLATES[action].format(topic=topic)
    else:
        # Fallback if classification or action doesn't match expected keys
        if action in ["explain", "discuss", "create"]:
            return TEMPLATES[action].format(topic=topic)
        else:
            return TEMPLATES["general"].format(topic=topic)


    # Classify the query
    classification = classify_query(parsed_query_example)
    
    # Generate a prompt based on classification
    prompt = generate_prompt(classification, parsed_query_example)
    
    # Print the generated prompt
    print("Generated Prompt:", prompt)
