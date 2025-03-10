from owlready2 import *
from . import _my_ontology
from .lkif_top import AbstractEntity

onto = _my_ontology()

class Atom(AbstractEntity):
    ontology = onto

class Whole(Thing):
    ontology = onto

class Composition(Whole):
    ontology = onto


class Part(Thing):
    ontology = onto


class Pair(Thing):
    ontology = onto


class part(TransitiveProperty):
    ontology = onto


class part_of(TransitiveProperty):
    ontology = onto
    inverse_property = part


class strict_part(part):
    ontology = onto


class strict_part_of(part_of):
    ontology = onto
    inverse_property = strict_part


class member_of(strict_part_of):
    ontology = onto


class member(strict_part):
    ontology = onto
    inverse_property = member_of


class direct_part_of(part_of):  # Missing equivalentProperty:strict_part_of
    ontology = onto


class direct_part(part):  # Missing equivalentProperty:strict_part
    ontology = onto
    inverse_property = direct_part_of


class contained_in(part_of, TransitiveProperty):
    ontology = onto


class contains(part, TransitiveProperty):
    ontology = onto
    inverse_property = contained_in


class composes(part_of, TransitiveProperty):
    ontology = onto


class composed_of(part, TransitiveProperty):
    ontology = onto
    inverse_property = composes


class component(strict_part):
    ontology = onto


class component_of(strict_part_of):
    ontology = onto
    inverse_property = component


AllDisjoint([Whole, Atom])

gca__pair = GeneralClassAxiom(Part & strict_part.exactly(2, Part))
gca__pair.is_a.append(Pair)

gca__part = GeneralClassAxiom(strict_part_of.all(Whole) | strict_part_of.all(Whole))
gca__part.is_a.append(Part)

gca__whole = GeneralClassAxiom(AbstractEntity & strict_part.all(Part))
gca__whole.is_a.append(Whole)

Part.is_a.append(strict_part_of.some(Whole))
Whole.is_a.append(strict_part.some(Part))

direct_part.is_a.append(strict_part)
direct_part_of.is_a.append(strict_part_of)

# Classes
Atom.comment.append("An atom has no parts")
Composition.comment.append("A composition has multiple parts, the components should meet")
Whole.comment.append('A whole has at least some part')
Part.comment.append("A part is a part_of some whole")
Pair.comment.append("A composition of exactly two parts")
# Properties
part.comment.append("Transitive part relation")
part_of.comment.append("Transitive part_of relation")
strict_part.comment.append("Non transitive part relation")
strict_part_of.comment.append("Non transitive part_of relation")
member_of.comment.append("Specifies membership of a set or group")
member.comment.append("Specifies membership of a set or group")
direct_part_of.comment.append("The non-transitive part_of relation")
direct_part.comment.append("The non-transitive part relation.")
contains.comment.append("Specifies that some thing is contained (spatially) within some other thing")
contained_in.comment.append("Specifies that some thing is contained (spatially) within some other thing")
composes.comment.append("Specifies that some thing is composed_of (spatially) within some other thing")
composed_of.comment.append("Specifies that some thing is composed_of (spatially) within some other thing")
component_of.comment.append("Specifies that some thing is a (functional) component of some other thing")
component.comment.append("Specifies that some thing is a (functional) component of some other thing")
