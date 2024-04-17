import datetime
current_time = datetime.datetime.now()
header = \
"""
---
title: TITLE
layout: post
author: befell
---
"""
title = input("Title: ")
with open("_posts/"+ current_time.strftime(f"%Y-%m-%d-{title.lower().replace(' ','-')}.md"), "w") as obj:
    obj.write(header.replace("TITLE", title))
