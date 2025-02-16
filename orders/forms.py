from django.forms import ModelForm, BooleanField
from orders.models import Order


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class OrderCreateForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Order
        fields = ('table_number', 'items',)


class OrderUpdateForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Order
        fields = ('table_number', 'items', 'status',)
