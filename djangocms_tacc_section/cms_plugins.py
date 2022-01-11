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

    # Copied and reduced from djangocms_style
    # https://github.com/django-cms/djangocms-style/blob/3.0.0/djangocms_style/cms_plugins.py#L15-L40
    fieldsets = (
        (None, {
            'fields': (
                # TACC: To allow custom choices in model
                ('custom_class_name', 'custom_tag_type'),
                # ('class_name', 'tag_type'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'additional_classes',
                'id_name',
                'attributes',
            ),
        }),
    )
