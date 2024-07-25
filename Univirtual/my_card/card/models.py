from django.db import models
class Card(models.Model):
    # Campos del modelo
    name = models.CharField(max_length=30)
    excel_file = models.FileField(default='default_value', upload_to='uploads/')
 

    def __str__(self):
        return f"datos de la persona: {self.name}  {self.excel_file}"
