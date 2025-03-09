from owlready2 import *

from core.lkif_model import _my_ontology
from action import Agent, Creation
from process import creation
from role import counts_as, imposed_on, played_by, EpistemicRole, plays
from lkif_top import MentalObject

onto = _my_ontology()


class Reason(Thing):
    ontology = onto


class Argument(Thing):
    ontology = onto


class Cause(EpistemicRole):
    ontology = onto


class Belief(Thing):
    ontology = onto


class CommunicatedAttitude:
    ontology = onto


class EvaluativeAttitude:
    ontology = onto


class Evidence:
    ontology = onto


class Exception:
    ontology = onto


class Expectation:
    ontology = onto

class Intention:
    ontology = onto

class Expression:
    ontology = onto

class Fact:
    ontology = onto

class Promise(CommunicatedAttitude):
    ontology = onto

class Observation(EpistemicRole):
    ontology = onto

class Problem(Observation):
    ontology = onto

class EvaluativeProposition:
    ontology = onto

class Proposition(Thing):
    ontology = onto

class PropositionalAttitude:
    ontology = onto

class Desire(PropositionalAttitude):
    ontology = onto

class Declaration(CommunicatedAttitude):
    ontology = onto

class Qualification(Thing):
    ontology = onto

class Qualified(Thing):
    ontology = onto

class Document(Thing):
    ontology = onto

class Medium(Thing):
    ontology = onto

class Assertion(CommunicatedAttitude):
    ontology = onto

class Lie(Assertion):
    ontology = onto

class SpeechAct(Creation):
    ontology = onto

class Surprise(Observation):
    ontology = onto

class StatementInWriting(Thing):
    ontology = onto

class Assumption(Thing):
    ontology = onto


class states(ObjectProperty):
    ontology = onto


class stated_by(ObjectProperty):
    ontology = onto


class addressee(ObjectProperty):
    ontology = onto
    domain = [CommunicatedAttitude]
    range = [Agent]


class asserted_by(ObjectProperty):
    ontology = onto
    domain = [Expression]
    range = [Agent]


class asserts(states):
    ontology = onto
    domain = [Assertion]
    range = [Expression]
    inverse_property = asserted_by


class towards(imposed_on):
    ontology = onto
    range = [Proposition]
    domain = [PropositionalAttitude]


class attitude(counts_as):
    ontology = onto
    domain = [Proposition]
    range = [PropositionalAttitude]
    inverse_property = towards

class bears(ObjectProperty):
    ontology = onto
    domain = [Medium]
    range = [Expression]


class declared_by(stated_by):
    ontology = onto
    range = [Declaration]
    domain = [Expression]


class declares(states):
    ontology = onto
    domain = [Declaration]
    range = [Expression]
    inverse_property = declared_by



class held_by(ObjectProperty):
    ontology = onto
    domain = [MentalObject]
    range = [Agent]


class holds(ObjectProperty):
    ontology = onto
    domain = [Agent]
    range = [MentalObject]
    inverse_property = held_by


class utterer(held_by):
    ontology = onto
    range = [Agent]
    domain = [CommunicatedAttitude]


class utters(holds):
    ontology = onto
    domain = [Agent]
    range = [CommunicatedAttitude]
    inverse_property = utterer

class author(utterer):
    ontology = onto


class believed_by(held_by):
    ontology = onto
    domain = [Belief]
    range = [Agent]


class believes(holds):
    ontology = onto
    domain = [Agent]
    range = [Belief]
    inverse_property = believed_by


class intended_by(held_by):
    ontology = onto
    range = [Agent]
    domain = [Intention]


class intends(holds):
    ontology = onto
    domain = [Agent]
    range = [Intention]
    inverse_property = intended_by


class medium(ObjectProperty):
    ontology = onto
    domain = [Expression]
    range = [Medium]
    inverse_property = bears


class observer(believed_by):
    ontology = onto
    range = [Agent]
    domain = [Belief]


class observes(believes):
    ontology = onto
    domain = [Agent]
    range = [Belief]
    inverse_property = observer


class promised_by(stated_by):
    ontology = onto
    domain = [Expression]
    range = [Promise]


class promises(states):
    ontology = onto
    range = [Expression]
    domain = [Promise]
    inverse_property = promised_by


class qualified_by(ObjectProperty):
    ontology = onto
    domain = [Qualified]
    range = [Qualification]


class qualifies(ObjectProperty):
    ontology = onto
    domain = [Qualification]
    range = [Qualified]
    inverse_property = qualified_by


class qualitatively_comparable(SymmetricProperty):
    ontology = onto
    domain = [Qualified]
    range = [Qualified]


class evaluated_by(attitude, qualified_by):
    ontology = onto
    domain = [EvaluativeProposition]
    range = [EvaluativeAttitude]


class evaluates(qualifies, towards):
    ontology = onto
    domain = [EvaluativeAttitude]
    range = [EvaluativeProposition]
    inverse_property = evaluated_by


class evaluatively_comparable(qualitatively_comparable, SymmetricProperty):
    ontology = onto
    domain = [EvaluativeProposition]
    range = [EvaluativeProposition]

class stated_by(attitude):
    ontology = onto
    range = [CommunicatedAttitude]


class state(towards):
    ontology = onto
    domain = [CommunicatedAttitude]
    inverse_property = stated_by


AllDisjoint([Expectation, Observation])

gca_reason = GeneralClassAxiom(EpistemicRole & played_by.some(Proposition & attitude.some(Belief)))
gca_reason.is_a.append(Reason)

gca_argument = GeneralClassAxiom(Reason & played_by.some(Expression & attitude.some(Belief)))
gca_argument.is_a.append(Argument)

gca_assumption = GeneralClassAxiom(EpistemicRole & played_by.some(Proposition & attitude.some(Belief)))
gca_assumption.is_a.append(Assumption)

gca_belief = GeneralClassAxiom(PropositionalAttitude & believed_by.all(Agent))
gca_belief.is_a.append(Belief)

gca_ca = GeneralClassAxiom(
    PropositionalAttitude & states.all(Expression) & addressee.some(Agent) & addressee.all(Agent) & utterer.some(Agent))
gca_ca.is_a.append(CommunicatedAttitude)

gca_aa = GeneralClassAxiom(PropositionalAttitude & evaluates.all(EvaluativeProposition))
gca_aa.is_a.append(EvaluativeAttitude)

gca_document = GeneralClassAxiom(Medium & bears.all(Expression & stated_by.some(StatementInWriting)))
gca_document.is_a.append(Document)

gca_pa = GeneralClassAxiom(
    Proposition & evaluatively_comparable.all(EvaluativeProposition) & evaluatively_comparable.some(
        EvaluativeProposition))
gca_pa.is_a.append(EvaluativeProposition)

gca_evidence = GeneralClassAxiom(
    EpistemicRole & played_by.some(Proposition & attitude.some(Belief) & plays.some(Observation)))
gca_evidence.is_a.append(Evidence)

gca_exception = GeneralClassAxiom(EpistemicRole & played_by.some(Proposition))
gca_exception.is_a.append(Exception)

gca_expectation = GeneralClassAxiom(EpistemicRole & played_by.all(plays.all(Not(Observation))) &
                                    played_by.some(Proposition & attitude.some(Belief)))
gca_expectation.is_a.append(Expectation)

gca_expression = GeneralClassAxiom(Proposition & medium.all(Medium) & stated_by.all(CommunicatedAttitude) & stated_by.some(CommunicatedAttitude))
gca_expression.is_a.append(Expression)

gca_fact = GeneralClassAxiom(EpistemicRole & played_by.some(Proposition & attitude.some(Belief) & plays.some(Observation)))
gca_fact.is_a.append(Fact)

gca_intention = GeneralClassAxiom(PropositionalAttitude & intended_by.all(Agent))
gca_intention.is_a.append(Intention)

gca_medium = GeneralClassAxiom(Thing & bears.all(Expression))
gca_medium.is_a.append(Medium)

gca_proposition = GeneralClassAxiom(MentalObject & attitude.all(PropositionalAttitude))
gca_proposition.is_a.append(Proposition)

gca_ppa = GeneralClassAxiom(MentalObject & towards.all(Proposition))
gca_ppa.is_a.append(PropositionalAttitude)

gca_qualification = GeneralClassAxiom(MentalObject & qualifies.all(Qualified))
gca_qualification.is_a.append(Qualification)

gca_qualified = GeneralClassAxiom(And([Thing & qualitatively_comparable.some(Qualified), qualitatively_comparable.all(Qualified)]))
gca_qualified.is_a.append(Qualified)

gca_siw = GeneralClassAxiom(CommunicatedAttitude & author.some(Agent))
gca_siw.is_a.append(StatementInWriting)

gca_surprise = GeneralClassAxiom(held_by.all(Agent))
gca_surprise.is_a.append(Surprise)

Surprise.is_a.append(held_by.some(Agent))
StatementInWriting.is_a.append(states.some(Expression & medium.some(Document)))
SpeechAct.is_a.append(creation.some(CommunicatedAttitude))
Qualified.is_a.append(qualified_by.some(Qualification))
Qualification.is_a.append(qualifies.some(Qualified))
PropositionalAttitude.is_a.append(towards.some(Proposition))
Promise.is_a.append(promises.some(Expression))
Observation.is_a.append(played_by.some(attitude.some(observer.some(Agent))))
Medium.is_a.append(bears.some(Expression))
Intention.is_a.append(intended_by.some(Agent))
Expression.is_a.append(medium.some(Medium))
EvaluativeProposition.is_a.append(evaluated_by.some(EvaluativeAttitude))
EvaluativeAttitude.is_a.append(evaluates.some(EvaluativeProposition))
Assertion.is_a.append(asserts.some(Expression))
Belief.is_a.append(believed_by.some(Agent))
CommunicatedAttitude.is_a.append(states.some(Expression))
Declaration.is_a.append(declares.some(Expression))

qualitatively_comparable.inverse_property = qualitatively_comparable
evaluatively_comparable.inverse_property = evaluatively_comparable

Surprise.comment.append("Not to be confused with the actual writing/document itself, which is the medium of the statement.")
StatementInWriting.comment.append("Not to be confused with the actual writing/document itself, which is the medium of the statement.")
SpeechAct.comment.append("A speech act (or illocutionary act) creates some propositional attitude which qualifies an expression (which by default is mediated through some medium). The actor of the speech act is the utterer of the atitude (NB cannot be expressed in OWL DL).")
Reason.comment.append("Teleological counterpart of cause")
Qualified.comment.append("Something that is qualified by some qualification")
Qualification.comment.append("A qualification expresses e.g. a judgment. The thing qualified by the qualification is comparable to something else.")
PropositionalAttitude.comment.append("A propositional attitude connects a person (the holder of the attitude) to some proposition, in fact it expresses some qualification over the proposition. Distinguishing a proposition from the propositional content expressed by it is necessary when properties relating to the thing expressed and properties of the expression itself must be distinguished. For LKIF the distinction between Belief, Intention, Qualification, and Observation is relevant. The distinction between belief/expectation, intention, and observation is relevant for i.a. establishing mens rea (guilty mind). The distinction between beliefs (expressing the content of the mind of an agent) and statements (expressing the content of an act of communication by an agent) is classical.")
Proposition.comment.append("A (non logical) proposition is a proposition qualified by a propositional attitude. NB: The proposition used here does not correspond to a proposition in proposition logics.")
Promise.comment.append("A promise is a communicated attitude about some future action or state")
Problem.comment.append("A problem is an observation that deviates from an Intention.")
Observation.comment.append("An observation is the role played by some proposition believed to be true or false through observation of an agent.")
Medium.comment.append("A medium is a bearer of expressions, i.e. externalised propositions. Propositions become expressions once they are externalised through some medium.")
Lie.comment.append("An assertion that is inconsistent with the beliefs of the speaker. It is *intentionally* false.")
Intention.comment.append("Intention is where the agent expects certain consequences of his or her actions and desires those consequences to occur. This concept must be related to qualification and preference in some way.")
Fact.comment.append("A fact is a proposition (about something) which is (commonly) agreed upon to hold as true: it has some backing in evidence")
Expression.comment.append(
    "An expression is a proposition beared by some medium, e.g. a document, and is stated by some communicated attitude")
Expectation.comment.append(
    "An expectation is a predictive belief held on purely logical grounds, i.e. not based on direct external evidence, like an observation or a statement by another agent. It is also often characterized as a belief about the future, but this isn't very helpful since one may also hold expectations about the (yet unknown) past. The theory of evolution is for instance a fertile ground for predictions about the existence of past species, and therefore at the same a predictor of future observations.",
    "Is not only not an observation by itself, but also the thing being expected cannot be an observation in any sense")
Exception.comment.append(
    "An exception is something that is excluded from a general statement or does not follow a rule. In LKIF rules, an exception is a rule which has an exception relation to another rule (cf. Deliverable 1.1)")
Evidence.comment.append(
    "Observation and/or statement, used as a backing for a belief. Evidence is the role of observation which is qualified by some belief.")
EvaluativeProposition.comment.append(
    "Some thing which is evaluatively qualified, i.e. an evaluation applies to the proposition, the proposition is judged. The proposition is comparable to some other proposition.")
EvaluativeAttitude.comment.append(
    "An evaluative attitude expresses e.g. a judgment. The proposition qualified by the evaluative attitude is comparable to something else.")
Document.comment.append("A Document bears some (and only) expression(s) stated by some statement in writing.")
Desire.comment.append("A feeling of wanting")
Declaration.comment.append(
    "Searle: the successful performance of a declaration is sufficient to bring about the fit between words and world, to make the propositional content true. In other words, if there is an inconsistency between the declaration and assertions, beliefs, or observations, it is not the declaration that is false. True of definitions and norms, and several other performative statements by legislators.")
CommunicatedAttitude.comment.append(
    "A communictated attitude is a propositional attitude involved in an act of communication.")
Cause.comment.append("A cause is an epistemic role played by something which is the outcome of a (chain) of processes")
Belief.comment.append("Something an agent 'believes in', i.e. holds as true")
Assumption.comment.append(
    "proposes something that usually is the case, although there is no specific evidence that it is true in this particular case")
Assertion.comment.append(
    "The assertion is subject to a fit between words and world, in Searle's terms. It's propositional content can be true of false. If it is inconsistent with other assertions, beliefs, observations, it may come to be considered false.")
Argument.comment.append("An argument is a reason that is expressed through some medium")

utters.comment.append("Relates an agent to its utterance(s)")
utterer.comment.append("Relates an utterance (communicated propositional attitude) to its utterer")
towards.comment.append(
    "A towards relation between a propositional attitude and a proposition expresses that the attitude is held towards that proposition. Qualification of the proposition can be either true or false, i.e. the attitude denotes whether the proposition is either true or false.")
states.comment.append("Relates an author to its statements")
stated_by.comment.append("Relates a statement to its author")
qualifies.comment.append("Relates an evaluative attitude or qualification to the proposition or thing being qualified")
qualified_by.comment.append("Relates something which is qualified to the attitude or qualification qualifying it")
promises.comment.append("Relates a promise to the expression being promised")
promised_by.comment.append("Relates an expression to the promise over the expression")
observes.comment.append("Relates an agent to the thing it beliefs it observes")
observer.comment.append("Relates a believed observation to the agent observing it")
medium.comment.append("Relates an expression to the medium it is beared in (i.e. for extentional propositions)")
intends.comment.append("Specifies that the agent holds some intention")
intended_by.comment.append("Specifies that some intention is held by some agent")
holds.comment.append("Relates an agent to the propositional attitude it holds")
held_by.comment.append("Relates a propositional attitude to the agent holding the attitude")
evaluatively_comparable.comment.append("Expresses whether some thing is evaluatively comparable to some other thing.")
declares.comment.append("Relates a declaration to the expression being declared")
declared_by.comment.append("Relates a declared expression to the attitude to the declaration")
believed_by.comment.append("Relates a belief to the agent holding the belief")
bears.comment.append("A Medium 'bears' or carries expressions.")
author.comment.append(
    "Relates an expression to the author of the expression (e.g. for expressions contained in documents)")
attitude.comment.append("Relates a proposition to the attitude held towards it")
asserts.comment.append("Relates an assertion to the expression being asserted")
asserted_by.comment.append("Relates an expression being asserted to the assertion")
addressee.comment.append(
    "Allows for expressing the relation between a communicated attitude and the Agent to which the communication act is addressed")
