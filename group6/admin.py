from django.contrib import admin
from group6.models import *

#register all models (Table) in group6 to admin page of django
admin.site.register(ProjectG6)
admin.site.register(CategoriesProject)
admin.site.register(ApproveProjectForm)
admin.site.register(ResearchProjectForm)
admin.site.register(OfferProjectForm)
admin.site.register(TimeLineForm)
admin.site.register(StepInTimeLine)
admin.site.register(NotificationProject)
admin.site.register(Message)
