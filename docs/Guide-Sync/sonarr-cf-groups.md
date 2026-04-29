# Sonarr - Custom Format Groups

Custom Format Groups are logical groupings of custom formats used by sync tools such as [Recyclarr](https://recyclarr.dev){:target="_blank" rel="noopener noreferrer"} and [Notifiarr](https://notifiarr.com){:target="_blank" rel="noopener noreferrer"}. Each group bundles related custom formats together for easier profile management and/or display.

!!! info

    Custom Format Groups are metadata used by external sync tools and are shown here for reference only. They are **not** designed to be imported into Sonarr and cannot be used directly within the application.

---

<!-- markdownlint-disable MD011 MD022 MD052 MD055 MD056 -->
{%- macro cf_slug(name) -%}{{ name | lower | replace('+', 'plus') | replace('(', '') | replace(')', '') | replace('/', '') | replace('.', '') | replace(':', '') | replace(',', '') | replace(' ', '-') | replace('--', '-') }}{%- endmacro -%}
{% set ns = namespace(current_category='') -%}
{% for key, group in sonarr['cf-groups']|dictsort -%}
{% if not (key.startswith('sqp-') or key.endswith('-sqp')) -%}
{% set category = group['name'].split(']')[0][1:] -%}
{% if category != ns.current_category -%}
{% set ns.current_category = category -%}

## {{ category }}

---

{% endif -%}

### {{ group['name'].split('] ')[1] }}

| Group Name | Trash ID | Default |
| --- | --- | :---: |
| {{ group['name'] }} | `{{ group['trash_id'] }}` | {% if group['default'] is defined and group['default'] == 'true' %}:white_check_mark:{% else %}:x:{% endif %} |

??? question "Description - [Click to show/hide]"

    {{ group['trash_description'] | replace('<br>', '\n    ') }}

| Custom Format | Trash ID | Required |
| --- | --- | :---: |
{% for cf in group['custom_formats'] -%}
| [{{ cf['name'] }}](../Sonarr/sonarr-collection-of-custom-formats.md#{{ cf_slug(cf['name']) }}) | `{{ cf['trash_id'] }}` | {% if cf['required'] %}:white_check_mark:{% else %}:x:{% endif %} |
{% endfor %}

{% if group.get('quality_profiles', {}).get('include', {}) -%}
??? abstract "Applicable Quality Profiles - [Click to show/hide]"

    | Quality Profile | Trash ID |
    | --- | --- |
    {%- for pname, pid in group.get('quality_profiles', {}).get('include', {})|dictsort %}
    {%- if '[sqp]' not in pname|lower %}
    | {{ pname }} | `{{ pid }}` |
    {%- endif %}
    {%- endfor %}

{% endif -%}

---

{% endif -%}
{% endfor -%}
<!-- markdownlint-enable MD011 MD022 MD052 MD055 MD056 -->
