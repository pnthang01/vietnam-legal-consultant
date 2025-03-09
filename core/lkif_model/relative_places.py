from owlready2 import *
from . import _my_ontology
from mereology import contained_in, Atom, part, strict_part, Part, Composition
from lkif_top import SpatioTemporalOccurrence

onto = _my_ontology()


class Place(SpatioTemporalOccurrence):
    ontology = onto


class LocationComplex(Place):
    ontology = onto


class AbsolutePlace(Place):
    ontology = onto


class ComprehensivePlace(LocationComplex):
    ontology = onto


class RelativePlace(Place):
    ontology = onto


class spatial_relation(ObjectProperty):
    ontology = onto
    domain = [Place]
    range = [Place]


class spatial_reference(spatial_relation):
    ontology = onto
    domain = [Place]
    range = [Thing]


class relatively_fixed(spatial_relation, SymmetricProperty, TransitiveProperty):
    ontology = onto
    domain = [Place]
    range = [Place]


class meet(spatial_relation, SymmetricProperty):
    ontology = onto
    domain = [Place]
    range = [Place]


class partially_coincide(meet, SymmetricProperty):
    ontology = onto
    domain = [Place]
    range = [Place]


class overlap(partially_coincide, relatively_fixed):
    ontology = onto
    domain = [Place]
    range = [Place]


class abut(meet, SymmetricProperty):
    ontology = onto
    domain = [Place]
    range = [Place]


class connect(meet, relatively_fixed):
    ontology = onto
    domain = [Place]
    range = [Place]


class in_(contained_in, spatial_relation):
    ontology = onto
    domain = [Place]
    range = [Place]


class location_complex_for(spatial_relation, InverseFunctionalProperty):
    ontology = onto
    range = [Place]
    domain = [LocationComplex]


class location_complex(spatial_relation, FunctionalProperty):
    ontology = onto
    range = [LocationComplex]
    domain = [Place]
    inverse_property = location_complex_for


class externally_connect(abut, connect):
    ontology = onto
    domain = [Place]
    range = [Place]


class exactly_coincide(meet, SymmetricProperty, TransitiveProperty):
    ontology = onto
    domain = [Place]
    range = [Place]


class cover(meet, TransitiveProperty):
    ontology = onto
    domain = [Place]
    range = [Place]


class covered_by(meet, partially_coincide, TransitiveProperty):
    ontology = onto
    domain = [Place]
    range = [Place]
    inverse_property = cover


AllDisjoint([AbsolutePlace, RelativePlace])

gca__atom = GeneralClassAxiom(part.exactly(0))
gca__atom.is_a.append(Atom)

gca__composition = GeneralClassAxiom(strict_part.min(2, Part))
gca__composition.is_a.append(Composition)

gca__location_complex_for = GeneralClassAxiom(Place & location_complex_for.all(Place))
gca__location_complex_for.is_a.append(LocationComplex)

gca__place = GeneralClassAxiom(SpatioTemporalOccurrence & location_complex.some(LocationComplex)
                               & location_complex.some(LocationComplex))
gca__place.is_a.append(Place)

gca__relative_place = GeneralClassAxiom(Place & spatial_reference.some(Thing))
gca__relative_place.is_a.append(RelativePlace)


LocationComplex.is_a.append(location_complex_for.some(Place))
Place.is_a.append([AbsolutePlace, RelativePlace])


Inverse(abut)
Inverse(exactly_coincide)
Inverse(meet)
Inverse(partially_coincide)
Inverse(relatively_fixed)


RelativePlace.comment.append("A relative place is defined by some reference to some object/thing")
Place.comment.append("A place is a spatio-temporal-occurrence")
LocationComplex.comment.append(
    "A location complex is a relatively stable complex of places referred to as one: it is the maximal collection of places with the same reference object.")
ComprehensivePlace.comment.append(
    "A place is comprehensive if it always covers every place (and thus also every location-complex) and every object.")
AbsolutePlace.comment.append("An absolute place is defined without reference to other places.")

spatial_relation.comment.append("A spatial relation is a relation between two places")
spatial_reference.comment.append("The reference to an object determines the relative place.")
relatively_fixed.comment.append(
    "Two places are relatively fixed if and only if either x and y have a common reference object or neither x nor y has a reference object")
partially_coincide.comment.append(
    "Definition partially-coincide: partially-coincide(a, b) iff exists x :( cover(a, x) and cover(b, x) )")
overlap.comment.append("Two places overlap if they are relatively fixed and partially coincide")
meet.comment.append("Specifies that two places meet, but need not overlap or cover (reflexive)")
abut.comment.append(
    "Two places abut if they meet but do not partially coincide. NOTE: OWL 1.1: 'abut' is irreflexive and disjoint with 'partially-coincide'")
connect.comment.append("Two places are connected if they are both relatively fixed and when they meet")
covered_by.comment.append("Specifies that two places cover eachother. To add in OWL 1.1: 'covered-by' is reflexive, 'covered-by' is transitive")
cover.comment.append("Definition cover:  cover(a, b) iff forall x:( meet(x, b) implies meet(x, a) )")
cover.comment.append(
    "Specifies that two places cover eachother. Note: this cover-relation is the inverse of the COV relation described by Donnelly (2005)")
exactly_coincide.comment.append(
    "Definition exactly-coincide: exactly-coincide(a, b) iff forall x:( meet(x, a) iff meet(x, b) )")
externally_connect.comment.append(
    "Two places are externally connected if they are relatively fixed and abut, but do not overlap (OWL 1.1)")
in_.comment.append(
    "The 'in' property is used to express that one place is located (i.e. contained) within another place. It is therefore a mereological relation as well.")
