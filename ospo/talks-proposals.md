---
layout: default
title: Talks, Event Submissions and Proposals
crumbs:
  - link: /ospo/talks-proposals
    text: "Talks, Event Submissions, and Proposals"
---

### Talks and Event Submissions

| Date | Title       | Event | Result |
| ---- | ----------- | ----- | ------ |
{% for proposal in site.data.ospo.submissions -%}
| {{proposal[1].date}} | [{{proposal[1].title}}]({{proposal[1].link}}) | [{{proposal[1].event}}]({{proposal[1].event_link}}) | {{proposal[1].result}} |
{% endfor %}

### Funding Proposals

| Date | Title       | Funder | Result | Outcomes |
| ---- | ----------- | ------ | ------ | -------- |
{% for proposal in site.data.ospo.proposals -%}
| {{proposal[1].date}} | [{{proposal[1].title}}]({{proposal[1].link}}) | [{{proposal[1].funding}}]({{proposal[1].link_call}}) | {{proposal[1].result}} | {{proposal[1].outcomes}} |
{% endfor %}
