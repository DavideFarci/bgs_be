from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated  # Importato!
from .models import Game, GameParam
from .serializers import GameSerializer, GameParamSerializer


class GameViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_queryset(self):
        return Game.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["get"])
    def params(self, request, pk=None):
        game = self.get_object()
        params = game.params.all()
        serializer = GameParamSerializer(params, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def add_param(self, request, pk=None):
        game = self.get_object()
        nome = request.data.get("nome")
        if nome:
            param = GameParam.objects.create(game=game, nome=nome)
            serializer = GameParamSerializer(param)
            return Response(serializer.data, status=201)
        return Response({"error": "Nome del parametro non fornito."}, status=400)


class GameParamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # 👈 Anche qui
    queryset = GameParam.objects.all()
    serializer_class = GameParamSerializer
