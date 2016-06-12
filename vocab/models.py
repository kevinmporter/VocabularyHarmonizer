from __future__ import unicode_literals

from django.db import models
from django.apps import apps
from common.models import License


class Term(models.Model):
    """
    An atomic vocabulary term. (e.g., tension_test, modulus_of_elasticity, etc.)
    @author Kevin Porter
    """
    term = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=2048)
    license = models.ForeignKey(License, blank=True, null=True)

    def __str__(self):
        return self.term

    def license_url(self):
        if self.license:
            url = self.license.url
        else:
            url = '#'
        return url

    def get_primary_relationships(self):
        """
        Provides all triples for which this term is a subject.
        :return: All triples for which this term is a subject.

        @author Kevin Porter
        """
        TermRelationshipTerm = apps.get_model(app_label='vocab', model_name='termrelationshipterm')
        qs = TermRelationshipTerm.objects.filter(subject=self)
        return qs

    def get_secondary_relationships(self):
        """
        Provides all triples for which this term is an object.
        :return: All triples for which this term is an object.

        @author Kevin Porter
        """
        TermRelationshipTerm = apps.get_model(app_label='vocab', model_name='termrelationshipterm')
        qs = TermRelationshipTerm.objects.filter(object=self)
        return qs

    def relationships(self, relationships=None):
        """
        A serializer function for retrieving or saving the relationships for a term.
        :return: A list of all the primary relationships for this term.
        """
        if relationships:
            TermRelationshipTerm = apps.get_model(app_label='vocab', model_name='termrelationshipterm')
            Relationship = apps.get_model(app_label='vocab', model_name='relationship')
            for relationship in relationships:
                try:
                    r = Relationship.objects.get(relationship=relationship['relationship'])
                except Relationship.DoesNotExist:
                    raise Exception('Relationships must be manually added to the dictionary.')
                try:
                    o = Term.objects.get(term=relationship['object'])
                except Term.DoesNotExist:
                    raise Exception('Object vocab must be manually added to the dictionary.')
                TermRelationshipTerm.objects.get_or_create(subject=self, predicate=r, object=o)
        from .serializers import TripleSerializer
        rels = self.get_primary_relationships()
        return TripleSerializer(rels, many=True).data


class Relationship(models.Model):
    """
    A relationship between vocab. (e.g., synonymous_to, similar_to, related_to, etc.)
    @author Kevin Porter
    """
    relationship = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=2048)
    license = models.ForeignKey(License, blank=True, null=True)

    def __str__(self):
        return self.relationship

    def get_triples(self):
        TermRelationshipTerm = apps.get_model(app_label='vocab', model_name='termrelationshipterm')
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
