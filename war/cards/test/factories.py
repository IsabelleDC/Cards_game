import factory
from cards.models import WarGame


class WarGameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cards.WarGame'
    result = WarGame.TIE


class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cards.Player'
        # django_get_or_create = ('username', 'email', 'password')
        # email = factory.lazy_attribute(lambda o: '%s@gmail.com' % (o.username))
        # username ='testuser'
        # email ='test@gmail.com'
        # p = PlayerFactory(profile_name='john')
