from django.contrib import admin
from .models import (
    RequestList,
    RequestType,
    IndianStates,
    StatusList,
) 

# Register your models here.
admin.site.register(RequestList)
admin.site.register(RequestType)
admin.site.register(IndianStates)
admin.site.register(StatusList)