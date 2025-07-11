---
layout: default
title: Open Source Programme Office
permalink: /ospo/
crumbs:
  - link: "/ospo/"
    text: "OSPO"
---

### Proposals

| date | title(link) | funder | result | outcomes |
| ---- | ----------- | ------ | ------ | -------- |
{% for proposal in site.data.ospo.proposals -%}
| {{proposal[1].date}} | [{{proposal[1].title}}]({{proposal[1].url}}) | [{{proposal[1].funding}}]({{prposal[1].url_call}}) | {{proposal[1].result}} | {{proposal[1].outcomes}} |
{% endfor %}

### Talks/events submissions

| date | title(link) | event | result |
| ---- | ----------- | ----- | ------ |
{% for proposal in site.data.ospo.submissions -%}
| {{proposal[1].date}} | [{{proposal[1].title}}]({{proposal[1].url}}) | [{{proposal[1].event}}]({{prposal[1].event_url}}) | {{proposal[1].result}} |
{% endfor %}

### Activities

| date | title(link) | event | results |
| ---- | ----------- | ----- | ------- |
{% for proposal in site.data.ospo.events -%}
| {{proposal[1].date}} | [{{proposal[1].title}}]({{proposal[1].url}}) | [{{proposal[1].event}}]({{prposal[1].event_url}}) | {{proposal[1].results}} |
{% endfor %}
