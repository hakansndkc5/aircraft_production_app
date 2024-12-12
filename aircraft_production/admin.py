from django.contrib import admin
from .models import Part, Aircraft, Team, Employee, AircraftPart, TeamPartAuthorization, UsedPart

admin.site.register(Part)
admin.site.register(Aircraft)
admin.site.register(Team)
admin.site.register(Employee)
admin.site.register(AircraftPart)
admin.site.register(TeamPartAuthorization)
admin.site.register(UsedPart)