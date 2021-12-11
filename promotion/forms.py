from django import forms

from .models import Promotion

class PromotionForm(forms.ModelForm):

    class Meta:
        model = Promotion
        fields = ('title', 
            'text', 
            'candidate', 
            'election',
            'symbol',
            'party',
            'name_kor',
            'name_hanja',
            'sex',
            'birth',
            'job',
            'educational_background',
            'career',
            'bulletin',
            'poster',
            'pledge',
        )