from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from .models import About, GalleryImage, Review, HomePage


class AboutInline(admin.StackedInline):
    model = About
    extra = 1
    max_num = 1
    min_num = 1


# Custom Formset to Ensure Exactly 8 Gallery Images
class GalleryImageInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        if any(self.errors):
            return
        total_forms = len(
            [
                form
                for form in self.forms
                if form.cleaned_data and not form.cleaned_data.get("DELETE", False)
            ]
        )
        if total_forms != 8:
            raise ValidationError("You must upload exactly 8 images.")


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    formset = GalleryImageInlineFormSet
    extra = 8
    max_num = 8
    min_num = 8


# Custom Formset to Ensure Exactly 4 Reviews
class ReviewInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        total_reviews = 0 + len(
            [
                form
                for form in self.forms
                if form.cleaned_data and not form.cleaned_data.get("DELETE", False)
            ]
        )
        if total_reviews != 4:
            raise ValidationError("You must add exactly 4 reviews.")


class ReviewInline(admin.TabularInline):
    model = Review
    formset = ReviewInlineFormSet
    extra = 4
    max_num = 4


class HomePageAdmin(admin.ModelAdmin):
    inlines = [AboutInline, ReviewInline, GalleryImageInline]

    def has_add_permission(self, request):
        permitted = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if permitted and HomePage.objects.exists():
            permitted = False
        return permitted

    def change_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["show_save_and_add_another"] = False
        extra_context["show_save_and_continue"] = False
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context
        )

    def add_view(self, request, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["show_save_and_add_another"] = False
        extra_context["show_save_and_continue"] = False
        return super().add_view(request, form_url, extra_context=extra_context)


admin.site.register(HomePage, HomePageAdmin)
