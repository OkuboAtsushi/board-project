from django.contrib import admin

from .models import BoardModel


class BoardModelAdmin(admin.ModelAdmin):
    readonly_fields = ('read_user_ids', )


admin.site.register(BoardModel, BoardModelAdmin)
