"""Provides the default settings for the news app
"""
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

DEFAULT_STATUS_CHOICES = (
    (1, _(u'DRAFT')),
    (2, _(u'READY FOR EDITING')),
    (3, _(u'READY TO PUBLISH')),
    (4, _(u'PUBLISHED')),
    (5, _(u'REJECTED')),
    (6, _(u'UN-PUBLISHED')),
)
STATUS_CHOICES = getattr(settings, 'STORY_STATUS_CHOICES', DEFAULT_STATUS_CHOICES)

DEFAULT_DEFAULT_STATUS = 1
DEFAULT_STATUS = getattr(settings, 'STORY_DEFAULT_STATUS', DEFAULT_DEFAULT_STATUS)

DEFAULT_PUBLISHED_STATUS = 4
PUBLISHED_STATUS = getattr(settings, 'STORY_PUBLISHED_STATUS', DEFAULT_PUBLISHED_STATUS)

DEFAULT_MARKUP_CHOICES = (
    (0, _(u'None')),
    (1, _(u'Creole')),
    (2, _(u'reStructuredText')),
    (3, _(u'Textile')),
    (4, _(u'Markdown')),
    (5, _(u'HTML')),
)
MARKUP_CHOICES = getattr(settings, 'STORY_MARKUP_CHOICES', DEFAULT_MARKUP_CHOICES)

DEFAULT_DEFAULT_MARKUP = 0
DEFAULT_MARKUP = getattr(settings, 'STORY_DEFAULT_MARKUP', DEFAULT_DEFAULT_MARKUP)

DEFAULT_ORIGIN_CHOICES = (
    (0, _('Admin')),
)
ORIGIN_CHOICES = getattr(settings, 'STORY_ORIGIN_CHOICES', DEFAULT_ORIGIN_CHOICES)

DEFAULT_DEFAULT_ORIGIN = 0
DEFAULT_ORIGIN = getattr(settings, 'STORY_DEFAULT_ORIGIN', DEFAULT_DEFAULT_ORIGIN)

DEFAULT_RELATION_MODELS = None
RELATION_MODELS = getattr(settings, 'STORY_RELATION_MODELS', DEFAULT_RELATION_MODELS)