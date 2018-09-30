from django.contrib import admin
from dashapp.models import Team, Members, FemalePresenter, MalePresenter

# Register your models here.
admin.site.register(Team)
admin.site.register(Members)
admin.site.register(FemalePresenter)
admin.site.register(MalePresenter)
