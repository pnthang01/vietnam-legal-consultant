import openai
from dotenv import load_dotenv
from owlready2 import *

import core
from mirascope.core import openai

load_dotenv()

# Get all LKIF classes with descriptions
def get_ontology_classes(ontology):
    class_defs = []
    for cls in ontology.classes():
        label = cls.label[0] if cls.label else cls.name
        definition = cls.comment[0] if cls.comment else "No explicit definition."
        class_defs.append((label, definition))
    return class_defs

# Classify terms using LLM
@openai.call("gpt-4o-mini")
def classify_term_with_llm(term, class_defs) -> str:
    # Prepare the prompt
    prompt = f"You are an expert legal classifier. Given the legal term '{term}', classify it into one of the following LKIF ontology classes. Respond with only the exact class name.\n\n"
    for label, definition in class_defs:
        prompt += f"Class Name: {label}\nDefinition: {definition}\n\n"

    prompt += f"Legal term to classify: '{term}'\nClass Name:"

    return prompt

# Example terms from legal clause
legal_terms = ["obligation", "breach", "damages", "right"]

onto = core.get_law_ontology()
# Extract ontology classes and definitions
ontology_class_defs = get_ontology_classes(onto)

# Classify each term
term_classification = {}
# for term in legal_terms:
classified_as = classify_term_with_llm(legal_terms[0], ontology_class_defs)
term_classification[legal_terms[0]] = classified_as

# Output Results
print("LLM-based Classification Results:")
for term, classification in term_classification.items():
    print(f"'{term}' classified as: {classification}")
