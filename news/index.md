---
layout: default
title: News
crumbs:
  - link: "/news/"
    text: "News"
---

{% if site.posts.size > 0 %}

  <h2>Latest News</h2>
  <ul class="posts">
  {% for post in site.posts %}
  {% assign post_url = post.url | prepend:site.baseurl %}
  <li>
    <a href="{{ post_url }}">
      {{ post.date | date_to_string }}
    </a>
    &raquo;
    <a href="{{ post_url }}">{{ post.title }}</a>

    <p class="entry">
      {{ post.content | strip_html | truncate:250 }}
      <a href="{{ post_url }}">Read more…</a>
    </p>
  </li>
  {% endfor %}
</ul>

{% endif %}
