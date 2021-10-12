from django.db import models

class WhiteCard(models.Model):
    CardNo = models.IntegerField()
    CardText = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.CardText

    def findScore(self, blackCard):
        return Score.objects.filter(
            WhiteCard=self,
            BlackCard=blackCard
        )[0]

    def findScoreAverage(self, blackCard):
        return self.findScore(blackCard).return_averages()


class BlackCard(models.Model):
    CardNo = models.IntegerField()
    CardText = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.CardText

    def findScore(self, whiteCard):
        return Score.objects.filter(
            WhiteCard=whiteCard,
            BlackCard=self
        )[0]


class Score(models.Model):
    # Uses two foreign keys to define the relationship
    WhiteCard = models.ForeignKey(WhiteCard, models.CASCADE)
    BlackCard = models.ForeignKey(BlackCard, models.CASCADE)
    rating = models.DecimalField(max_digits=4,decimal_places=2)
    timesAppeared = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'Black Card: {BlackCard.CardText}, White Card: {WhiteCard.CardText}'

    def return_averages(self):
        if self.timesAppeared != 0:
            average = self.rating / self.timesAppeared
            return average
        return 0

    def add_score(self, score):
        self.rating += score
        self.timesAppeared += 1
