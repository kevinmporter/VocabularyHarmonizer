from rest_framework import serializers
from .models import Term, Relationship, TermRelationshipTerm


class TermSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        term = super(TermSerializer, self).create(validated_data)
        if 'relationships' in validated_data:
            term.relationships(validated_data.get('relationships'))
        return term

    def update(self, instance, validated_data):
        term = super(TermSerializer, self).update(instance, validated_data)
        if 'relationships' in validated_data:
            term.relationships(validated_data.get('relationships'))
        return term

    class Meta:
        model = Term
        fields = ('term', 'relationships', )


class RelationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Relationship
        fields = ('relationship', )


class TripleSerializer(serializers.ModelSerializer):
    relationship = serializers.SlugRelatedField(slug_field='relationship',
                                                queryset=Relationship.objects.all())
    object = serializers.SlugRelatedField(slug_field='term',
                                          queryset=Term.objects.all())

    class Meta:
        model = TermRelationshipTerm
        fields = ('relationship', 'object', )
