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

# Models

class TaccsiteSection(CMSPlugin):
    """
    Patterns > "Section" Model
    https://confluence.tacc.utexas.edu/x/c5TtDg
    """
    class_name = models.CharField(
        verbose_name=_('Class name'),
        choices=CLASS_CHOICES,
        default=CLASS_CHOICES[0][0],
        blank=True,
        max_length=255,
    )
