from owlready2 import *
onto = get_ontology("http://test.org/Family#")
with onto:

    '''defining base classes'''
    class Human(Thing): pass
    class Man(Human): pass
    class Woman(Human): pass
    AllDisjoint([Man, Woman])

    '''defining properties'''
    class has_couple(Human>>Human): pass
    class has_wife(has_couple, Man>>Woman): pass
    class has_husbend(has_couple):
        inverse=has_wife
    class has_child (Human>>Human): pass
    class has_parent (ObjectProperty):
        inverse=has_child

    '''defining individuals'''
    Kevin = Man("Kevin")
    '''defining relations between individuals'''
    Viper = Woman("Viper", has_husbend=[Kevin])
    John = Man("John", has_parent=[Kevin])
    Anna = Woman("Anna", has_parent=[Kevin])

print('check kevin')
print(Kevin.has_child)
print(Kevin.has_wife)
print(John.has_parent)

'''reasoning'''
# with onto:
#     test = sync_reasoner_pellet(infer_property_values=True, infer_data_property_values = True)
#     print(test)

print('-')
print(Viper.has_husbend)
print(Kevin.has_wife)


onto.save(file = "family.owl", format = "rdfxml")