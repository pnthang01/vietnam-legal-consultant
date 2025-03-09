import types

from owlready2 import *
import i18n
i18n.load_path.append('../../resources/i18n')

onto_path.append("./")

# onto = get_ontology("http://www.estrellaproject.org/lkif-core/lkif-top.owl").load()
onto = default_world.get_ontology("file://./lkif-top.owl").load()

with onto:
    #lkif-top.owl
    AbstractEntity = types.new_class("AbstractEntity", (Thing,))
    MentalEntity = types.new_class("MentalEntity", (Thing, ))
    MentalObject = types.new_class("MentalObject", (MentalEntity,))
    Occurrence = types.new_class("Occurrence", (Thing,))
    SpatioTemporalOccurrence = types.new_class("SpatioTemporalOccurrence", (Occurrence,))
    PhysicalEntity = types.new_class("PhysicalEntity", (Thing,))
    AbstractEntity.comment.append(i18n.t('lkif.comment.AbstractEntity'))
    MentalEntity.comment.append(i18n.t('lkif.comment.MentalEntity'))
    MentalObject.comment.append(i18n.t('lkif.comment.MentalObject'))
    Occurrence.comment.append(i18n.t('lkif.comment.Occurrence'))
    PhysicalEntity.comment.append(i18n.t('lkif.comment.PhysicalEntity'))
    SpatioTemporalOccurrence.comment.append(i18n.t('lkif.comment.SpatioTemporalOccurrence'))
    #mereology.owl
    Atom = types.new_class("Atom", (AbstractEntity,))
    Whole = types.new_class("Whole", (Thing,))
    Part = types.new_class("Part", (Thing,))
    Composition = types.new_class("Composition", (Whole,))
    Pair = types.new_class("Pair", (Thing, ))
    class part(TransitiveProperty): pass
    class part_of(TransitiveProperty):
        inverse = part
    class strict_part(part): pass
    class strict_part_of(part_of):
        inverse = strict_part
    class member_of(strict_part_of): pass
    class member(strict_part):
        inverse = member_of
    class direct_part_of(part_of): pass  # Missing equivalentProperty:strict_part_of

    class direct_part(part):  # Missing equivalentProperty:strict_part
        inverse = direct_part_of
    class contained_in(part_of, TransitiveProperty):
        pass
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
    #process.owl
    Change = types.new_class("Change", (Thing, ))
    Process = types.new_class("Process", (Change,))
    class participant(ObjectProperty):
        domain = [Change]
        range = [Thing]
    class participant_in(ObjectProperty):
        domain = [Thing]
        range = [Change]
        inverse_property = participant
    #role.owl
    Agent = types.new_class("Agent", (Thing,))
    SubjectiveEntity = types.new_class("SubjectiveEntity", (MentalEntity, ))
    Role = types.new_class("Role", (SubjectiveEntity,))
    Artifact = types.new_class("Artifact", (Thing, ))
    Organisation = types.new_class("Organisation", (Thing,))
    Function = types.new_class("Function", (Role, ))
    SocialRole = types.new_class("SocialRole", (Role, ))
    OrganisationRole = types.new_class("OrganisationRole", (SocialRole,))
    PersonRole = types.new_class("PersonRole", (SocialRole,))
    EpistemicRole = types.new_class("EpistemicRole", (Role,))
    # action.owl
    Action = types.new_class("Action", (Process,))
    class actor(participant):
        domain = [Action]
        range = [Agent]
    class actor_in(participant_in):
        domain = [Agent]
        range = [Action]
        inverse = actor
    class context(ObjectProperty): pass
    class counts_as(ObjectProperty): pass
    class imposed_on(ObjectProperty, FunctionalProperty): pass
    class played_by(imposed_on):
        domain = [Role]
        range = [Thing]
    class plays(counts_as):
        domain = [Thing]
        range = [Role]
        inverse = played_by

    AllDisjoint([context, imposed_on])
    AllDisjoint([Agent, Role])
    AllDisjoint([PhysicalEntity, Role])
    AllDisjoint([Process, Role])
    AllDisjoint([Function, SocialRole])
    Action.is_a.append(actor.only(plays.some(Role)))

org_01 = Organisation("org_01", namespace=onto)
c_level_01 = OrganisationRole("c_level_01", namespace=onto)
Anna = Agent("Anna", namespace=onto, member_of=[org_01], plays=[c_level_01])

print(Organisation.comment)
print(Anna.member_of)
print(Anna.plays)
print(org_01.member)
# print(org_01.member)