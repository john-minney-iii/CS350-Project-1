from django.db import models

class WhiteCard(models.Model):
    CardNo = models.IntegerField()
    CardText = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.CardText

    def findScore(self, blackCard):
        for score in Score.objects.all():
            if score.Whitecard == self:
                if score.Blackcard == blackCard:
                    return score


class BlackCard(models.Model):
    CardNo = models.IntegerField()
    CardText = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.CardText

    def findScore(self, whiteCard):
        for score in Score.objects.all():
            if score.Blackcard == self:
                if score.Whitecard == whiteCard:
                    return score


class Score(models.Model):
    # Uses two foreign keys to define the relationship
    WhiteCard = models.ForeignKey(WhiteCard, models.CASCADE)
    BlackCard = models.ForeignKey(BlackCard, models.CASCADE)
    rating = models.DecimalField(max_digits=4,decimal_places=2)
    timesAppeared = models.IntegerField(default=0)

    def return_averages(self):
        average = self.rating / self.timesAppeared
        return average

    def add_score(self, score):
        self.rating += score
        self.timesAppeared += 1
