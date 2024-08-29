from django.forms import ModelForm, BooleanField, forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'









class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("viwes_counter", "owner")


    def clean_name(self):
        name = self.cleaned_data["name"]
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word.lower() in name.lower():
                raise forms.ValidationError(f"Название продукта не может содержать слово: {word}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word.lower() in description.lower():
                raise forms.ValidationError(f"Описание продукта не может содержать слово: {word}")
        return description









class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"




