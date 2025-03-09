from owlready2 import GeneralClassAxiom, Not, Thing

from . import _my_ontology
from action import Agent, Person
from role import SocialRole, Function, played_by, Role, OrganisationRole

onto = _my_ontology()

class LegalRole(Thing):
    ontology = onto

class SocialLegalRole(Thing):
    ontology = onto

class ProfessionalLegalRole(Thing):
    ontology = onto


gca__social_legal_role = GeneralClassAxiom(LegalRole & SocialRole & Not(Function))
gca__social_legal_role.is_a.append(SocialLegalRole)

gca__legal_role = GeneralClassAxiom(Role & played_by.some(Agent) & played_by.all(Agent))
gca__legal_role.is_a.append(LegalRole)

gca__professional_legal_role = GeneralClassAxiom(SocialLegalRole & OrganisationRole & played_by.all(Person))
gca__professional_legal_role.is_a.append(ProfessionalLegalRole)

SocialLegalRole.comment.append("A social legal role is played by some agent in the context of legal activities.")
LegalRole.comment.append("A legal role is a role played in a legal context. Legal role players can be both Agents and other 'things'")
ProfessionalLegalRole.comment.append("A professional legal role is a legal profession of some person, examples: lawyer, judge etc.")
