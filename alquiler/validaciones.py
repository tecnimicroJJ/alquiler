from django.core.exceptions import ValidationError
from datetime import datetime

def fecha_nacimiento_validacion(value):
    fecha_actual = datetime.datetime.now()
    if(str(value) >= str(fecha_actual)):
        raise ValidationError('La fecha de nacimiento debe ser inferior a la fecha actual')

         
