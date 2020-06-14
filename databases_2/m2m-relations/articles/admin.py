from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Membership


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            form.cleaned_data
            # print(form.cleaned_data['is_main'])
            if form.cleaned_data != {}:
                if form.cleaned_data['is_main'] == True:
                    count +=1
        if count != 1:
            raise ValidationError('Тут всегда ошибка')
        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Membership
    extra =1
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    model = Scope