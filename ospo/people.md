---
layout: default
title: People
crumbs:
  - link: /ospo/
    text: "OSPO"
short: "Who are we?"
---

# Who are we?

At the moment we are a group of people mostly based in ARC that are putting the things together to make this OSPO a reality.

<div class="row-fluid">
{% for member in site.data.members %}
{% include member.html member=member%}
  {% cycle '', '', '', '</div>' %}
  {% cycle '', '', '', '<div class="row-fluid">' %}
{% endfor %}
</div>

## Networks

Through this we are involved in the following networks:

<div class="row-fluid">
{% for member in site.data.ospo.networks %}
{% include network.html member=member%}
  {% cycle '', '', '</div>' %}
  {% cycle '', '', '<div class="row-fluid">' %}
{% endfor %}
</div>
