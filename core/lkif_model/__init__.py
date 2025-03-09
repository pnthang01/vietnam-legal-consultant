from owlready2 import default_world

onto = default_world

def _my_ontology():
    global onto
    return onto

def get_law_ontology():
    return onto

