from example.settings import *

STORY_SETTINGS.update({
    'RELATION_MODELS': [
        'simpleapp.basicphoto',
        'simpleapp.basicvideo'
    ],
})

INSTALLED_APPS += ('stories.relations',)
