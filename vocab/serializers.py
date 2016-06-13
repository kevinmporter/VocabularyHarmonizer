from rest_framework import serializers
from common.models import License
from .models import Term, Relationship, TermRelationshipTerm


class TermSerializer(serializers.ModelSerializer):
    license = serializers.SlugRelatedField(slug_field='name',
                                           queryset=License.objects.all())

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
        fields = ('id', 'term', 'relationships', 'description', 'license', 'license_url', )


class RelationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Relationship
        fields = ('relationship', 'description', )


class TripleSerializer(serializers.ModelSerializer):
    relationship = serializers.SlugRelatedField(slug_field='relationship',
                                                queryset=Relationship.objects.all())
    object = serializers.SlugRelatedField(slug_field='term',
                                          queryset=Term.objects.all())

    class Meta:
        model = TermRelationshipTerm
        fields = ('relationship', 'object', )
