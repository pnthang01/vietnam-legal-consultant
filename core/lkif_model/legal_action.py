from owlready2 import Thing, AllDisjoint, GeneralClassAxiom

from . import _my_ontology
from action import Person, Transaction, actor, Organisation, Action
from expression import SpeechAct, towards, Promise, StatementInWriting
from mereology import strict_part_of
from process import creation

onto = _my_ontology()

class LegalSpeechAct(SpeechAct):
    ontology = onto

class Decision(Thing):
    ontology = onto
class LegalPerson(Organisation):
    ontology = onto
    equivalent_to = [Person]

class PublicBody(LegalPerson):
    ontology = onto

class PrivateLegalPerson(LegalPerson):
    ontology = onto
    label = ["Legal Person (Private Law)"]

class Assignment(Thing):
    ontology = onto

class ActOfLaw(Thing):
    ontology = onto

class Company(PrivateLegalPerson):
    ontology = onto

class LimitedCompany(Company):
    ontology = onto

class PublicLimitedCompany(Company):
    ontology = onto
    label = ["PLC"]

class LegislativeBody(PublicBody):
    ontology = onto
    label = ["Legislative Body", "Legislature"]

class Corporation(PrivateLegalPerson):
    ontology = onto

class Unincorporated(Corporation):
    ontology = onto
    equivalent_to = [LimitedCompany]

class Incorporated(Corporation):
    ontology = onto
    equivalent_to = [PublicLimitedCompany]

class Foundation(Corporation):
    ontology = onto

class Delegation(Thing):
    ontology = onto

class Association(PrivateLegalPerson):
    ontology = onto

class Society(PrivateLegalPerson):
    ontology = onto
    equivalent_to = [Association]

class Cooperative(Society):
    ontology = onto

class NaturalPerson(Person):
    ontology = onto
    equivalent_to = [Person]

class Mandate(Thing):
    ontology = onto


class PublicAct(Action):
    ontology = onto

AllDisjoint([PrivateLegalPerson, PublicBody])
AllDisjoint([Unincorporated, Foundation, Incorporated])

gca_mandate = GeneralClassAxiom(PublicAct & strict_part_of.some(Transaction) & actor.some(PublicBody))
gca_mandate.is_a.append(Mandate)

gca_delegation = GeneralClassAxiom(LegalSpeechAct & PublicAct & actor.some(PublicBody) & strict_part_of.some(Transaction))
gca_delegation.is_a.append(Delegation)

gca_decision = GeneralClassAxiom(LegalSpeechAct & creation.some(Promise & towards.some(PublicAct)) & actor.some(PublicBody) &
                                 creation.some(StatementInWriting & towards.some(PublicAct)))
gca_decision.is_a.append(Decision)

gca_actoflaw = GeneralClassAxiom(PublicAct & LegalSpeechAct & actor.some(LegislativeBody))
gca_actoflaw.is_a.append(ActOfLaw)

gca_assigment = GeneralClassAxiom(PublicAct & LegalSpeechAct & actor.some(PublicBody) & strict_part_of.some(Transaction))
gca_assigment.is_a.append(Assignment)

Company.is_a.append(LimitedCompany)
Company.is_a.append(PublicLimitedCompany)
Corporation.is_a.append(Unincorporated)
Corporation.is_a.append(Incorporated)
Corporation.is_a.append(Foundation)


Assignment.comment.append("A public act that attributes a power to perform a public act to a public body.")
Association.comment.append("A voluntary association (also sometimes called an unincorporated association, or just an association) is a group of individuals who voluntarily enter into an agreement to form a body (or organization) to accomplish a purpose.")
ActOfLaw.comment.append("Act of law: a public act by a legislative body which creates an expression with legal status; the legal status depends on the jurisdiction of the legislative body.")
Incorporated.comment.append("An organisation formed into a legal corporation")
PublicLimitedCompany.comment.append("Similar to the US corporation, offers several advantages over trading as sole trader.")
Decision.comment.append("Decision: A (written) decision of a public body to perform a public act using a public power assigned by law.")
Company.comment.append("A company refers to a legal entity formed which has a separate legal identity from its members, and is ordinarily incorporated to undertake commercial business. Although some jurisdictions refer to unincorporated entities as companies, in most jurisdictions the term refers only to incorporated entities.")
PublicAct.comment.append("A public act is an act by some Person or Organisation which creates (at least) a communicated attitude (and thereby an expression)")
LegalSpeechAct.comment.append("A legal speech act creates some propositional attitude towards a legal expression.")
Delegation.comment.append("Delegate: entrust a task or responsibility to some other person")
LegislativeBody.comment.append("A legislature is a type of (representative) deliberative assembly with the power to adopt laws.")
Cooperative.comment.append("An autonomous association of persons united voluntarily to meet their common economic, social, and cultural needs and aspirations through a jointly-owned and democratically-controlled enterprise.")
Foundation.comment.append("A kind of (philanthropic) organization, set up as a legal entity either by individuals or institutions, with the purpose of distributing grants to support causes in line with the goals of the foundation")
PublicBody.comment.append("A public body or body created by an act of law to serve a public interest")
LegalPerson.comment.append("A legal entity is a natural person or a legal construct through which the law allows a group of natural persons to act as if it were a single composite individual for certain purposes. The most common purposes are lawsuits, property ownership, and contracts. Sometimes referred to as corporate personhood or legal personality, this concept allows for easy conduct of business by having ownership, lawsuits, and agreements under the name of the legal entity instead of the several names of the people making up the entity.\n\nA legal entity is not necessarily distinct from the natural persons of which it is composed. Most legal entities are simply amalgamations of the persons that make it up for convenience's sake. A legal entity that does have a separate existence from its members is called a company or corporation. This distinction gives the corporation its unique perpetual succession privilege and is usually also the source of the limited liability of corporate members. Some other legal entities also enjoy limited liability of members, but not on account of separate existence (Source: Wikipedia.org)")
Corporation.comment.append("A corporation is a legal entity which, while being composed of natural persons, exists completely separately from them. This separation gives the corporation unique powers which other legal entities lack.")
Mandate.comment.append("Mandate: give (someone) authority to act in a certain way")
NaturalPerson.comment.append("A natural person is a human being perceptible through the senses and subject to physical laws, as opposed to an artificial person, i.e., an organization that the law treats for some purposes as if it were a person distinct from its members or owner.")
Society.comment.append("An organized group of people associated together for religious, benevolent, cultural, scientific, political, patriotic, or other purposes.")
LimitedCompany.comment.append("A limited company is a corporation whose liability is limited by law")
PrivateLegalPerson.comment.append("A legal person as defined in private law")