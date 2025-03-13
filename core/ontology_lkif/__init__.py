import types

from owlready2 import *
import i18n

i18n.load_path.append('../../resources/i18n')

onto_path.append("./")

# onto = get_ontology("http://www.estrellaproject.org/lkif-core/lkif-top.owl").load()
# onto = default_world.get_ontology("file://./time.owl").load()
onto = get_ontology("http://test.org/LKIF#")

with onto:
    #lkif-top.owl
    class AbstractEntity(Thing):
        comment = i18n.t('lkif.comment.AbstractEntity')
    class MentalEntity(Thing):
        comment = i18n.t('lkif.comment.MentalEntity')
    class MentalObject(MentalEntity):
        comment = i18n.t('lkif.comment.MentalObject')
    class Occurrence(Thing):
        comment = i18n.t('lkif.comment.Occurrence')
    class PhysicalEntity(Thing):
        comment = i18n.t('lkif.comment.PhysicalEntity')
    class SpatioTemporalOccurrence(Occurrence):
        comment = i18n.t('lkif.comment.SpatioTemporalOccurrence')
    #mereology.owl
    class Atom(AbstractEntity):
        comment = i18n.t('lkif.comment.Atom')
    class Part(AbstractEntity):
        comment = i18n.t('lkif.comment.Part')
    class Whole(AbstractEntity):
        comment = i18n.t('lkif.comment.Whole')
    class Composition(Whole):
        comment = i18n.t('lkif.comment.Composition')
    class Pair(Composition):
        comment = i18n.t('lkif.comment.Pair')
    class part(TransitiveProperty):
        comment = i18n.t('lkif.comment.part')
    class part_of(TransitiveProperty):
        comment = i18n.t('lkif.comment.part_of')
        inverse_property = part
    class strict_part(part, ObjectProperty):
        comment = i18n.t('lkif.comment.strict_part')
    class strict_part_of(part_of, ObjectProperty):
        comment = i18n.t('lkif.comment.strict_part_of')
        inverse_property = strict_part
    class component(ObjectProperty, strict_part):
        comment = i18n.t('lkif.comment.component')
    class component_of(ObjectProperty, strict_part_of):
        comment = i18n.t('lkif.comment.component_of')
        inverse_property = component
    class composed_of(part, TransitiveProperty):
        comment = i18n.t('lkif.comment.composed_of')
    class composes(part_of, TransitiveProperty):
        comment = i18n.t('lkif.comment.composes')
        inverse_property = composed_of
    class contained_in(part_of, TransitiveProperty):
        comment = i18n.t('lkif.comment.contained_in')
    class contains(part, TransitiveProperty):
        comment = i18n.t('lkif.comment.contains')
        inverse_property = contained_in
    class direct_part(part, ObjectProperty):
        comment = i18n.t('lkif.comment.direct_part')
    direct_part.equivalent_to.append(strict_part)
    class direct_part_of(part_of, ObjectProperty):
        comment = i18n.t('lkif.comment.direct_part_of')
        inverse_property = direct_part
    direct_part_of.equivalent_to.append(strict_part_of)
    class member_of(strict_part_of, ObjectProperty):
        comment = i18n.t('lkif.comment.member_of')
    class member(strict_part, ObjectProperty):
        comment = i18n.t('lkif.comment.member')
        inverse_property = member_of
    Pair.is_a.append(strict_part.exactly(2, Part))
    Part.is_a.append(strict_part_of.some(Whole))
    Part.is_a.append(strict_part_of.only(Whole))
    Whole.is_a.append(strict_part.some(Part))
    Whole.is_a.append(strict_part.only(Part))
    AllDisjoint([Atom, Whole])
    #time.owl
    class TemporalOccurrence(SpatioTemporalOccurrence):
        comment = i18n.t('lkif.comment.TemporalOccurrence')
    class Interval(Composition, TemporalOccurrence):
        comment = i18n.t('lkif.comment.Interval')
    class Moment(Atom, TemporalOccurrence):
        comment = i18n.t('lkif.comment.Moment')
    class PairOfPeriods(Pair):
        comment = i18n.t('lkif.comment.PairOfPeriods')
    class temporal_relation(ObjectProperty):
        domain = [TemporalOccurrence]
        range = [TemporalOccurrence]
        comment = i18n.t('lkif.comment.temporal_relation')
    class after(TransitiveProperty, temporal_relation):
        domain = [TemporalOccurrence]
        range = [TemporalOccurrence]
        comment = i18n.t('lkif.comment.after')
    class before(TransitiveProperty, temporal_relation):
        domain = [TemporalOccurrence]
        range = [TemporalOccurrence]
        inverse_property = after
        comment = i18n.t('lkif.comment.before')
    class between(ObjectProperty, temporal_relation):
        domain = [TemporalOccurrence]
        range = [PairOfPeriods]
        comment = i18n.t('lkif.comment.between')
    class during(ObjectProperty, temporal_relation):
        comment = i18n.t('lkif.comment.during')
    class finishes(ObjectProperty, temporal_relation):
        comment = i18n.t('lkif.comment.finishes')
    class immediately_after(ObjectProperty, after):
        domain = [TemporalOccurrence]
        range = [TemporalOccurrence]
        comment = i18n.t('lkif.comment.immediately_after')
    class immediately_before(ObjectProperty, before):
        domain = [TemporalOccurrence]
        range = [TemporalOccurrence]
        inverse_property = immediately_after
        comment = i18n.t('lkif.comment.immediately_before')
    class overlap(ObjectProperty):
        comment = i18n.t('lkif.comment.overlap')
    class preceeds(ObjectProperty, temporal_relation):
        comment = i18n.t('lkif.comment.preceeds')
    class starts(ObjectProperty, temporal_relation):
        comment = i18n.t('lkif.comment.starts')
    PairOfPeriods.is_a.append(component.only(TemporalOccurrence))
    TemporalOccurrence.is_a.append(And([immediately_before.some(TemporalOccurrence), immediately_after.some(TemporalOccurrence)]))
    AllDisjoint([Interval, Moment])
    #process.owl
    class Change(Thing):
        comment = i18n.t("lkif.comment.Change")
    class Process(Change):
        comment = i18n.t("lkif.comment.Process")
    class Continuation(Change):
        comment = i18n.t("lkif.comment.Continuation")
    class Initiation(Change):
        comment = i18n.t("lkif.comment.Initiation")
    class MentalProcess(MentalEntity, Process):
        comment = i18n.t("lkif.comment.MentalProcess")
    class PhysicalObject(PhysicalEntity):
        comment = i18n.t("lkif.comment.PhysicalObject")
    class PhysicalProcess(Process, PhysicalEntity):
        comment = i18n.t("lkif.comment.PhysicalProcess")
    class Termination(Change):
        comment = i18n.t("lkif.comment.Termination")
    class participant(ObjectProperty):
        comment = i18n.t("lkif.comment.participant")
        domain = [Change]
        range = [Thing]
    class participant_in(ObjectProperty):
        comment = i18n.t("lkif.comment.participant_in")
        domain = [Thing]
        range = [Change]
        inverse_property = participant
    class requirement(participant, ObjectProperty):
        comment = i18n.t("lkif.comment.requirement")
    class requirement_of(participant_in, ObjectProperty):
        comment = i18n.t("lkif.comment.requirement_of")
        inverse_property = requirement
    class resource(participant, ObjectProperty):
        comment = i18n.t("lkif.comment.resource")
    class resource_for(participant_in, ObjectProperty):
        comment = i18n.t("lkif.comment.resource_for")
        inverse_property = resource
    class result(participant, ObjectProperty):
        comment = i18n.t("lkif.comment.result")
    class result_of(participant_in, ObjectProperty):
        comment = i18n.t("lkif.comment.result_of")
        inverse_property = result
    class created_by(result_of, ObjectProperty):
        comment = i18n.t("lkif.comment.created_by")
    class creation(result, ObjectProperty):
        inverse_property = created_by
        comment = i18n.t("lkif.comment.creation")
    Change.is_a.append(result.some(Thing))
    Change.is_a.append(requirement.some(Thing))
    Continuation.is_a.append(requirement.some(Initiation))
    Continuation.is_a.append(direct_part_of.some(Change))
    Initiation.is_a.append(result.some(Continuation))
    Initiation.is_a.append(direct_part_of.some(Change))
    Process.is_a.append(resource.some(TemporalOccurrence))
    Termination.is_a.append(requirement.some(Continuation))
    Termination.is_a.append(direct_part_of.some(Change))
    AllDisjoint([Change, PhysicalObject])
    #action.owl
    class Action(Process):
        comment = i18n.t("lkif.comment.Action")
    class Agent(Thing):
        comment = i18n.t("lkif.comment.Agent")
    class Artifact(PhysicalObject):
        comment = i18n.t("lkif.comment.Artifact")
    class Plan(MentalObject):
        comment = i18n.t("lkif.comment.Plan")
    class CollaborativePlan(Plan):
        comment = i18n.t("lkif.comment.CollaborativePlan")
    class Creation(Action):
        comment = i18n.t("lkif.comment.Creation")
    class NaturalObject(PhysicalObject):
        comment = i18n.t("lkif.comment.NaturalObject")
    class Organisation(Agent):
        comment = i18n.t("lkif.comment.Organisation")
    class Person(Agent, NaturalObject):
        comment = i18n.t("lkif.comment.Person")
    class PersonalPlan(Plan):
        comment = i18n.t("lkif.comment.PersonalPlan")
    class Reaction(Action):
        comment = i18n.t("lkif.comment.Reaction")
    class Transaction(CollaborativePlan):
        comment = i18n.t("lkif.comment.Transaction")
    class Trade(Transaction):
        comment = i18n.t("lkif.comment.Trade")
    class actor(participant):
        domain = [Action]
        range = [Agent]
        comment = i18n.t("lkif.comment.actor")
    class actor_in(participant_in):
        domain = [Agent]
        range = [Action]
        inverse_property = actor
        comment = i18n.t("lkif.comment.actor_in")
    Action.equivalent_to.append(actor.exactly(1))
    Action.is_a.append(actor.only(Agent))
    Agent.equivalent_to.append(actor_in.some(Action))
    Agent.is_a.append(actor_in.only(Action))
    Agent.is_a.append(participant_in.only(Change))
    Artifact.is_a.append(result_of.some(Creation))
    Creation.is_a.append(creation.min(1))
    Organisation.is_a.append(member.some(Person))
    Organisation.is_a.append(member.only(Or([Person, Organisation])))
    Plan.is_a.append(part.some(Action))
    Plan.is_a.append(part.only(Or([Action, Plan])))
    Transaction.is_a.append(direct_part.only(Action))
    Transaction.is_a.append(direct_part.exactly(2))
    AllDisjoint([Action, Plan])
    AllDisjoint([Agent, Change])
    AllDisjoint([Artifact, NaturalObject])
    AllDisjoint([Artifact, Person])
    AllDisjoint([CollaborativePlan, PersonalPlan])
    AllDisjoint([Organisation, Person])
    AllDisjoint([Change, PhysicalObject])
    #end action.owl
    #role.owl
    class SubjectiveEntity(MentalEntity):
        comment = i18n.t("lkif.comment.SubjectiveEntity")
    class Role(SubjectiveEntity):
        comment = i18n.t("lkif.comment.Role")
    class SocialRole(Role):
        comment = i18n.t("lkif.comment.SocialRole")
    class PersonRole(SocialRole):
        comment = i18n.t("lkif.comment.PersonRole")
    class OrganisationRole(SocialRole):
        comment = i18n.t("lkif.comment.OrganisationRole")
    class Function(Role):
        comment = i18n.t("lkif.comment.Function")
    class EpistemicRole(Role):
        comment = i18n.t("lkif.comment.EpistemicRole")
    class imposed_on(FunctionalProperty):
        comment = i18n.t("lkif.comment.imposed_on")
    class counts_as(ObjectProperty):
        comment = i18n.t("lkif.comment.counts_as")
    class plays(ObjectProperty, counts_as):
        comment = i18n.t("lkif.comment.plays")
        domain = [Thing]
        range = [Role]
    class played_by(ObjectProperty, imposed_on):
        comment = i18n.t("lkif.comment.played_by")
        domain = [Role]
        range = [Thing]
        inverse_property = plays
    class context(FunctionalProperty):
        comment = i18n.t("lkif.comment.context")
    AllDisjoint([context, imposed_on])
    AllDisjoint([Function, SocialRole])
    AllDisjoint([Process, Role])
    AllDisjoint([Role, PhysicalEntity])
    AllDisjoint([Role, Agent])
    SubjectiveEntity.is_a.append(And([context.some(Thing), imposed_on.some(Thing)]))
    Role.is_a.append(played_by.some(Thing))
    SocialRole.is_a.append(played_by.only(Agent))
    SocialRole.is_a.append(played_by.some(Agent))
    PersonRole.is_a.append(played_by.only(Person))
    PersonRole.is_a.append(played_by.some(Person))
    OrganisationRole.is_a.append(played_by.only(And([Agent, member_of.some(Organisation)])))
    Function.is_a.append(played_by.only(And([PhysicalObject, Not(Agent)])))
    Function.is_a.append(played_by.some(PhysicalObject))
    EpistemicRole.is_a.append(played_by.only(MentalObject))
    EpistemicRole.is_a.append(played_by.some(MentalObject))
    EpistemicRole.is_a.append(context.some(MentalProcess))
    Organisation.is_a.append(member.only(plays.some(OrganisationRole)))
    Artifact.is_a.append(plays.some(Function))
    Agent.is_a.append(plays.only(Role))
    Action.is_a.append(actor.only(plays.some(Role)))
    #end role.owl
    #expression.owl
    class PropositionalAttitude(MentalObject):
        comment = i18n.t("lkif.comment.PropositionalAttitude")
    class EvaluativeAttitude(PropositionalAttitude):
        comment = i18n.t("lkif.comment.EvaluativeAttitude")
    class Qualification(MentalObject):
        comment = i18n.t("lkif.comment.Qualification")
    class Qualified(Thing):
        comment = i18n.t("lkif.comment.Qualified")
    class Reason(EpistemicRole):
        comment = i18n.t("lkif.comment.Reason")
    class SpeechAct(Creation):
        comment = i18n.t("lkif.comment.SpeechAct")
    class Argument(Reason):
        comment = i18n.t("lkif.comment.Argument")
    class Assumption(EpistemicRole):
        comment = i18n.t("lkif.comment.Assumption")
    class Belief(PropositionalAttitude):
        comment = i18n.t("lkif.comment.Belief")
    class Cause(EpistemicRole):
        comment = i18n.t("lkif.comment.Cause")
    class CommunicatedAttitude(PropositionalAttitude):
        comment = i18n.t("lkif.comment.CommunicatedAttitude")
    class StatementInWriting(CommunicatedAttitude):
        comment = i18n.t("lkif.comment.StatementInWriting")
    class Assertion(CommunicatedAttitude):
        comment = i18n.t("lkif.comment.Assertion")
    class Declaration(CommunicatedAttitude):
        comment = i18n.t("lkif.comment.Declaration")
    class Desire(PropositionalAttitude):
        comment = i18n.t("lkif.comment.Desire")
    class Evidence(EpistemicRole):
        comment = i18n.t("lkif.comment.Evidence")
    class Exception(EpistemicRole):
        comment = i18n.t("lkif.comment.Exception")
    class Expectation(EpistemicRole):
        comment = i18n.t("lkif.comment.Expectation")
    class Fact(EpistemicRole):
        comment = i18n.t("lkif.comment.Fact")
    class Intention(PropositionalAttitude):
        comment = i18n.t("lkif.comment.Intention")
    class Lie(Assertion):
        comment = i18n.t("lkif.comment.Lie")
    class Medium(Thing):
        comment = i18n.t("lkif.comment.Medium")
    class Document(Medium):
        comment = i18n.t("lkif.comment.Document")
    class Observation(EpistemicRole):
        comment = i18n.t("lkif.comment.Observation")
    class Surprise(Observation):
        comment = i18n.t("lkif.comment.Surprise")
    class Problem(Observation):
        comment = i18n.t("lkif.comment.Problem")
    class Promise(CommunicatedAttitude):
        comment = i18n.t("lkif.comment.Promise")
    class Proposition(MentalObject):
        comment = i18n.t("lkif.comment.Proposition")
    class Expression(Proposition):
        comment = i18n.t("lkif.comment.Expression")
    class EvaluativeProposition(Proposition):
        comment = i18n.t("lkif.comment.EvaluativeProposition")
    class addressee(ObjectProperty):
        comment = i18n.t("lkif.comment.addressee")
        domain = [CommunicatedAttitude]
        range = [Agent]
    class towards(imposed_on):
        comment = i18n.t("lkif.comment.towards")
        domain = [PropositionalAttitude]
        range = [Proposition]
    class attitude(counts_as):
        comment = i18n.t("lkif.comment.attitude")
        domain = [Proposition]
        range = [PropositionalAttitude]
        inverse_property = towards
    class qualitatively_comparable(SymmetricProperty):
        comment = i18n.t("lkif.comment.qualitatively_comparable")
        domain = [Qualified]
        range = [Qualified]
        inverse_property = None
    Inverse(qualitatively_comparable)
    class stated_by(attitude):
        comment = i18n.t("lkif.comment.stated_by")
        range = [CommunicatedAttitude]
    class states(towards):
        comment = i18n.t("lkif.comment.states")
        domain = [CommunicatedAttitude]
        inverse_property = stated_by
    class asserted_by(stated_by):
        comment = i18n.t("lkif.comment.asserted_by")
        range = [Assertion]
        domain = [Expression]
    class asserts(states):
        comment = i18n.t("lkif.comment.asserts")
        domain = [Assertion]
        range = [Expression]
        inverse_property = asserted_by
    class bears(ObjectProperty):
        comment = i18n.t("lkif.comment.bears")
        domain = [Medium]
        range = [Expression]
    class declared_by(stated_by):
        comment = i18n.t("lkif.comment.declared_by")
        domain = [Expression]
        range = [Declaration]
    class declares(states):
        comment = i18n.t("lkif.comment.declares")
        domain = [Declaration]
        range = [Expression]
        inverse_property = declared_by
    class qualified_by(ObjectProperty):
        comment = i18n.t("lkif.comment.qualified_by")
        domain = [Qualified]
        range = [Qualification]
    class qualifies(ObjectProperty):
        comment = i18n.t("lkif.comment.qualifier")
        domain = [Qualification]
        range = [Qualified]
        inverse_property = qualified_by
    class evaluated_by(qualified_by, attitude):
        comment = i18n.t("lkif.comment.evaluated_by")
        domain = [EvaluativeProposition]
        range = [EvaluativeAttitude]
    class evaluates(qualifies, towards):
        comment = i18n.t("lkif.comment.evaluates")
        domain = [EvaluativeAttitude]
        range = [EvaluativeProposition]
        inverse_property = evaluated_by
    class evaluatively_comparable(SymmetricProperty, qualitatively_comparable):
        comment = i18n.t("lkif.comment.evaluatively_comparable")
        domain = [EvaluativeProposition]
        range = [EvaluativeProposition]
    Inverse(evaluatively_comparable)
    class held_by(ObjectProperty):
        comment = i18n.t("lkif.comment.held_by")
        domain = [MentalObject]
        range = [Agent]
    class holds(ObjectProperty):
        comment = i18n.t("lkif.comment.holds")
        domain = [Agent]
        range = [MentalObject]
        inverse_property = held_by
    class utterer(held_by):
        comment = i18n.t("lkif.comment.utterer")
        domain = [CommunicatedAttitude]
        range = [Agent]
    class utters(holds):
        comment = i18n.t("lkif.comment.utters")
        domain = [Agent]
        range = [CommunicatedAttitude]
        inverse_property = utterer
    class believed_by(held_by):
        comment = i18n.t("lkif.comment.believed_by")
        domain = [Belief]
        range = [Agent]
    class believes(holds):
        comment = i18n.t("lkif.comment.believes")
        domain = [Agent]
        range = [Belief]
        inverse_property = believed_by
    class intended_by(held_by):
        comment = i18n.t("lkif.comment.intended_by")
        domain = [Intention]
        range = [Agent]
    class intends(holds):
        comment = i18n.t("lkif.comment.intends")
        domain = [Agent]
        range = [Intention]
        inverse_property = intended_by
    class medium(ObjectProperty):
        comment = i18n.t("lkif.comment.medium")
        domain = [Expression]
        range = [Medium]
        inverse_property = bears
    class observer(believed_by):
        comment = i18n.t("lkif.comment.observer")
        range = [Agent]
        domain = [Belief]
    class observes(believes):
        comment = i18n.t("lkif.comment.observes")
        domain = [Agent]
        range = [Belief]
        inverse_property = observer
    class promised_by(stated_by):
        comment = i18n.t("lkif.comment.promised_by")
        domain = [Expression]
        range = [Promise]
    class promises(states):
        comment = i18n.t("lkif.comment.promises")
        domain = [Promise]
        range = [Expression]
        inverse_property = promised_by
    class author(utterer):
        comment = i18n.t("lkif.comment.author")
    Action.is_a.append(actor.only(intends.some(Intention)))
    Action.is_a.append(actor.only(believes.some(And([Belief, towards.some(plays.some(Expectation))]))))
    Agent.is_a.append(holds.only(MentalEntity))
    Reaction.is_a.append(actor.only(And([observes.some(And([Belief, qualifies.some(plays.some(And([Observation, played_by.some(Action)])))]))])))
    Argument.is_a.append(played_by.some(And([Expression, attitude.some(Belief)])))
    Assertion.is_a.append(asserts.some(Expression))
    Assumption.is_a.append(played_by.some(And([Proposition, attitude.some(Belief)])))
    Belief.is_a.append(believed_by.some(Agent))
    Belief.is_a.append(believes.only(Agent))
    CommunicatedAttitude.is_a.append(states.some(Expression))
    CommunicatedAttitude.is_a.append(states.only(Expression))
    CommunicatedAttitude.is_a.append(addressee.some(Agent))
    CommunicatedAttitude.is_a.append(addressee.only(Agent))
    CommunicatedAttitude.is_a.append(utterer.some(Agent))
    Declaration.is_a.append(declares.some(Expression))
    Document.is_a.append(bears.only(And([Expression, stated_by.some(StatementInWriting)])))
    EvaluativeAttitude.is_a.append(evaluates.some(EvaluativeProposition))
    EvaluativeAttitude.is_a.append(evaluates.only(EvaluativeProposition))
    EvaluativeProposition.is_a.append(evaluated_by.some(EvaluativeAttitude))
    EvaluativeProposition.is_a.append(evaluatively_comparable.only(EvaluativeProposition))
    EvaluativeProposition.is_a.append(evaluatively_comparable.some(EvaluativeProposition))
    Evidence.is_a.append(played_by.some(And([Proposition, attitude.some(Belief), plays.some(Observation)])))
    Exception.is_a.append(played_by.some(Proposition))
    Expectation.is_a.append(played_by.only(plays.only(Not(Observation))))
    Expectation.is_a.append(played_by.some(And([Proposition, attitude.some(Belief)])))
    Expression.is_a.append(medium.some(Medium))
    Expression.is_a.append(medium.only(Medium))
    Expression.is_a.append(stated_by.some(CommunicatedAttitude))
    Expression.is_a.append(stated_by.only(CommunicatedAttitude))
    Fact.is_a.append(played_by.some(And([Proposition, attitude.some(Belief), plays.some(Observation)])))
    Intention.is_a.append(intended_by.some(Agent))
    Intention.is_a.append(intended_by.only(Agent))
    Medium.is_a.append(bears.some(Expression))
    Medium.is_a.append(bears.only(Expression))
    Observation.is_a.append(played_by.some(attitude.some(observer.some(Agent))))
    Promise.is_a.append(promises.some(Expression))
    Proposition.is_a.append(attitude.only(PropositionalAttitude))
    PropositionalAttitude.is_a.append(towards.some(Proposition))
    PropositionalAttitude.is_a.append(towards.only(Proposition))
    Qualification.is_a.append(qualifies.some(Qualified))
    Qualification.is_a.append(qualifies.only(Qualified))
    Qualified.is_a.append(qualified_by.some(Qualification))
    Qualified.is_a.append(qualitatively_comparable.only(Qualification))
    Qualified.is_a.append(qualitatively_comparable.some(Qualification))
    Reason.is_a.append(played_by.some(And([Proposition, attitude.some(Belief)])))
    SpeechAct.is_a.append(creation.some(CommunicatedAttitude))
    StatementInWriting.is_a.append(states.some(And([Expression, medium.some(Document)])))
    StatementInWriting.is_a.append(author.some(Agent))
    MentalObject.is_a.append(held_by.some(Agent))
    MentalObject.is_a.append(held_by.only(Agent))
    AllDisjoint([Expectation, Observation])
    #Left over
    Change.is_a.append(part.only(Change))

Org_01 = Organisation("Org1")
Anna = Person("Anna", member_of=[Org_01])

print(Anna.member_of)
print(Org_01.member)