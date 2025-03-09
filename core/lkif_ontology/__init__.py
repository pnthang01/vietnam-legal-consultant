import types

from owlready2 import *

onto_path.append("./")
onto = get_ontology("file://./lkif-top.owl")
# onto = default_world.get_ontology("file://./lkif_loaded.owl").load()

with onto:
    #lkif-top.owl
    AbstractEntity = types.new_class("AbstractEntity", (Thing,))
    MentalEntity = types.new_class("MentalEntity", (Thing, ))
    MentalObject = types.new_class("MentalObject", (MentalEntity,))
    Occurrence = types.new_class("Occurrence", (Thing,))
    SpatioTemporalOccurrence = types.new_class("SpatioTemporalOccurrence", (Occurrence,))
    PhysicalEntity = types.new_class("PhysicalEntity", (Thing,))
    #
    Change = types.new_class("Change", (Thing,))
    LegalRole = types.new_class("LegalRole", (Thing,))
    SocialLegalRole = types.new_class("SocialLegalRole", (Thing, ))
    ProfessionalLegalRole = types.new_class("ProfessionalLegalRole", (Thing, ))

    Decision = types.new_class("Decision", (Thing, ))
    #expression.owl
    Argument = types.new_class("Argument", (Thing,))
    Reason = types.new_class("Reason", (Thing,))
    Belief = types.new_class("Belief", (Thing,))
    Document = types.new_class("Document", (Thing, ))
    Proposition = types.new_class("Proposition", (Thing, ))
    Qualification = types.new_class("Qualification", (Thing, ))
    Qualified = types.new_class("Qualified", (Thing, ))
    Medium = types.new_class("Medium", (Thing, ))
    #lkif-core.owl
    LegalRole = types.new_class("LegalRole", (Thing,))
    SocialLegalRole = types.new_class("SocialLegalRole", (Thing,))
    ProfessionalLegalRole = types.new_class("ProfessionalLegalRole", (Thing, ))

    #role.owl
    Agent = types.new_class("Agent", (Thing,))
    Organisation = types.new_class("Organisation", (Thing,))


org_01 = Organisation("org_01", namespace=onto)

print(org_01)