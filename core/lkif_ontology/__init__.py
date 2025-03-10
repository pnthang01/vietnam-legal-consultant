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
    Whole = types.new_class("Whole", (AbstractEntity,))
    Part = types.new_class("Part", (AbstractEntity,))
    Composition = types.new_class("Composition", (Whole,))
    Pair = types.new_class("Pair", (Composition, ))
    Part.comment.append(i18n.t('lkif.comment.Part'))
    Whole.comment.append(i18n.t('lkif.comment.Whole'))
    Pair.comment.append(i18n.t('lkif.comment.Pair'))
    class part(TransitiveProperty):
        comment = i18n.t('lkif.comment.part')
    class part_of(TransitiveProperty):
        inverse = part
        comment = i18n.t('lkif.comment.part_of')
    class strict_part(part):
        comment = i18n.t('lkif.comment.strict_part')
    class strict_part_of(part_of):
        inverse = strict_part
        comment = i18n.t('lkif.comment.strict_part_of')
    class member_of(strict_part_of):
        comment = i18n.t('lkif.comment.member_of')
    class a__member(strict_part):
        inverse=member_of
        comment = i18n.t('lkif.comment.member')
    class direct_part_of(part_of):
        is_a = [strict_part_of]
        comment = i18n.t('lkif.comment.direct_part_of')
    class direct_part(part):  # Missing equivalentProperty:strict_part
        inverse = direct_part_of
        is_a = [strict_part]
        comment = i18n.t('lkif.comment.direct_part')
    class contained_in(part_of, TransitiveProperty):
        comment = i18n.t('lkif.comment.contained_in')
    class contains(part, TransitiveProperty):
        inverse = contained_in
        comment = i18n.t('lkif.comment.contains')
    class composes(part_of, TransitiveProperty):
        comment = i18n.t('lkif.comment.composes')
    class composed_of(part, TransitiveProperty):
        inverse = composes
        comment = i18n.t('lkif.comment.composed_of')
    class component(strict_part):
        comment = i18n.t('lkif.comment.component')
    class component_of(strict_part_of):
        inverse = component
        comment = i18n.t('lkif.comment.component_of')
    AllDisjoint([Whole, Atom])
    gca__pair = GeneralClassAxiom(strict_part.exactly(2, Part))
    gca__pair.is_a.append(Pair)
    gca__part = GeneralClassAxiom(strict_part_of.some(Whole) | strict_part_of.only(Whole))
    gca__part.is_a.append(Part)
    gca__whole = GeneralClassAxiom(strict_part.some(Part) | strict_part.only(Part))
    gca__whole.is_a.append(Whole)
    #
    Change = types.new_class("Change", (Thing,))

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
    #process.owl
    Change = types.new_class("Change", (Thing, ))
    Process = types.new_class("Process", (Change,))
    PhysicalObject = types.new_class("PhysicalObject", (PhysicalEntity,))
    PhysicalObject.comment.append(i18n.t('lkif.comment.PhysicalObject'))
    class participant(ObjectProperty):
        domain = [Change]
        range = [Thing]
    class participant_in(ObjectProperty):
        domain = [Thing]
        range = [Change]
        inverse = participant
    #end process.owl
    #role.owl
    Agent = types.new_class("Agent", (Thing,))
    SubjectiveEntity = types.new_class("SubjectiveEntity", (MentalEntity, ))
    Role = types.new_class("Role", (SubjectiveEntity,))
    Artifact = types.new_class("Artifact", (Thing, ))
    Function = types.new_class("Function", (Role, ))
    SocialRole = types.new_class("SocialRole", (Role, ))
    OrganisationRole = types.new_class("OrganisationRole", (SocialRole,))
    OrganisationRole.comment.append(i18n.t('lkif.comment.OrganisationRole'))
    PersonRole = types.new_class("PersonRole", (SocialRole,))
    EpistemicRole = types.new_class("EpistemicRole", (Role,))
    # action.owl
    NaturalObject = types.new_class("NaturalObject", (PhysicalObject,))
    NaturalObject.comment.append(i18n.t('lkif.comment.NaturalObject'))
    Organisation = types.new_class("Organisation", (Agent,))
    Organisation.comment.append(i18n.t('lkif.comment.Organisation'))
    Action = types.new_class("Action", (Process,))
    Person = types.new_class("Person", (Agent, NaturalObject))
    Person.comment.append(i18n.t('lkif.comment.Person'))
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
    # end action.owl
    # legal-role.owl
    LegalRole = types.new_class("LegalRole", (Role,))
    gca__legal_role = GeneralClassAxiom(played_by.some(Agent) | played_by.only(Agent))
    gca__legal_role.is_a.append(LegalRole)
    LegalRole.comment.append(i18n.t('lkif.comment.LegalRole'))
    SocialLegalRole = types.new_class("SocialLegalRole", (LegalRole, ))
    SocialLegalRole.comment.append(i18n.t('lkif.comment.SocialLegalRole'))
    gca__social_legal_role = GeneralClassAxiom(SocialRole & Not(Function))
    gca__social_legal_role.is_a.append(SocialLegalRole)
    ProfessionalLegalRole = types.new_class("ProfessionalLegalRole", (SocialLegalRole, OrganisationRole))
    ProfessionalLegalRole.comment.append(i18n.t('lkif.comment.ProfessionalLegalRole'))
    gca__professional_legal_role = GeneralClassAxiom(played_by.only(Person))
    gca__professional_legal_role.is_a.append(ProfessionalLegalRole)
    AllDisjoint([SocialLegalRole, SocialRole])
    # end legal-role.owl
    AllDisjoint([context, imposed_on])
    AllDisjoint([Agent, Role])
    AllDisjoint([PhysicalEntity, Role])
    AllDisjoint([Process, Role])
    AllDisjoint([Function, SocialRole])
    Action.is_a.append(actor.only(plays.some(Role)))
    #start action.owl again
    # gca__organisation = GeneralClassAxiom(a__member.some(Person) | a__member.only(Or([Organisation, Person])))
    # gca__organisation.is_a.append(Organisation)
    Organisation.is_a.append(a__member.some(Person) | a__member.only(Or([Organisation, Person])))
    AllDisjoint([Organisation, Person])
    #end action.owl again
    # start role.owl again
    gca__organisation_role = GeneralClassAxiom(played_by.only(And([Agent, member_of.some(Organisation)])))
    gca__organisation_role.is_a.append(OrganisationRole)
    # end role.owl again

#Test here
org_01 = Organisation("org_01", namespace=onto)
c_level_01 = OrganisationRole("c_level_01", namespace=onto)
Anna = Person("Anna", namespace=onto, member_of=[org_01], plays=[c_level_01])


print(Anna.member_of)
print(Anna.plays)
print(org_01.a__member)
# print(org_01.member)
