Placeholder Image Server
========================

In the design of Single-Page-Applications (SPAs), managing state is a very critical aspect.
To control complexity, we tend to implement a "single source of truth" where very few, if not one, 
component is designed to be stateFUL - that is to manage the entire application state.
As a result, stateLESS components (such as REST APIs) are now great canditates for breaking an 
application into separate projects/services that can be deployed and tuned independently.

This placeholder image service takes a URL that indicates the image sizes and generates that image.
Of course, one can design the URL to even contain more information,
like color of the image or text to display within image. 
All that is needed to construct the requested image is contained within the URL, and 
there’s no need for authentication, thus this makes a case for a stateLESS application.
Note that Placeholder images are often used in prototypes or example projects.


## IMPORTANT

** Notice the use of the following,
   - Python: 3.6.3 (core language)
   - Django: 1.11.6 (web Framework)
   - Semantic-ui: 2.4.0 (css library)


## Get Started


- Create the project using ``django-admin.py startproject placeholder --template=project_name``
  This is abit "lighter" than the conventional django project setup process.

- Install the requirements, ``pip install requirements.txt`` 

- The core project module/file is ``placeholder.py`` that contains settings, urls and views.
  You can use django, in it's smallest version, and keep on scaling. 

- Take a closer look at how django discovers your "templates" and "static files".
  See "settings.configure" within placeholder.py

- start the project ``python placeholder.py runserver`` 


### Reference

- Working light with django: (http://www.oreilly.com/catalog/0636920032502)
- See more about django: (https://docs.djangoproject.com/en/dev/releases/1.11/)
- Read about PIL: (https://pillow.readthedocs.org/en/latest/installation.html.)


### Contribution guidelines
   - Writing more parameters to the HTTP Request (e.g. image color)
   - Other guidelines shall be issued with time.

### Who i talk to?
   - Contact: @MwamiTovi on GitHub
   - Email directly: matovu.synergy@gmail.com