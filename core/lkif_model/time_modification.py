import datetime

from owlready2 import Thing, ObjectProperty, DataProperty, FunctionalProperty, InverseFunctionalProperty

from . import _my_ontology
from legal_action import PublicAct
from .time import Moment, temporal_relation, Interval, finishes, starts, TemporalOccurrence

onto = _my_ontology()


class Modification(PublicAct):
    ontology = onto


class TextualModification(Modification):
    ontology = onto


class SemanticAnnotation(Modification):
    ontology = onto


class ModificationOfSystem(SemanticAnnotation):
    ontology = onto


class Remaking(ModificationOfSystem):
    ontology = onto


class Application(ModificationOfSystem):
    ontology = onto


class Ratification(ModificationOfSystem):
    ontology = onto


class TemporalModification(Modification):
    ontology = onto


class EfficacyModification(TemporalModification):
    ontology = onto


class Ultractivity(EfficacyModification):
    ontology = onto


class Transposition(ModificationOfSystem):
    ontology = onto


class DynamicTemporalEntity(TemporalOccurrence):
    ontology = onto


class ApplicationInterval(Interval, DynamicTemporalEntity):
    ontology = onto


class InForceModification(Thing):
    ontology = onto


class ProrogationInForce(InForceModification):
    ontology = onto


class InForceInterval(Interval, DynamicTemporalEntity):
    ontology = onto


class StartInForce(InForceModification):
    ontology = onto


class EndInForce(InForceModification):
    ontology = onto


class Annulment(InForceModification):
    ontology = onto


class EfficacyInterval(Interval, DynamicTemporalEntity):
    ontology = onto


class StartEfficacy(EfficacyInterval):
    ontology = onto


class EndEfficacy(EfficacyModification):
    ontology = onto


class Suspension(EfficacyModification):
    ontology = onto


class StaticTemporalEntity(Thing):
    ontology = onto


class PublicationDate(StaticTemporalEntity, Moment):
    ontology = onto


class ModificationOfScope(SemanticAnnotation):
    ontology = onto


class DeliveryDate(StaticTemporalEntity, Moment):
    ontology = onto


class Exception(ModificationOfScope):
    ontology = onto


class Renewal(InForceModification):
    ontology = onto


class Repeal(TextualModification):
    ontology = onto


class ProrogationEfficacy(EfficacyModification):
    ontology = onto


class Extension(ModificationOfScope):
    ontology = onto


class Integration(TextualModification):
    ontology = onto


class Substitution(TextualModification):
    ontology = onto


class InForceModification(TemporalModification):
    ontology = onto


class EnterInForceDate(StaticTemporalEntity, Moment):
    ontology = onto


class ApplicationDate(DynamicTemporalEntity, Moment):
    ontology = onto


class Retroactivity(EfficacyModification):
    ontology = onto


class ModificationOfMeaning(SemanticAnnotation):
    ontology = onto


class Variation(ModificationOfMeaning):
    ontology = onto


class ExistenceDate(Moment):
    ontology = onto


class Relocation(TextualModification):
    ontology = onto


class Interpretation(ModificationOfMeaning):
    ontology = onto


class Deregulation(ModificationOfSystem):
    ontology = onto


class StaticTemporalEntity(TemporalOccurrence):
    ontology = onto


class ModificationOfTerm(ModificationOfMeaning):
    ontology = onto


class produce_efficacy_modification(ObjectProperty):  #TODO: Dont know if this is correct
    ontology = onto
    domain = [Repeal, Integration, Substitution]


class initial_date_of(starts):
    ontology = onto
    domain = [Moment]
    range = [Interval]


class initial_date(temporal_relation):
    ontology = onto
    domain = [Interval]
    range = [Moment]
    inverse_property = initial_date_of


class in_force(ObjectProperty):
    ontology = onto
    domain = [Modification]
    range = [InForceInterval]


class final_date(temporal_relation):
    ontology = onto
    domain = [Interval]
    range = [Moment]


class final_date_of(finishes):
    ontology = onto
    domain = [Moment]
    range = [Interval]
    inverse_property = final_date


class efficacy(ObjectProperty):
    ontology = onto
    domain = [Modification]
    range = [EfficacyInterval]


class duration(ObjectProperty):
    ontology = onto
    domain = [Suspension]
    range = [Interval]


class application(ObjectProperty):
    ontology = onto
    domain = [Modification]
    range = [ApplicationDate]


class date(DataProperty):
    ontology = onto
    domain = [Moment]
    range = [datetime.datetime]


class produce_textual_modification(ObjectProperty, FunctionalProperty):
    ontology = onto
    domain = [Annulment | Renewal]
    range = [EndInForce]


class produce_inforce_modification(ObjectProperty, InverseFunctionalProperty):
    ontology = onto
    range = [Annulment | Renewal]
    domain = [Repeal | Integration | Substitution]


Transposition.comment.append("Interpretation in context of the European Union")
EfficacyModification.comment.append("Modifies the efficacy period of some norm")
DynamicTemporalEntity.comment.append("A dynamic temporal entity represents the norm in its evolution over time.")
Remaking.comment.append("When an act is completely rewritten in a new way but the topic remains the same.")
Application.comment.append(
    "When a local act applies in the local legal system normative supra-ordered such as when a region applies an EU directive or a decree it applies the normative contant in some act")
Ratification.comment.append(
    "When an international treaty is ratified by local parliament in order to include it in the local legal system. The same thing happens when each local parliament ratifies bilateral or multilateral agreements.")
ProrogationInForce.comment.append(
    "Prorogation of the date of enactment of some normative content. The 'life' of the act is lengthened with respect to some previous end of enactment modification.")
ApplicationDate.comment.append(
    "The date when a modification is applied to the destination legislative document. The date can be instantaneous, in the future or in the past. Normally this date coincides with the date of efficacy of the text in which the modification takes place.")
Retroactivity.comment.append(
    "When the efficacy or a partial efficacy starts before the entry into force of the document")
ModificationOfTerm.comment.append("Modification of the term specified by some procedural deadline.")
EfficacyInterval.comment.append(
    "The period during which a normative fragment may be either operative or inoperative, by explicit provision of the document itself. The document is said to be in a period of operation, or enforceability or efficacy, when it may or must be applied or enforced.")
Substitution.comment.append("Substitution of a part or entire act or annex")
TemporalModification.comment.append("Modifies the efficacy or being in force of some norm")
Suspension.comment.append(
    "When a part of an act or some provisions are suspended in coming to be operative for a period or indefinately")
InForceModification.append("Modifies the period of being in force of some norm")
PublicationDate.comment.append(
    "The date when the normative document is published in the official journal designated as the source for making all such documents public and legal.")
Exception.comment.append("Restricts the scope of normative content to some particular jurisdiction")
ModificationOfMeaning.comment.append(
    "A modification that changes the meaning of some provision without changing its literal text")
StaticTemporalEntity.comment.append(
    "A static temporal entity captures a single moment in the norm's life that is fixed over time.")
EndInForce.comment.append(
    "When an act states the end of the period of enactment, and includes an implicit repealing of the text.")
ApplicationInterval.comment.append(
    "This is the interval during which a normative document, or fragment, produces the consequences that the normative provision establishes.")
Interpretation.comment.append(
    "Modification of the interpretation of normative content by the author or some superior actor")
Deregulation.comment.append(
    "When a part of some primary legislative source is delegated to some secondary legislative source (e.g. from act to regulation).")
InForceInterval.comment.append(
    "The period during which a normative fragment belongs to the normative system. The period of force for each fragment may change over time as a function of the modifications the document goes through.")
Repeal.comment.append("Removal of some part of text or the entire act from the legal system.")
DeliveryDate.comment.append(
    "The date when the competent authorities finalise the document by affixing their signatures to it (e.g. promulgation by the president, signature by the queen etc.) This is the date shown on the document itself: it is an objective element and clearly identifyable.")
EnterInForceDate.comment.append(
    "The date when a dnormative document becomes law and enters the legal system for the first time. This is the moment in the doucment's history starting from which the document can be amended, its applicability assessed, and its manner of producing an effect determined.")
Variation.comment.append("Modification by paraphrasing")
ExistenceDate.comment.append(
    "The date when the formal act by which a legislative body freezes the document into its final form, it is the time when the document can be said to have begun its existence.")
Relocation.comment.append("Moving some part of the text to some other place within the same document")
ProrogationEfficacy.comment.append("Prorogation of entry into force, but applied to the efficacy of some norm")
Extension.comment.append("Extends the scope of normative content to some particular jurisdiction")
