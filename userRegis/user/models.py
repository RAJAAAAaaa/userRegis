from django.db import models
import uuid
from simple_history import register
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User
from django.dispatch import receiver
from simple_history.signals import (
    pre_create_historical_record,
    post_create_historical_record
)
from simple_history.utils import update_change_reason

register(User)
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    changed_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    history = HistoricalRecords(history_change_reason_field=models.TextField(null=True)),
    #log = HistoricalRecords(related_name='history')
    #history = HistoricalRecords(history_id_field=models.UUIDField(default=uuid.uuid4))
    __history_date = None

    @property
    def _history_date(self):
        return self.__history_date

    @_history_date.setter
    def _history_date(self, value):
        self.__history_date = value


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    history = HistoricalRecords()





class IPAddressHistoricalModel(models.Model):
    """
    Abstract model for history models tracking the IP address.
    """
    ip_address = models.GenericIPAddressField('IP address')

    class Meta:
        abstract = True


class PollWithExtraFields(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    history = HistoricalRecords(bases=[IPAddressHistoricalModel,])


@receiver(pre_create_historical_record)
def pre_create_historical_record_callback(sender, **kwargs):
    print("Sent before saving historical record")

@receiver(post_create_historical_record)
def post_create_historical_record_callback(sender, **kwargs):
    print("Sent after saving historical record")
