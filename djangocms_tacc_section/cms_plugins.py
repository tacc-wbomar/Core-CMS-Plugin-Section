from djangocms_style.cms_plugins import StylePlugin
from cms.plugin_pool import plugin_pool

from django.utils.translation import gettext_lazy as _

from .models import TaccsiteSection

# Plugins

@plugin_pool.register_plugin
class TaccsiteSectionPlugin(StylePlugin):
    """
    Patterns > "Section" Plugin
    https://confluence.tacc.utexas.edu/x/c5TtDg
    """
    module = 'TACC Site'
    model = TaccsiteSection
    name = _('Section')

    # Copied from djangocms_style with minor changes:
    #   - no 'Inline style settings'
    #   - use `custom_class_name` not `class_name`
    # FAQ: If user wants to override spacing, they may:
    #      - use Style plugin (if they have permission)
    #      - request Design & Dev standardize use case
    # https://github.com/django-cms/djangocms-style/blob/3.0.0/djangocms_style/cms_plugins.py#L15-L40
    fieldsets = (
        (None, {
            'fields': (
                'label',
                # To allow custom class_name in model
                ('custom_class_name', 'tag_type'),
                # ('class_name', 'tag_type'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'additional_classes',
                'id_name',
                'template',
                'attributes',
            ),
        }),
    )
