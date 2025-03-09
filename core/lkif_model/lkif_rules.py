from owlready2 import ObjectProperty, GeneralClassAxiom, Thing

from . import _my_ontology, expression, mereology
from .role import EpistemicRole, plays, played_by

onto = _my_ontology()

class Atom(EpistemicRole):
    ontology = onto

class Exception(Atom, expression.Exception):
    ontology = onto

class Assumption(Atom, expression.Assumption):
    ontology = onto

class Rule(EpistemicRole):
    ontology = onto

class ValidRule(Rule):
    ontology = onto

class Argument(Rule, expression.Argument):
    ontology = onto

class NegatedAtom(EpistemicRole):
    ontology = onto

class rule_predicate(ObjectProperty):
    ontology = onto
    range = [plays.some(Atom | Rule)]
    domain = [plays.some(Rule)]

class prior(rule_predicate):
    ontology = onto

class excluded(rule_predicate):
    ontology = onto
    range = [plays.some(Atom)]

class applies(rule_predicate):
    ontology = onto
    range = [plays.some(Atom)]

class rebuts(rule_predicate):
    ontology = onto
    range = [plays.some(Rule)]

gca__atom = GeneralClassAxiom(played_by.all(mereology.Atom) & played_by.some(expression.Expression & mereology.Atom))
gca__atom.is_a.append(Atom)

gca__rule = GeneralClassAxiom(played_by.all(mereology.Composition) & played_by.some(expression.Expression & mereology.Composition))
gca__rule.is_a.append(Rule)

gca__negated_tom = GeneralClassAxiom(played_by.all(mereology.Atom) & played_by.some(expression.Expression & mereology.Atom))
gca__negated_tom.is_a.append(NegatedAtom)

NegatedAtom.comment.append("A negated atom is the negation of some other atom (cf. Deliverable 1.1)")
Argument.comment.append("An argument is some rule used in argumentation (cf. Deliverable 1.1)")
Exception.comment.append("An exception states an exception to the head of the rule (defeasibly), cf. Deliverable 1.1")
Rule.comment.append("An LKIF rule, based on swrl:Impl")
ValidRule.comment.append("A valid LKIF rule")
Atom.comment.append("An atom is the most basic (undivisible) part of an LKIF rule (cf. Deliverable 1.1)")
Assumption.comment.append("An assumption is some atom held to be true, without proof, in the head of a rule (defeasibly), cf. Deliverable 1.1")
rule_predicate.comment.append("Some predicate in or over some rule")
prior.comment.append("Specifies a prior relation between two rules")
excluded.comment.append("Specifies an exclusion relation between a rule and an atom")
applies.comment.append("Specifies whether some rule applies to some atom")
rebuts.comment.append("Specifies whether some rule abuts another rule")