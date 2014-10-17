from django.test import TestCase
from cards.models import Card, WarGame


class CardTestCase(TestCase):
    def setUp(self):
        self.card = Card.objects.create(suit=Card.CLUB, rank="jack")
        self.high_card = Card.objects.create(suit=Card.CLUB, rank="queen")

    def test_get_ranking(self):
        """Test that we get the proper ranking for a card"""
        self.assertEqual(self.card.get_ranking(), 11)

    def test_get_war_result(self):
        self.assertEqual(self.card.get_war_result(self.high_card), -1)
        self.assertEqual(self.high_card.get_war_result(self.card), 1)
        self.assertEqual(self.card.get_war_result(self.card), 0)

    def get_ties(self):
        return WarGame.objects.filter(player=self, result=WarGame.TIE).count()

    def get_record_display(self):
        return "{}-{}-{}".format(self.get_wins(), self.get_losses(), self.get_ties())
