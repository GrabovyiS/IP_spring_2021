from django.contrib import admin

from .models import Records
from .models import Cities
from .models import Equipment_spots
from .models import Equipment_models
from .models import Month_avg
from .models import Year_avg

admin.site.register(Records)
admin.site.register(Cities)
admin.site.register(Equipment_spots)
admin.site.register(Equipment_models)
admin.site.register(Month_avg)
admin.site.register(Year_avg)
# Register your models here.
