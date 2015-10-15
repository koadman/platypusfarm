---
layout: page
title: Reviews
permalink: /reviews/
---

This is an archive of open peer reviews written by Darling lab members.

### Hosted at journal sites

Review for [An evaluation of alternative methods for constructing phylogenies from whole genome sequence data: a case study with Salmonella](https://peerj.com/articles/620v0.1/reviews/1/)

Review for [MetaBAT, an efficient tool for accurately reconstructing single genomes from complex microbial communities](https://peerj.com/articles/1165/reviews/)

### Hosted locally

<ul>
  {% for post in site.posts %}
    {% if post.category == "reviews"  %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      {{ post.excerpt }}
    </li>
    {% endif %}
  {% endfor %}
</ul>

