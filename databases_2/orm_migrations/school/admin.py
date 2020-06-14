from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'display_teachers')
    list_filter = ('group', 'teacher')

    fieldsets = (
        (None, {
            'fields': ('name', 'group',)
        }),
        ('Учителя', {
            'fields': ('teacher',)
        }),
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    list_filter = ('subject',)
