from owlready2 import GeneralClassAxiom, Thing, AllDisjoint, OneOf

from . import _my_ontology
from .mereology import member, part, direct_part
from .process import participant, participant_in, Process, Change, PhysicalObject, result_of, creation
from .lkif_top import MentalObject

onto = _my_ontology()


class Action(Process):
    ontology = onto


class Agent(Thing):
    ontology = onto


class Plan(MentalObject):
    ontology = onto


class Artifact(PhysicalObject):
    ontology = onto


class NaturalObject(PhysicalObject):
    ontology = onto


class Person(Agent, NaturalObject):
    ontology = onto


class Organisation(Thing):
    ontology = onto


class Creation(Action):
    ontology = onto


class CollaborativePlan(Plan):
    ontology = onto


class PersonPlan(Plan):
    ontology = onto


class Reaction(Action):
    ontology = onto


class Transaction(CollaborativePlan):
    ontology = onto


class Trade(Transaction):
    ontology = onto


class actor(participant):
    ontology = onto
    domain = [Action]
    range = [Agent]


class actor_in(participant_in):
    ontology = onto
    domain = [Agent]
    range = [Action]
    inverse_property = actor


AllDisjoint([Action, Plan])
AllDisjoint([CollaborativePlan, PersonPlan])
AllDisjoint([Agent, Change])
AllDisjoint([Organisation, Person])
AllDisjoint([Artifact, Person, NaturalObject])
AllDisjoint([Change, PhysicalObject])

gca__action = GeneralClassAxiom(Process & actor.all(Agent))
gca__action.is_a.append(Action)

gca__agent = GeneralClassAxiom(Thing & actor_in.all(Action) & participant_in.all(Change))
gca__agent.is_a.append(Agent)

gca__organisation = GeneralClassAxiom(Agent & member.all(Organisation | Person))
gca__organisation.is_a.append(Organisation)

gca__plan = GeneralClassAxiom(MentalObject & part.all(Action | Plan))
gca__plan.is_a.append(Plan)

gca__transaction = GeneralClassAxiom(CollaborativePlan & direct_part.all(Action) & direct_part.exactly(2))
gca__transaction.is_a.append(Transaction)


Action.is_a.append(actor.exactly(1))
Agent.is_a.append(actor_in.some(Action))
Artifact.is_a.append(result_of.some(Creation))
Creation.is_a.append(creation.min(1))
Organisation.is_a.append(member.some(Person))
Organisation.is_a.append(member.all(OneOf([Organisation, Person])))
Plan.is_a.append(part.some(Action))

Action.comment.append(
    "An action is a change which is brought about by a single agent, playing a role. The agent is the holder of some indended outcome of the action: an action is always intentional. The intention of the agent has usually corresponds with an expectation the intended outcome to be brought about: the agent believes in some expectation. Note that the intention might not correspond with the *actual* outcome of the action.")
Agent.commnt.append("An agent is any owl:Thing which can act, i.e. play the 'actor' role wrt. an action",
                    "It is a holder for propositional attitudes")
Artifact.comment.append("A physical object created by some person to fulfill a particular purpose")
CollaborativePlan.comment.append(
    "A collaborative plan is a plan which is shared (and executed) between at least two agents a and b.")
Creation.comment.append("An act which results in the creation of some entity/individual")
NaturalObject.append("A natural object is an object not created by man.")
Organisation.comment.append(
    "An organisation is a group of other organisations or persons which acts 'as one'. An organisation can be both formal (i.e. created by law or decree) or informal.")
Person.comment.append("A person is an individual agent. Usually associated with 'human being'.")
PersonPlan.comment.append("A personal plan is a plan which is held (and can be executed) by at most one agent.")
Plan.comment.append(
    "A plan is a structure of multiple other plans or actions. These can be both sequential or concurrent. Usually a plan is referred to in the context of the intention to act of some agent, however when executed the plan itself comes into effect.")
Reaction.comment.append(
    "A reaction is an action that is (at least) performed by an agent that has observed some other action (this is an intensional view): Action <-> Reaction")
Transaction.comment.append(
    "A trade is an exchange of some things between two agents a and b. Consists of two actions A and B where a is the actor of action A and the recipient of action B, and vice versa. Usually these actions are performed concurrently, but these may also be done consequently. The ownership of the things being traded is the requirement/result pair for each action.")
actor.comment.append("Specifies that some participant is an actor in the action.")
actor_in.comment.append("Specifies that the participant is an actor in some action.")
