from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, GameParamViewSet

# Creiamo un router
router = DefaultRouter()

# Registriamo i viewset con il router
router.register(r'games', GameViewSet)
router.register(r'gameparams', GameParamViewSet)

# Inclusione delle rotte create dal router
urlpatterns = [
    path('', include(router.urls)),  # Include tutte le rotte generate dal router
]
