from django.forms import ModelForm
from .models import Listing, Category


class ListingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        # This allows to customize what values from the foreign key you want to display..since it was originally
        # displaying numbers, it was customized to display the category associated with those numbers
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].label_from_instance = lambda obj: "%s" % (obj.category)
    class Meta:
        model = Listing
        exclude = ["id", "listed_by", "created_at"]