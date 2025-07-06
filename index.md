---
layout: default
---

# Open Source

What does UCL do to promote Open Source (Software, Data, Hardware, Educational Resources, Science, ...)? In these pages you'll find our efforts to find that out.

Many of us are from [UCL's Advanced Research Computing Centre](https://ucl.ac.uk/arc), but we are not alone. Check our [about page]({{ 'about.html' | relative_url }}) to know who we are. From within ARC we are leading the efforts to build an [Open Source Programme Office in UCL]({{ 'ospo.html' | relative_url }}).

In these pages you will find:
- Announcements to [Activities & events](./events) that are happening in UCL (or near by) related with Open Source.
- [News](./news) related to Open Source that are of interest to the UCL community.
- All the work done to create and consolidate the [Open Source Programme Office]({{ 'ospo.html' | relative_url }}), including submission to talks and funding proposals.
- And a number of [Guides](./guides) that you may find useful.

Our announcements and news page provide an <i class="fa-solid fa-rss"></i> [RSS feed]({{"feed.xml" | prepend: baseurl}}) so you can be up to date without having to visit our page all the time, and the listed events are also available on our [published calendar](https://outlook.office365.com/owa/calendar/30254fbb15664ffaad6db9083612c8fc@ucl.ac.uk/0b3efa837e1e463ebf8b0d56d134c42d11556152029707409414/calendar.ics).

## Latest News  <a href="{{'feed.xml' | prepend: baseurl}}"> <span class="icon-image  icon--github"> <svg viewBox="0 0 16 16"> <path fill="#000000" d="{{ site.data.icons.rss_logo }}"/> </svg> </span></a>

<!-- List of latest 5 news articles -->
{% for item in site.posts limit:5 %} <!-- site.posts is already sorted -->
- 📆 {{item.date | date: "%Y-%m-%d"}} - [{{item.title}}]({{item.url}})
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
