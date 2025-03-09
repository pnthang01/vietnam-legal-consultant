from owlready2 import FunctionalProperty, AllDisjoint, ObjectProperty, Thing, OneOf, Not, GeneralClassAxiom

from . import _my_ontology
from .action import actor, Action, Person
from .mereology import member, member_of
from .process import Process, PhysicalObject, MentalProcess
from .lkif_top import PhysicalEntity, MentalObject, MentalEntity

onto = _my_ontology()


class Agent(Thing):
    ontology = onto


class SubjectiveEntity(MentalEntity):
    ontology = onto


class Role(SubjectiveEntity):
    ontology = onto


class Artifact(Thing):
    ontology = onto


class Organisation(Thing):
    ontology = onto


class Function(Role):
    ontology = onto


class SocialRole(Role):
    ontology = onto


class OrganisationRole(SocialRole):
    ontology = onto


class PersonRole(SocialRole):
    ontology = onto


class EpistemicRole(Role):
    ontology = onto


class context(ObjectProperty):
    ontology = onto


class counts_as(ObjectProperty):
    ontology = onto


class imposed_on(ObjectProperty, FunctionalProperty):
    ontology = onto


class played_by(imposed_on):
    ontology = onto
    domain = [Role]
    range = [Thing]


class plays(counts_as):
    ontology = onto
    domain = [Thing]
    range = [Role]
    inverse_property = played_by


AllDisjoint([context, imposed_on])
AllDisjoint([Agent, Role])
AllDisjoint([PhysicalEntity, Role])
AllDisjoint([Process, Role])
AllDisjoint([Function, SocialRole])

gca__action = GeneralClassAxiom(actor.all(plays.some(Role)))
gca__action.is_a.append(Action)

gca__agent = GeneralClassAxiom(plays.all(Role))
gca__agent.is_a.append(Agent)

gca__artifact = GeneralClassAxiom(plays.some(Function))
gca__artifact.is_a.append(Artifact)

gca__organisation = GeneralClassAxiom(member.all(plays.some(OrganisationRole)))
gca__organisation.is_a.append(Organisation)

gca__epistemic_role = GeneralClassAxiom(played_by.some(MentalObject) & context.some(MentalProcess) & played_by.all(MentalObject))
gca__epistemic_role.is_a.append(EpistemicRole)

gca__function = GeneralClassAxiom(Role & played_by.all(PhysicalObject & Not(Agent)) & played_by.some(PhysicalObject))
gca__function.is_a.append(Function)

gca__organisation_role = GeneralClassAxiom(SocialRole & played_by.all(Agent & member_of.some(Organisation)))
gca__organisation_role.is_a.append(OrganisationRole)

gca__person_role = GeneralClassAxiom(SocialRole & played_by.some(Person) & played_by.all(Person))
gca__person_role.is_a.append(PersonRole)

gca__social_role = GeneralClassAxiom(Role & played_by.all(Agent) & played_by.some(Agent))
gca__social_role.is_a.append(SocialRole)

Role.is_a.append(played_by.some(Thing))
SubjectiveEntity.is_a.append(context.some(Thing) & imposed_on.some(Thing))


Role.comment.append(
    "A role is a specification of default behavior and accompanying expectations of the thing 'playing' the role. Similar to actors in a theater who play roles, but are not the roles. Example: student.")
EpistemicRole.comment.append("The role of something used in a (mental) reasoning/inference process")
Function.comment.append("The use or purpose of some object as used in some context.")
OrganisationRole.comment.append(
    "A role which has a meaning in the context of an organisation: i.e. the role defines a 'position' within sthe structure of roles within an organisation")
PersonRole.comment.append("A role played by some person (i.e. not an organisation)")
SocialRole.comment.append(
    "A social role is played by some agent in the context of social activities. The social role brings with it some expectation of 'default' behavior of the role-filler.")
SubjectiveEntity.comment.append(
    "A subjective entity is ontologically subjective, i.e. its existence is relative to an observer, that attributes its properties to some other entity, given a context.")

context.comment.append("The context property relates a subjective entity to the context in which the entity holds.")
imposed_on.comment.append("Specifies that some subjective entity is imposed on some thing")
counts_as.comment.append(
    "The counts-as relation of Searle (1995) is used to express the creation of observer-relative or social facts such as the playing of roles or having a function.")
played_by.comment.append("Specifies that some role is played by some thing")
plays.comment.append("Specifies that some thing plays a role")
