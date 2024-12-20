from django.db import models

class QRCode(models.Model):
    qr_code_text = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.qr_code_text
