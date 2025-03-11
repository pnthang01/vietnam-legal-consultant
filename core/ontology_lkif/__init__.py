import types

from owlready2 import *
import i18n

i18n.load_path.append('../../resources/i18n')

onto_path.append("./")

# onto = get_ontology("http://www.estrellaproject.org/lkif-core/lkif-top.owl").load()
onto = default_world.get_ontology("file://./lkif-top.owl").load()

with onto:

    #action.owl
    class Action(Process):
        comment = i18n.t("lkif.comment.Action")
    class Agent(Thing):
        comment = i18n.t("lkif.comment.Agent")
    class Artifact(PhysicalObject):
        comment = i18n.t("lkif.comment.Artifact")
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
    class Plan(MentalObject):
        comment = i18n.t("lkif.comment.Plan")
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

    class member_of(Person >> Organisation):
        pass
    class member(Organisation >> Person):
        inverse = member_of

Org_01 = Organisation("Org1")
Anna = Person("Anna", member_of=[Org_01])

print(Anna.member_of)
print(Org_01.member)