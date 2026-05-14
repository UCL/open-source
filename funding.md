---
layout: default
title: Funding opportunities
permalink: /funding/
crumbs:
  - link: "/funding/"
    text: "funding"

---

## Funding opportunities

The below funding opportunities are regularly updated from the listing in [CURIOSS funding site](https://curioss.org/resources/funding-opportunities/).

<div class="row-fluid">
{% assign sorted_funding = site.data.funding | sort %}
{% for funding_op in sorted_funding %}
  <div class="span6" style="padding-bottom:15px">{% include funding.html funding_op=funding_op %}</div>
  {% cycle '', '</div>' %}
  {% cycle '', '<div class="row-fluid">' %}
{% endfor %}
</div>

