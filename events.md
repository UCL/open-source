---
layout: default
title: Events
permalink: /events/
crumbs:
  - link: "/events/"
    text: "Events"
---

# Events

{% capture nowunix %}{{ 'now' | date: '%s' }}{% endcapture %}

<!-- FIXME -->

{% comment %}
{% assign doclist = site.data.samplelist.docs | sort: 'title'  %}

<ol>
{% for item in doclist %}
    <li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ol>
{% endcomment %}

## What's coming?

{% comment %}

Ideally, one could filter the future events as
{assign doclist = site.data.events | where_exp: 'item', 'item.date > site.time}
However, it doesn't work because date are dates, and site.time are datetimes
In the expression above you can't convert one to the other, and site.time or now converted to date will be as an string.
We could put all the dates as strings on the data, but that then will make it to have to convert them later.
{% endcomment %}

{% assign doclist =  site.data.events | sort: 'date' %}

<div class="row-fluid">
{% for event in doclist %}
 {% capture event_date %}{{event.date | date: '%s'}}{% endcapture %}
   {% if event_date >= nowunix %}
  <div class="span6" style="padding-bottom:15px">{% include event.html event=event%}</div>
  {% cycle '', '</div>' %}
  {% cycle '', '<div class="row-fluid">' %}
  {% endif %}
{% endfor %}
</div>

## What has happened?

<div class="row-fluid">
{% for event in doclist reversed %}
  {% capture event_date %}{{event.date | date: '%s'}}{% endcapture %}
  {% if event_date < nowunix %}
  {% comment %}
  Tried setting the include as md, but then the formatting and spacing becomes too difficult to get it right
  {% capture event_formatted %}{% include event.markdown event=event %}{% endcapture %}
  {{ event_formatted | markdownify }}
  {% endcomment %}
  <div class="span6" style="padding-bottom:15px">  {% include event.html event=event %}</div>
  {% cycle '', '</div>' %}
  {% cycle '', '<div class="row-fluid">' %}
  {% endif %}
{% endfor %}
