from . import _my_ontology
from owlready2 import Thing, GeneralClassAxiom, ObjectProperty, AllDisjoint, TransitiveProperty

from mereology import Composition, Atom, Pair, component
from lkif_top import SpatioTemporalOccurrence

onto = _my_ontology()


class TemporalOccurrence(SpatioTemporalOccurrence):
    ontology = onto


class Moment(Atom, TemporalOccurrence):
    ontology = onto


class Interval(Composition, TemporalOccurrence):
    ontology = onto


class PairOfPeriods(Thing):
    ontology = onto


class temporal_relation(ObjectProperty):
    ontology = onto
    domain = [TemporalOccurrence]
    range = [TemporalOccurrence]

class after(temporal_relation, TransitiveProperty):
    ontology = onto
    domain = [TemporalOccurrence]
    range = [TemporalOccurrence]


class before(temporal_relation, TransitiveProperty):
    ontology = onto
    domain = [TemporalOccurrence]
    range = [TemporalOccurrence]
    inverse_property = after


class between(temporal_relation, TransitiveProperty):
    ontology = onto
    domain = [TemporalOccurrence]
    range = [PairOfPeriods]


class during(temporal_relation):
    ontology = onto


class finishes(temporal_relation):
    ontology = onto


class immediately_after(after):
    ontology = onto
    domain = [TemporalOccurrence]
    range = [TemporalOccurrence]


class immediately_before(before):
    ontology = onto
    domain = [TemporalOccurrence]
    range = [TemporalOccurrence]
    inverse_property = immediately_after


class overlap(temporal_relation):
    ontology = onto


class preceeds(temporal_relation):
    ontology = onto


class starts(temporal_relation):
    ontology = onto

AllDisjoint([Interval, Moment])

gca__pair_of_periods = GeneralClassAxiom(Pair & component.all(TemporalOccurrence))
gca__pair_of_periods.is_a.append(PairOfPeriods)

gca__temporal_occurrence = GeneralClassAxiom(SpatioTemporalOccurrence & immediately_after.some(TemporalOccurrence) & immediately_before.some(TemporalOccurrence))
gca__temporal_occurrence.is_a.append(PairOfPeriods)



Interval.comment.append("An interval is a composition of multiple periods of time.")
Moment.comment.append("A moment is an atomic period of time, i.e. it cannot be divided into other parts")
PairOfPeriods.comment.append("A pair of two time periods")
TemporalOccurrence.comment.append("A period of time, has a duration")

after.comment.append("'after' is the transitive closure of 'next'; this is defined in time-rules.owl.",
                     "Specifies that a time period occurs after another period, but might overlap with it.")
before.comment.append("Specifies that a time period occurs before another period, but might overlap with it.")
between.comment.append("Specifies that a time period occurs between two other periods")
during.comment.append("Specifies that a time period occurs during another period")
finishes.comment.append(
    "Specifies that a time period finishes another period, i.e. the other period starts before, but ends at the same moment")
immediately_after.comment.append(
    "Specifies that a time period occurs immediately after another period, i.e. it starts where the other period ends")
immediately_before.comment.append(
    "Specifies that a time period occurs immediately before another period, i.e. it ends where the other period starts",
    "t1 previous t2: interval t1 is before t2, but there is no interval between them, i.e., t1 ends where t2 starts")
overlap.comment.append("Specifies that a time period overlaps with another time period (in any way)")
preceeds.comment.append("Specifies that a time period preceeds another period, the periods do not overlap")
starts.comment.append(
    "Specifies that a time period starts another period, i.e. the other period starts at the same time, but ends at a later time.")
temporal_relation.comment.append("A relation between two time periods")
