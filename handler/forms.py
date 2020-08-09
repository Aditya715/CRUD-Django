from django import forms
from .models import (
    RequestList,
    RequestType,
    IndianStates,
    StatusList
)

class RequestListForm(forms.ModelForm):

    query_set_type = RequestType.objects.values_list('type', flat=True)
    query_set_states = IndianStates.objects.values_list('state', flat=True)

    choices_type = [(each, each) for each in query_set_type]
    choices_state = [(each, each) for each in query_set_states]

    # mentioned to create a checkbox but I'm going for radio as \
    # checkbox will allow it for multiple input and if you want it 
    # then we cound replace it with multiple select dropdown as it'll be best here.
    request_type = forms.CharField(widget=forms.RadioSelect(choices=choices_type))
    state = forms.CharField(widget=forms.Select(choices=choices_state))
 
    class Meta:
        model = RequestList
        fields = [
            'id',
            'request_type',
            'request_desc',
            'city',
            'state',
            'pin_code',
            'mobile_number',
        ]

class UpdateStatusForm(forms.ModelForm):
    
    status_query = StatusList.objects.values_list('status', flat=True)

    status_choices = [ (each, each) for each in status_query ]

    status = forms.CharField(widget=forms.Select(choices=status_choices))

    class Meta:
        model = RequestList
        fields = ['status', 'remarks']