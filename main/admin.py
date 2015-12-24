from django.contrib import admin
from django.contrib.admin import ModelAdmin
from models import *


# Register your models here.
class ActivityAdmin(ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_module_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        if request.user.is_superuser:
            return True
        elif obj.agent == request.user.profile:
            return True
        else:
            return False

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('agent')
            self.exclude.append('users')
            self.exclude.append('userCount')
        return super(ActivityAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'agent', None) is None:
            obj.agent = request.user.profile
        obj.save()

    def get_queryset(self, request):
        qs = super(ActivityAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(agent=request.user.profile)

admin.site.register(Profile)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Agent)
admin.site.register(Badge)
admin.site.register(Category)
