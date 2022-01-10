## Texas Advanced Computing Center
# Django CMS Plugin: "Section"

This plugin creates a customizable "Section" (`<section>`) wrapper.

- __`__dist-name__`__: `djangocms-tacc-section`
- __`__package_name__`__: `djangocms_tacc_section`
- __`__ClassName__`__: `TaccsiteSection`
- __"Plugin Name"__: "Section"

## For Plugin Developer

After cloning this repository for your plugin:

1. Follow https://github.com/tacc-wbomar/Core-CMS-Plugin/wiki/Core-CMS-Plugin-Development-Quick-Start.
2. Remove this section from your repository's `README.md`.


## Quick Start

1. Follow https://github.com/tacc-wbomar/Core-CMS-Plugin/wiki/Core-CMS-Plugin-Usage-Quick-Start.

2. (Optional) Add properties and values to your Django project's settings.

    - __`DJANGOCMS_TACCSITE_SECTION_TAGS`__

        A list of tags from which the user can choose one to be the element of the wrapper.

        ```python
        DJANGOCMS_TACCSITE_SECTION_TAGS = [
            'section', 'article', 'header', 'footer', 'aside', 'div'
        ]
        ```

    - __`DJANGOCMS_TACCSITE_SECTION_CLASSNAMES_CONSTANT`__

        A string of classes which will alwyas be added to each wrapper.

        ```python
        # (Generic Example)
        DJANGOCMS_TACCSITE_SECTION_CLASSNAMES_CONSTANT = '_example_tacc_section_class_constant'
        ```

        ```python
        # (Specific Example)
        DJANGOCMS_TACCSITE_SECTION_CLASSNAMES_CONSTANT = 'o-section  some-other-constant'
        ```

    - __`DJANGOCMS_TACCSITE_SECTION_CLASSNAMES_CHOICES`__

        A list of classes from which the user can choose one to be added to the wrapper.

        ```python
        # (Generic Example)
        DJANGOCMS_TACCSITE_SECTION_CLASSNAMES_CHOICES = [
            ('_example_tacc_section_class_a', 'Example Class A'),
            ('_example_tacc_section_class_b', 'Example Class B'),
        ]
        ```

        ```python
        # (Specific Example)
        DJANGOCMS_TACCSITE_SECTION_CLASSNAMES_CHOICES = [
            ('o-section--style-light', 'Light Background, Dark Text'),
            ('o-section--style-dark', 'Dark Background, Light Text'),
        ]
        ```

## Usage

1. Add instance of plugin to a page.
1. Configure the plugin instance.
1. (Optional) Add and nest plugin instances to support content inside.
1. See plugin render markup that matches configuration (and wraps nested plugin content).

## Features

1. Renders HTML element and classnames (as configured).
1. Renders nested plugin instances to wrap content.
