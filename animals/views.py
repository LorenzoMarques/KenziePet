from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from .models import Animal
from .serializers import AnimalSerializer
from django.shortcuts import get_object_or_404


class AnimalView(APIView):
    def get(self, request, animal_id=None):

      animals = Animal.objects.all()

      serializer = AnimalSerializer(animals, many=True)

      return Response(serializer.data)



    def post(self, request):
        serializer = AnimalSerializer(data=request.data)


        serializer.is_valid(raise_exception=True)

        serializer.save()


        return Response(serializer.data, status.HTTP_201_CREATED)

class AnimalViewDetail(APIView):

  def get(self, request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)

    serializer = AnimalSerializer(animal)

    return Response(serializer.data)

  def delete(self, request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)

    animal.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

  def patch(self, request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)

    serializer = AnimalSerializer(animal, request.data, partial=True)

    serializer.is_valid(raise_exception=True)

    try:
        serializer.save()
    except KeyError:
      try:
        if request.data["sex"]:
          return Response(
              {"message": "You can not update sex property."}, status.HTTP_422_UNPROCESSABLE_ENTITY
          )
      except:
        return Response(
              {"message": "You can not update group property."}, status.HTTP_422_UNPROCESSABLE_ENTITY
          )
        
        
         

    return Response(serializer.data)
