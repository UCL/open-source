---
layout: default
title: OSPO Documents
---

# {{page.title}}

## 📜 Proposals

{% for doc in site.pages %}
	{% if doc.path contains 'ospo/documents/' %}
	   	{% if doc.category contains 'proposals' %}
- {{doc.date}}: [{{doc.title}}]({{doc.url | prepend: baseurl}})
        {% endif %}
    {% endif %}
{% endfor %}

## 🗣️ Talks
{% for doc in site.pages %}
	{% if doc.path contains 'ospo/documents/' %}
	   	{% if doc.category contains 'talk' %}
- {{doc.date}}: [{{doc.title}}]({{doc.url | prepend: baseurl}})
        {% endif %}
    {% endif %}
{% endfor %}

## 🗒️ Activities outputs

{% for doc in site.pages %}
	{% if doc.path contains 'ospo/documents/' %}
	   	{% if doc.category contains 'event' %}
- {{doc.date}}: [{{doc.title}}]({{doc.url | prepend: baseurl}})
        {% endif %}
    {% endif %}
{% endfor %}

