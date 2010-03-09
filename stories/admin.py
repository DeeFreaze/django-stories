import os
from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from genericcollection import *

from models import Story
from stories.settings import RELATION_MODELS, INCLUDE_PRINT
from forms import StoryForm


if RELATION_MODELS:
    from models import StoryRelation

    class InlineStoryRelation(GenericCollectionTabularInline):
        model = StoryRelation
        # exclude = ('relation_type',)

if 'reversion' in settings.INSTALLED_APPS:
    from reversion.admin import VersionAdmin
    AdminModel = VersionAdmin
else:
    AdminModel = admin.ModelAdmin

HAS_CATEGORIES = 'categories' in settings.INSTALLED_APPS

class StoryOptions(AdminModel):
    revision_form_template = "admin/stories/reversion_form.html"
    form = StoryForm
    list_display = ('headline', 'status', 'publish_date', 'modified_date')
    list_filter = ('site', 'publish_date')
    search_fields = ('headline', 'teaser', 'body')
    date_hierarchy = 'publish_date'
    list_per_page = 25
    prepopulated_fields = {'slug': ('headline',)}
    filter_horizontal = ('authors',)
    if RELATION_MODELS:
        inlines = [InlineStoryRelation,]
    fieldsets = (
        (None,{
            'fields': ('headline', 'subhead', 'teaser', 'body')
        }), 
        ('Story data', {
            'fields': ('kicker', 'authors', 'non_staff_author', 'status', 'comments', )
        }),)
    if HAS_CATEGORIES:
        fieldsets = fieldsets + (
            ('Categories', {
                'fields': ('primary_category','categories')
            }),
        )
    if INCLUDE_PRINT:
        fieldsets = fieldsets + ('Print Information', {
            'fields': ('print_pub_date', 'print_section', 'print_page'),
            'classes': ('collapse',),
        })
    fieldsets = fieldsets + (('Advanced Options',{
            'fields': ('origin','slug',('publish_date', 'publish_time'), 'update_date', 'site', ),
            'classes': ('collapse',),
        }),)
    
    class Media:
        js = ('js/genericcollections.js',)

admin.site.register(Story, StoryOptions)
