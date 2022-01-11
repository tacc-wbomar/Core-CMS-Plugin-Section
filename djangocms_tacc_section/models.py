from django.conf import settings

from djangocms_style.models import Style

from django.db import models
from django.utils.translation import gettext_lazy as _

# Constants

CLASS_BASE = getattr(
    settings,
    'DJANGOCMS_TACCSITE_SECTION_CLASSNAMES_REQUIRED',
    '_example_tacc_section_class_constant',
)
CLASS_CHOICES = getattr(
    settings,
    'DJANGOCMS_TACCSITE_SECTION_CLASSNAMES_CHOICES',
    [
        ('_example_tacc_section_class_a', 'Example Class A'),
        ('_example_tacc_section_class_b', 'Example Class B'),
    ],
)
TAG_CHOICES = getattr(
    settings,
    'DJANGOCMS_TACCSITE_SECTION_TAGS',
    ['section', 'article', 'header', 'footer', 'aside', 'div'],
)
TAG_CHOICES = tuple((entry, entry) for entry in TAG_CHOICES)

# Models

# This inheritence causes django-cms/django-cms#5913
# SEE: https://github.com/django-cms/django-cms/issues/5913
# FAQ: No `AbstractStyle` exists
# NOTE: Possible solution might be custom `cmsplugin_ptr`
# SEE: https://github.com/django-cms/djangocms-style/blob/315e8ef/djangocms_style/models.py#L137-L146
class TaccsiteSection(Style):
    """
    Patterns > "Section" Model
    https://confluence.tacc.utexas.edu/x/c5TtDg
    """
    custom_class_name = models.CharField(
        verbose_name=_('Style'),
        choices=CLASS_CHOICES,
        default=CLASS_CHOICES[0][0],
        blank=False,
        max_length=255,
    )
    custom_tag_type = models.CharField(
        verbose_name=_('Tag'),
        choices=TAG_CHOICES,
        default=TAG_CHOICES[0][0],
        max_length=255,
    )

    def save(self, *args, **kwargs):
        self.class_name = self.custom_class_name
        self.tag_type = self.custom_tag_type
        super().save(*args, **kwargs)
