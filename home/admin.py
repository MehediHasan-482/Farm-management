from django.contrib import admin
from .models import user
from .models import signup
from .models import cow
from .models import Contact
from .models import protfolio
from .models import cart

# Register your models here.
admin.site.register(user)
admin.site.register(signup)
admin.site.register(cow)
admin.site.register(Contact)
admin.site.register(protfolio)
admin.site.register(cart)

