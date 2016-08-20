from django.forms import ModelForm
from .models import missionstatuses
from django.utils.translation import ugettext_lazy as _


class NewMissionStatus(ModelForm):

    class Meta:
        model = missionstatuses
        fields = {
            'name', 'description', 'color',
        }
        labels = {
            'name': _('Name of the Mission Status')
        }
