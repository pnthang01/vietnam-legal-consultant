from owlready2 import Thing

from . import _my_ontology

onto = _my_ontology()

class AbstractEntity(Thing):
    ontology = onto

class MentalEntity(Thing):
    ontology = onto

class MentalObject(MentalEntity):
    ontology = onto

class Occurrence(Thing):
    ontology = onto

class PhysicalEntity(Thing):
    ontology = onto

class SpatioTemporalOccurrence(Occurrence):
    ontology = onto
#
# AbstractEntity.comment.append(
#     "An abstract entity is an entity that is not a physical object, but rather an abstract concept or idea.")
# MentalEntity.comment.append(
#     "A mental entity is an entity that is not a physical object, but rather an abstract concept or idea.")
# MentalObject.comment.append(
#     "A mental object is an object that is not a physical object, but rather an abstract concept or idea.")
# Occurrence.comment.append(
#     "An occurrence is an entity that is not a physical object, but rather an abstract concept or idea.")
# PhysicalEntity.comment.append(
#     "A physical entity is an entity that is not a physical object, but rather an abstract concept or idea.")
# SpatioTemporalOccurrence.comment.append(
#     "An occurrence in space-time.")

