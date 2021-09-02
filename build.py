# index page
top = open('./templates/top.html').read()
content = open('./content/index.html').read()
bottom = open('./templates/bottom.html').read()
full_site = top + content + bottom
open('./docs/index.html', 'w+').write(full_site)

# blog page
top = open('./templates/top.html').read()
content = open('./content/blog.html').read()
bottom = open('./templates/bottom.html').read()
full_site = top + content + bottom
open('./docs/blog.html', 'w+').write(full_site)

# about page
top = open('./templates/top.html').read()
content = open('./content/about.html').read()
bottom = open('./templates/bottom.html').read()
full_site = top + content + bottom
open('./docs/about.html', 'w+').write(full_site)

# projects page
top = open('./templates/top.html').read()
content = open('./content/projects.html').read()
bottom = open('./templates/bottom.html').read()
full_site = top + content + bottom
open('./docs/projects.html', 'w+').write(full_site)
