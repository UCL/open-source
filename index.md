---
layout: default
---

# Open Source

<section class="content-box news-summary">

UCL has a long history of open-source software development and open research.
Openness and inclusion form part of UCL's core values.

</section>

These pages are dedicated to supporting and promoting open-source software and materials by UCL staff and students.
We are also in the process of building an [Open Source Programme Office at UCL](./ospo).
For open research, the library has a dedicated [Office for Open Science and Scholarship](https://www.ucl.ac.uk/library/open-science-research-support/ucl-office-open-science-and-scholarship).

## Looking for advice?
We have a few [guides and links](./guides) that you may find useful.
In particular, [UCL's position on open source software licenses](./guides/ucl-and-oss.html).

Also in these pages you will find:

- Announcements of [Activities & events](./events) that are happening in UCL (or nearby) related to open source.
- [News](./news) related to Open Source that is of interest to the UCL community.
- Work done to create and consolidate the [Open Source Programme Office](./ospo), including talks given at conferences and funding proposals.

Our [news](./news) page is available as an <i class="fa-solid fa-rss"></i> [RSS feed]({{"feed.xml" | prepend: baseurl}}), and our upcoming events as a [published calendar](https://outlook.office365.com/owa/calendar/30254fbb15664ffaad6db9083612c8fc@ucl.ac.uk/0b3efa837e1e463ebf8b0d56d134c42d11556152029707409414/calendar.ics).

## Showcase

Here are some of the open-source software projects in the UCL community that have a good [OSSF Scorecard aggregate score](https://scorecard.dev/):

<div class="row-fluid">
{% for repo in site.data.repos %}
{% include showcase_project.html repo=repo %}
  {% cycle '', '</div>' %}
  {% cycle '', '<div class="row-fluid">' %}
{% endfor %}
</div>

## Latest News <a href="{{'feed.xml' | prepend: baseurl}}"> <span class="icon-image  icon--github"> <svg viewBox="0 0 16 16"> <path fill="#000000" d="{{ site.data.icons.rss_logo }}"/> </svg> </span></a>

<!-- List of latest 2 news articles -->

{% for item in site.posts limit:2 %} <!-- site.posts is already sorted -->

- 📆 {{item.date | date: "%Y-%m-%d"}} - [{{item.title}}]({{item.url | prepend: site.baseurl }})
  {% endfor %}

## Upcoming events [🗓️](https://outlook.office365.com/owa/calendar/30254fbb15664ffaad6db9083612c8fc@ucl.ac.uk/0b3efa837e1e463ebf8b0d56d134c42d11556152029707409414/calendar.ics)

{% capture nowunix %}{{ 'now' | date: '%s' }}{% endcapture %}
{% assign doclist =  site.data.events | sort: 'date' %}
{% for event in doclist %}
{%- capture event_date -%}{{event.date | date: '%s'}}{%- endcapture -%}
{% if event_date >= nowunix %}

- 📆 {{event.date | date: "%Y-%m-%d"}} - [{{event.title}}]({{event.url}}) (by {{event.organiser}})
  {%- endif -%}
  {% endfor %}
