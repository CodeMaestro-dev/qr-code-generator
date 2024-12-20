from django import forms
from . import models

class CreateQRCode(forms.ModelForm):
    class Meta:
        model = models.QRCode
        fields = ['qr_code_text']
        labels = {
            'qr_code_text': 'Enter Text for QR Code',
        }
