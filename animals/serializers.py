from rest_framework import serializers
from .models import Animal
from groups.serializers import GroupSerializer
from characteristics.serializers import CharacteristicSerializer
from groups.models import Group
from characteristics.models import Characteristic



class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weigth = serializers.FloatField()
    sex = serializers.CharField(max_length=15)
    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)

    def create(self, valideted_data):

        group_data = valideted_data.pop("group")

        characteristics_data = valideted_data.pop("characteristics")
        
        group =Group.objects.get_or_create(**group_data)[0]

        animal = Animal.objects.create(**valideted_data, group=group)
        for characteristic in characteristics_data:
            characteristics = Characteristic.objects.get_or_create(**characteristic)[0]
            animal.characteristics.add(characteristics)
            
        
        return animal
    def update(self, instance: Animal, validated_data: dict):
        non_editable_keys = ("sex","group",)
        for key, value in validated_data.items():
            if key in non_editable_keys:
                raise KeyError
            if key != "characteristics":
              setattr(instance, key, value)
            if key == "characteristics":
                instance.characteristics.clear()
                for characteristic in validated_data["characteristics"]:
                    characteristics = Characteristic.objects.get_or_create(**characteristic)[0]
                    instance.characteristics.add(characteristics)


        instance.save()

        return instance
