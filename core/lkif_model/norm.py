from owlready2 import TransitiveProperty, ObjectProperty, SymmetricProperty, GeneralClassAxiom, And, AllDisjoint

from . import _my_ontology
from expression import qualitatively_comparable, qualifies, qualified_by, Qualified, bears, utterer, attitude, \
    Expression, Belief, towards, EvaluativeProposition, Medium, Document, Observation, Qualification, Intention, Problem
from legal_action import LegislativeBody, PublicAct, NaturalPerson, LegalPerson
from process import created_by
from role import played_by

onto = _my_ontology()


class NormativelyQualified(Qualified):
    ontology = onto


class Norm(Qualification):
    ontology = onto
    equivalent_to = [qualifies.some(NormativelyQualified)]


class LegalSource(Medium):
    ontology = onto


class LegalDocument(LegalSource, Document):
    ontology = onto


class SoftLaw(LegalSource):
    ontology = onto


class CodeOfConduct(LegalDocument, SoftLaw):
    ontology = onto


class Regulation(LegalDocument):
    ontology = onto


class Statute(LegalDocument):
    ontology = onto


class Proclamation(LegalSource):
    ontology = onto


class LegalExpression(Expression):
    ontology = onto


class PotestativeExpression(LegalExpression):
    ontology = onto


class HohfeldianPower(PotestativeExpression):
    ontology = onto


class ActionPower(HohfeldianPower):
    ontology = onto


class QualificatoryExpression(LegalExpression):
    ontology = onto


class EnablingPower(PotestativeExpression):
    ontology = onto


class Right(Norm):
    ontology = onto


class ExistentialExpression(LegalExpression):
    ontology = onto


class Code(LegalDocument):
    ontology = onto


class Allowed(NormativelyQualified):
    ontology = onto


class StrictlyAllowed(Allowed):
    ontology = onto


class Obliged(Allowed):
    ontology = onto


class LegalDoctrine(LegalSource):
    ontology = onto


class InternationalArbitration(SoftLaw):
    ontology = onto


class Immunity(HohfeldianPower):
    ontology = onto


class Disallowed(NormativelyQualified):
    ontology = onto


class Precedent(LegalSource):
    ontology = onto


class ObligativeRight(Right):
    ontology = onto


class PersuasivePrecedent(Precedent):
    ontology = onto


class BeliefInViolation(Belief):
    ontology = onto
    equivalent_to = [Belief & towards.some(Disallowed)]


class DeclarativePower(PotestativeExpression):
    ontology = onto


class Contract(LegalDocument):
    ontology = onto


class Decree(LegalDocument, Proclamation):
    ontology = onto


class EvaluativeExpression(LegalExpression, EvaluativeProposition):
    ontology = onto


class LibertyRight(Right):
    ontology = onto


class Custom(Medium):
    ontology = onto


class StrictlyDisallowed(Disallowed):
    ontology = onto


class PermissiveRight(Right):
    ontology = onto


class ExclusionaryRight(ObligativeRight):
    ontology = onto


class InternationalAgreement(LegalSource):
    ontology = onto


class Resolution(SoftLaw, InternationalAgreement):
    ontology = onto


class CustomaryLaw(LegalSource, Custom):
    ontology = onto


class Treaty(InternationalAgreement, LegalDocument):
    ontology = onto


class MandatoryPrecedent(Precedent):
    ontology = onto


class ObservationOfViolation(Problem):
    ontology = onto


class PotestativeRight(EnablingPower):
    ontology = onto


class AllowedAndDisallowed(Allowed, Disallowed):
    ontology = onto
    equivalent_to = [Allowed & Disallowed]


class DefinitionalExpression(LegalExpression):
    ontology = onto


class Permission(Norm):
    ontology = onto


class Prohibition(Permission):
    ontology = onto


class Obligation(Permission):
    ontology = onto
    equivalent_to = [Prohibition]


class DisallowedIntention(Intention):
    ontology = onto
    equivalent_to = [Intention & towards.some(Disallowed)]


class NonBindingInternationalAgreement(InternationalAgreement, SoftLaw):
    ontology = onto


class Directive(Proclamation, LegalDocument):
    ontology = onto


class LiabilityRight(Right):
    ontology = onto


class normatively_comparable(qualitatively_comparable, ObjectProperty):
    ontology = onto
    domain = [NormativelyQualified]
    range = [NormativelyQualified]


class allowed_by(qualified_by, ObjectProperty):
    ontology = onto
    domain = [Allowed]


class allows(qualifies, ObjectProperty):
    ontology = onto
    range = [Allowed]
    inverse_property = allowed_by


class commands(allows, ObjectProperty):
    ontology = onto
    range = [Obliged]


class commanded_by(allowed_by, ObjectProperty):
    ontology = onto
    domain = [Obliged]
    inverse_property = commands


class normatively_equivalent_or_worse(normatively_comparable, ObjectProperty):
    ontology = onto
    domain = [Allowed]


class normatively_not_equivalent(normatively_comparable, SymmetricProperty, ObjectProperty):
    ontology = onto


class normatively_equivalent_or_better(normatively_comparable, TransitiveProperty, ObjectProperty):
    ontology = onto
    range = [Allowed]
    inverse_property = normatively_equivalent_or_worse


class normatively_strictly_better(normatively_equivalent_or_better, TransitiveProperty, ObjectProperty):
    ontology = onto
    domain = [Disallowed]
    range = [Obliged]


class disallowed_by(qualified_by, ObjectProperty):
    ontology = onto
    domain = [Disallowed]


class disallows(qualifies):
    ontology = onto
    range = [Disallowed]
    inverse_property = disallowed_by


class normatively_strictly_worse(normatively_equivalent_or_worse, normatively_not_equivalent, TransitiveProperty,
                                 ObjectProperty):
    ontology = onto
    domain = [Obliged]
    range = [Disallowed]
    inverse_property = normatively_strictly_better


class strictly_equivalent(normatively_equivalent_or_better, normatively_equivalent_or_worse, TransitiveProperty,
                          ObjectProperty, SymmetricProperty):
    ontology = onto
    domain = [Allowed]
    range = [Allowed]


AllDisjoint([Custom, Document])
AllDisjoint([Treaty, NonBindingInternationalAgreement])

gca__normatively_qualified = GeneralClassAxiom(normatively_comparable.some(NormativelyQualified))
gca__normatively_qualified.is_a.append(NormativelyQualified)

gca___regulation = GeneralClassAxiom(
    bears.some(Norm & utterer.some(LegislativeBody)) & bears.all(utterer.some(LegislativeBody)))
gca___regulation.is_a.append(Regulation)

gca__legal_expression = GeneralClassAxiom(attitude.some(created_by.some(PublicAct)))
gca__legal_expression.is_a.append(LegalExpression)

gca__contract = GeneralClassAxiom(And([bears.all(utterer.some(NaturalPerson | LegalPerson)),
                                       bears.some(Norm & utterer.some(NaturalPerson | LegalPerson))]))
gca__contract.is_a.append(Contract)

gca__statute = GeneralClassAxiom(
    And([bears.some(Norm & utterer.some(LegalPerson)), bears.all(utterer.some(LegalPerson))]))
gca__statute.is_a.append(Statute)

gca__code = GeneralClassAxiom(
    And([bears.some(Norm & utterer.some(LegislativeBody)), bears.all(utterer.some(LegislativeBody))]))
gca__code.is_a.append(Code)

Prohibition.is_a.append(Obligation)
Prohibition.is_a.append(
    And([allows.all(Obliged), allows.some(Obliged), disallows.all(Disallowed), disallows.some(Disallowed)]))
Disallowed.is_a.append(disallowed_by.some(Prohibition))
Disallowed.is_a.append(normatively_strictly_better.some(Allowed))
Obliged.is_a.append(allowed_by.some(Obligation))
Obliged.is_a.append(normatively_strictly_worse.some(Disallowed))
Permission.is_a.append(allows.some(Allowed) & allows.all(Allowed))
ObservationOfViolation.is_a.append(Observation & played_by.some(Disallowed))
Allowed.is_a.append(normatively_equivalent_or_worse.some(NormativelyQualified))
Allowed.is_a.append(allowed_by.some(Permission))
LegalSource.is_a.append(bears.some(Norm | LegalExpression))
NormativelyQualified.is_a.append(qualified_by.some(Norm))
strictly_equivalent.is_a.append(strictly_equivalent)
normatively_not_equivalent.is_a.append(normatively_not_equivalent)

Precedent.comment.append(
    "In law, a precedent or authority is a legal case establishing a principle or rule that a court may need to adopt when deciding subsequent cases with similar issues or facts. The term may also refer to the collective body of case law that a court should consider when interpreting the law. When a precedent establishes an important legal principle, or represents new or changed law on a particular issue, that precedent is often known as a landmark decision.")
Prohibition.comment.append(
    "Prohibition obliges/allows thing(s), to which therefore the predication Obliged applies, and disallows thing(s), to which therefore the predication Disallowed applies. The union of the thing(s) allowed and the thing(s) disallowed is qualified by the prohibition. The things allowed and disallowed by the prohibition are disjoint (and completely partition the space of things qualified). If S then O(A) means that S is qualified, S and A is obliged/allowed, and S and not A is disallowed. If S then F(A) means that S is qualified, S and A is disallowed, and S and not A is obliged/allowed. The difference between Obligation and Prohibition is in which part of the partition of the qualified space is explicitly described by the normative statement. Alternative label: directive")
DefinitionalExpression.comment.append(
    "A definition in a legal context (for example “x means y” or “by x it is meant y”);")
Disallowed.comment.append("See Qualified. Alternative labels: violation, prohibited, forbidden")
Directive.comment.append(
    "Examples are European Union directive, a legislative act of the European Union and Directives, used by United States Government agencies (particularly the Department of Defense) to convey policies, responsibilities, and procedures.")
NonBindingInternationalAgreement.comment.append(
    "Some international agreement that is not binding under international law")
Obliged.comment.append(
    "Is allowed by an Obligation, i.e. the alternative is strictly_worse according to the Obligation. Alternative labels: directed, commanded.")
Right.comment.append(
    "A right is the legal or moral entitlement to do or refrain from doing something or to obtain or refrain from obtaining an action, thing or recogition in civil society.")
LiabilityRight.comment.append(
    "A liability right expresses some right to act that brings with it some liability to perform another (compensating) act. For instance, if some k performs the permitted action A, then k will have to perform another action B for the benefit of j.")
Permission.comment.append(
    "Permission allows propositions, to which therefore the predication Allowed applies. The thing(s) allowed is/are a subset of the thing(s) qualified by the permission. If S then P(A) means that S is qualified and S and A is allowed.")
DisallowedIntention.comment.append(
    "The propositional content (i.e. that which is intended) of the intention is disallowed. Interesting concept for establishing mens rea (guilty mind), although 'disallowed' is a weaker qualification than criminal. Note the distinction between purposely committing a crime and knowingly committing a crime. The crime committed does not have to match the crime intended for establishing intent!")
Obligation.comment.append("See prohibition")
AllowedAndDisallowed.comment.append("Something which is both allowed and disallowed through some norm")
PotestativeRight.comment.append(
    "A potestative right is an enabling power which is meant to benefit the holder of the power. For example, if some animal y does not \nbelong to anybody, then x has the potestative-right to start x’s ownership of the animal,  by capturing y.")
Norm.comment.append(
    "A norm is a kind of Qualification. A qualification which normatively qualifies some thing (i.e. some normatively qualified): i.e. a qualification which allows or disallows some thing.")
PotestativeExpression.comment.append(
    "Attributes a power to some agent (for example “a worker has the power to terminate his work contract”);")
LegalDocument.comment.append(
    "A legal document is a document bearing norms or normative statements. By virtue of this definition the norm-as-propositional-attitude is reified as norm-as proposition. In other words, the norm being expressed through the legal source is an expression of the propositional attitude.")
LegalDocument.comment.append(
    "Subclasses of legal source can be distinguished through the authority of the agent creating the expression (i.e. the agent holding the norm).")
ObservationOfViolation.comment.append("An observation of a violation, i.e. of something that is Disallowed.")
Allowed.comment.append("See normatively qualified. Alternative labels: permitted, sanctioned, let, licensed.")
Code.comment.append(
    "A legal code bears one or more norms, all of which are uttered by some legislative body. It cannot bear expressions which are not uttered by a legislative body.")
MandatoryPrecedent.comment.append(
    "In law, a binding precedent (also mandatory precedent or binding authority) is a precedent which must be followed by all lower courts. It is usually created by the decision of a higher court, such as the House of Lords in the United Kingdom. Binding precedent relies on the legal principle of stare decisis.")
Treaty.comment.append(
    "A treaty is a binding agreement under international law entered into by actors in international law, namely states and international organizations. Treaties are called by several names: treaties, international agreements, protocols, covenants, conventions, exchanges of letters, exchanges of notes, etc.")
Immunity.comment.append("Also called Disabilities")
InternationalArbitration.comment.append(
    "International Arbitration is the established method today for resolving disputes between parties to international commercial agreements. As with arbitration generally, it is a creature of contract, i.e., the parties' decision to submit any disputes to private adjudication by one or more arbitrators appointed in accordance with rules the parties themselves have agreed to adopt, usually by including a provision for the same in their contract. The practice of international arbitration has developed so as to allow parties from different legal and cultural backgrounds to resolve their disputes, generally without the formalities of their underlying legal systems.")
Statute.comment.append(
    "A statute bears one or more norms, all of which are uttered by some legal person. It cannot bear expressions which are uttered by a different kind of agent.")
LegalSource.comment.append(
    "A legal source is a source for legal statements, both norms and legal expressions. In a sense it is literally a 'source' of law")
ActionPower.comment.append(
    "An action-power consists in a generic power to produce a legal effect through an action determining it. Also called Subjections")
CustomaryLaw.comment.append(
    "In law, custom, or customary law consists of established patterns of behaviour that can be objectively verified within a particular social setting.")
InternationalAgreement.comment.append(
    "An agreement entered into by actors in international law, namely states and international organizations.")
ExclusionaryRight.comment.append(
    "An exclusionary right concerns the prohibition against performing certain inferences (against reasoning in certain ways), or \nagainst using certain kinds of premises for certain purposes, in the interest of a particular person. This is especially the case with anti-discrimination rules.")
Custom.comment.append(
    "The collective memory of some group of agents, i.e. propositions beared by custom are shared (i.e. held) by all members of the group")
Contract.comment.append(
    "A contract bears one or more norms, all of which are uttered by some natural person or legal person. It cannot bear expressions which are uttered by a different kind of agent.")
DeclarativePower.comment.append(
    "A declarative power covers the case when an effect is produced through the party’s declaration of it")
DeclarativePower.comment.append(
    "We say that j has the declarative power to realize A to mean that if j declares A, then it is legally valid that A. For example, if x has the declarative power to terminate y’s obligation toward x to do then if x declares that y’s obligation toward x finishes, then it is legally valid that this obligation finishes.")
LibertyRight.comment.append(
    "When, for the benefit of a person, this person is both permitted to perform and to omit an action – that is, when the action is facultative – we can say that he or she has a liberty right with regard to that action.")
EvaluativeExpression.comment.append(
    "A legal evaluative expression asserts that something is good or bad, is a value to be optimised or an evil to be minimised (for example “human dignity is value”, “participation ought to be promoted”);")
Resolution.comment.append(
    "A resolution is a written motion adopted by a deliberative body. The substance of the resolution can be anything that can normally be proposed as a motion.")
LegalDoctrine.comment.append(
    "Legal doctrine is a framework, set of rules, procedural steps, or test, often established through precedent in the common law, through which judgments can be determined in a given legal cas")
StrictlyAllowed.comment.append("Loose end.")
Decree.comment.append("The word decree is often used as a derogative term for any authoritarian decision")
BeliefInViolation.comment.append("A belief in some violation")
ExistentialExpression.comment.append(
    "Establishes or terminates the existence of a legal entity (for example “the company ceases to exist”);")
PersuasivePrecedent.comment.append(
    "In law, a persuasive precedent or advisory precedent is a precedent that need not be followed under the legal principle of stare decisis, but is nevertheless followed. Sources of persuasive precedent include the obiter dicta in the judgment of a court whose judgment would otherwise be binding, and the judgments of courts in other jurisdictions where the facts and/or legal system are similar to the case at hand. If a superior court adopts a persuasive precedent, it may become binding in the jurisdiction.")
EnablingPower.comment.append(
    "An enabling power is used in cases where the law aims at enabling some agent to produce an effect in a particular way.")
QualificatoryExpression.comment.append(
    "Ascribes a legal role to a person or an object (for example,  “x is a citizen”, “x is an intellectual work”, “x is a technical invention”);")
LegalExpression.comment.append(
    "Legal expressions are created by  some legal speech act and qualified by a communicated attitude")
Proclamation.comment.append(
    "A proclamation (Lat. proclamare, to make public by announcement) is an official declaration.")
PermissiveRight.comment.append(
    "The  negation of a directed obligation is a directed permission. However, it counts as a right,  namely, a permissive right, only when such negation is aimed at benefitting the author of  the permitted action.")
StrictlyDisallowed.comment.append("Loose end.")
SoftLaw.comment.append(
    "The term soft law refers to quasi-legal instruments which do not have any binding force, or whose binding force is somewhat weaker than the binding force of traditional law, often referred to as hard law, in this context. The term soft law initially appeared in the area of international law, but more recently it has been transferred to other branches of law.")
Regulation.comment.append(
    "A regulation bears one or more norms, all of which are uttered by some legislative body. It cannot bear expressions which are not uttered by a legislative body.")
CodeOfConduct.comment.append(
    "a code outlining the responsibilities of or best practice for an individual or organisation, such as a set of principles of good corporate behaviour adopted by a business")
NormativelyQualified.comment.append(
    "Some thing which is qualified (allowed, disallowed) by a norm, i.e. a norm applies to the thing. Taking the principle of deontic choice to mean that the utterer of a normative statement intends to influence choices made by the addressee of the statement, the qualified thing should is comparable to some alternative. Note that Qualified does not partition into Allowed and Disallowed. Firstly, things can be Allowed by one Norm and Disallowed by another one. Secondly, the logical complement of the thing allowed by a permission is qualified (as worse or equal than the thing allowed), but neither allowed nor disallowed.")
HohfeldianPower.comment.append("A hohfeldian power covers any action which determines a legal effect.")
disallowed_by.comment.append("Relates a qualified Disallowed to the norm disallowing it")
allowed_by.comment.append("Relates a qualified Allowed to the norm allowing it")
allows.comment.append("Relates a norm to the thing it allows")
disallows.comment.append("Relates a norm to the thing it disallows")
