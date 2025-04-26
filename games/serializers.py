from rest_framework import serializers
from .models import Game, GameParam

class GameParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameParam
        fields = ['id', 'nome']

class GameSerializer(serializers.ModelSerializer):
    params = GameParamSerializer(many=True, required=True)  # Permette di inviare params nel payload

    class Meta:
        model = Game
        fields = ['id', 'nome', 'descrizione', 'anno_di_pubblicazione', 'categorie', 
                  'autori', 'artisti', 'min_giocatori', 'max_giocatori', 'tempo_di_gioco', 
                  'immagine', 'params']

    def create(self, validated_data):
        params_data = validated_data.pop('params', [])  # Estrae i parametri dal payload
        if not params_data:
            raise serializers.ValidationError("Ogni gioco deve avere almeno un parametro associato.")

        game = Game.objects.create(**validated_data)
        for param in params_data:
            GameParam.objects.create(game=game, nome=param['nome'])  # Crea i parametri

        return game

