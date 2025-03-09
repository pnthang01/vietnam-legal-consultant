from owlready2 import Thing, GeneralClassAxiom, ObjectProperty, AllDisjoint

from . import _my_ontology
from mereology import part, direct_part_of
from .time import TemporalOccurrence
from lkif_top import PhysicalEntity, MentalEntity

onto = _my_ontology()


class Change(Thing):
    ontology = onto


class Process(Change):
    ontology = onto


class PhysicalProcess(Process, PhysicalEntity):
    ontology = onto


class MentalProcess(Process, MentalEntity):
    ontology = onto


class Termination(Change):
    ontology = onto


class Initiation(Change):
    ontology = onto


class Continuation(Thing):
    ontology = onto


class PhysicalObject(PhysicalEntity):
    ontology = onto



class participant(ObjectProperty):
    ontology = onto
    domain = [Change]
    range = [Thing]


class participant_in(ObjectProperty):
    ontology = onto
    domain = [Thing]
    range = [Change]
    inverse_property = participant


class result(participant):
    ontology = onto


class result_of(participant_in):
    ontology = onto
    inverse_property = result


class requirement_of(participant_in):
    ontology = onto


class requirement(participant):
    ontology = onto
    inverse_property = requirement_of


class resource(participant):
    ontology = onto


class resource_for(participant_in):
    ontology = onto
    inverse_property = resource


class created_by(result_of):
    ontology = onto


class creation(result):
    ontology = onto
    inverse_property = created_by


AllDisjoint([Change, PhysicalObject])

gca__change = GeneralClassAxiom(Thing & part.all(Change))
gca__change.is_a.append(Change)

gca__continuation = GeneralClassAxiom(Change & direct_part_of.some(Change))
gca__continuation.is_a.append(Continuation)

gca__initiation = GeneralClassAxiom(Change & direct_part_of.some(Change))
gca__initiation.is_a.append(Initiation)

gca__termination = GeneralClassAxiom(Change & direct_part_of.some(Change))
gca__termination.is_a.append(Termination)


Change.is_a.append(result.some(Thing) & requirement.some(Thing))
Continuation.is_a.append(requirement.some(Initiation))
Initiation.is_a.append(result.some(Continuation))
Process.is_a.append(resource.some(TemporalOccurrence))
Termination.is_a.append(requirement.some(Continuation))


Change.comment.append("A change is a difference between the situation before and after the change occurs (the event of the change). A change can be instantaneous")
Process.comment.append(
    "A process is a 'causal' change: any change which can be explained through some known or understood causal "
    "structure. Every process has some Time_Period as duration.")
MentalProcess.comment.append(
    "A mental, i.e. non-physical, process that has no physical effects. Examples are (human) thought and reasoning.")
Termination.comment.append("The termination of a change.")
Initiation.comment.append("The initiation of a change.")
Continuation.comment.append("The continuation of a change, once initiated")
PhysicalObject.comment.append(
    "A physical object is a physical entity consisting of matter, it has a spatio-temporal extension.")

created_by.comment.append(
    'Specifies that some thing is created (i.e. a result of) by a process, and exists because of the process taking '
    'place.')
participant.comment.append(
    'A participant is someone or something that participates in a change, i.e. is involved in a change')
participant_in.comment.append('Specifies that some thing participates in a process')
requirement.comment.append(
    'A requirement relation relates the process with a prerequisite for that process: without it the process cannot occur"')
requirement_of.comment.append('Specifies that some participant is a requirement for a process')
resource.comment.append('A resource is some quantity of something used to perform the action: i.e. time, energy')
resource_for.comment.append('Specifies that some participant is a resource for a process')
result.comment.append(
    'Specifies that some participant is the result of the process, it might have existed before the process took place, but is in some way altered')
result_of.comment.append(
    "Specifies that some participant is the result of a process, it might have existed before the process took place, but is in some way altered (an 'inanimate' goal of an act)")
created_by.comment.append(
    "Specifies that some thing is created (i.e. a result of) by a process, and exists because of the process taking place.")
creation.comment.append(
    "Specifies that some thing is created (i.e. a result of) by a process, and exists because of the process taking place.")
