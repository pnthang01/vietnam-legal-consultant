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
    #expression.owl
    # class addressee(ObjectProperty):
    #     comment = i18n.t("lkif.comment.addressee")
    #     domain = [CommunicatedAttitude]
    #     range = [Agent]
    # class asserted_by(stated_by):
    #     comment = i18n.t("lkif.comment.asserted_by")
    #     range = [Assertion]
    #     domain = [Expression]
    # class asserts(states):
    #     comment = i18n.t("lkif.comment.asserts")
    #     domain = [Assertion]
    #     range = [Expression]
    #     inverse_property = asserted_by
    # class attitude(counts_as):
    #     comment = i18n.t("lkif.comment.attitude")
    #     domain = [Proposition]
    #     range = [PropositionalAttitude]
    #     inverse_property = towards
    # class author(utterer):
    #     comment = i18n.t("lkif.comment.author")
    # class bears(ObjectProperty):
    #     comment = i18n.t("lkif.comment.bears")
    #     domain = [Medium]
    #     range = [Expression]
    # class believed_by(held_by):
    #     comment = i18n.t("lkif.comment.believed_by")
    #     domain = [Belief]
    #     range = [Agent]
    # class believes(holds):
    #     comment = i18n.t("lkif.comment.believes")
    #     domain = [Agent]
    #     range = [Belief]
    #     inverse_property = believed_by
    # class declared_by(stated_by):
    #     comment = i18n.t("lkif.comment.declared_by")
    #     domain = [Expression]
    #     range = [Declaration]
    # class declares(states):
    #     comment = i18n.t("lkif.comment.declares")
    #     domain = [Declaration]
    #     range = [Expression]
    #     inverse_property = declared_by
    # class evaluated_by(qualified_by, attitude):
    #     comment = i18n.t("lkif.comment.evaluated_by")
    #     domain = [EvaluativeProposition]
    #     range = [EvaluativeAttitude]
    # class evaluates(qualifies, towards):
    #     comment = i18n.t("lkif.comment.evaluates")
    #     domain = [EvaluativeAttitude]
    #     range = [EvaluativeProposition]
    #     inverse_property = evaluated_by
    # class evaluatively_comparable(SymmetricProperty, qualitatively_comparable):
    #     comment = i18n.t("lkif.comment.evaluatively_comparable")
    #     domain = [EvaluativeProposition]
    #     range = [EvaluativeProposition]
    # Inverse(evaluatively_comparable)
    # class held_by(ObjectProperty):
    #     comment = i18n.t("lkif.comment.held_by")
    #     domain = [MentalObject]
    #     range = [Agent]
    # class holds(ObjectProperty):
    #     comment = i18n.t("lkif.comment.holds")
    #     domain = [Agent]
    #     range = [MentalObject]
    #     inverse_property = held_by
    # class intended_by(held_by):
    #     comment = i18n.t("lkif.comment.intended_by")
    #     domain = [Intention]
    #     range = [Agent]
    # class intends(holds):
    #     comment = i18n.t("lkif.comment.intends")
    #     domain = [Agent]
    #     range = [Intention]
    #     inverse_property = intended_by
    # class medium(ObjectProperty):
    #     comment = i18n.t("lkif.comment.medium")
    #     domain = [Expression]
    #     range = [Medium]
    #     inverse_property = bears

    #Left over
    Change.is_a.append(part.only(Change))

Org_01 = Organisation("Org1")
Anna = Person("Anna", member_of=[Org_01])

print(Anna.member_of)
print(Org_01.member)