from __future__ import unicode_literals

from django.db import models
from django.apps import apps


class Term(models.Model):
    """
    An atomic vocabulary term. (e.g., tension_test, modulus_of_elasticity, etc.)
    @author Kevin Porter
    """
    term = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.term

    def get_primary_relationships(self):
        """
        Provides all triples for which this term is a subject.
        :return: All triples for which this term is a subject.

        @author Kevin Porter
        """
        TermRelationshipTerm = apps.get_model(app_label='terms', model_name='termrelationshipterm')
        qs = TermRelationshipTerm.objects.filter(subject=self)
        return qs

    def get_secondary_relationships(self):
        """
        Provides all triples for which this term is an object.
        :return: All triples for which this term is an object.

        @author Kevin Porter
        """
        TermRelationshipTerm = apps.get_model(app_label='terms', model_name='termrelationshipterm')
        qs = TermRelationshipTerm.objects.filter(object=self)
        return qs


class Relationship(models.Model):
    """
    A relationship between terms. (e.g., synonymous_to, similar_to, related_to, etc.)
    @author Kevin Porter
    """
    relationship = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.relationship

    def get_triples(self):
        TermRelationshipTerm = apps.get_model(app_label='terms', model_name='termrelationshipterm')
        qs = TermRelationshipTerm.objects.filter(predicate=self)
        return qs


class TermRelationshipTerm(models.Model):
    """
    A pseudo-triple statement. This structure is bound to change.
    @author Kevin Porter
    """
    subject = models.ForeignKey(Term, related_name='subject')
    predicate = models.ForeignKey(Relationship)
    object = models.ForeignKey(Term, related_name='object')

    def __str__(self):
        return str(self.subject) + ' ' + str(self.predicate) + ' ' + str(self.object)
