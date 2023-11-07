# Wiki

This project is part of Harvard's **CS50’s Web Programming with Python and JavaScript** cours.  
See [https://cs50.harvard.edu/web/2020/projects/1/wiki/](https://cs50.harvard.edu/web/2020/projects/1/wiki/).  

## Description

This program is a small-scale wiki, in which some programming languages and frameworks are defined.  

## Usage

Run `python manage.py runserver` inside the root directory of the project in your terminal. Follow the instructions in your terminal to run the according website in your browser or to stop the project.  

On the index page you see a navigation bar to the left with `Wiki` as title. On the right you see a list of all entries in alphabetical order, that redirect you to an according entry if clicked on them.  

Type a search request in the search bar to get redirected to an entry with the same title as the request. If the search request doesn't match an entry title, you get redirected to a search page with a list of all entries, that have the search request in their title and redirect you to that entry if clicked on them. Click on `Home` to get redirected to the index page.  

On an entry page, you cann see the entire entry as text. Click on `Edit` to get redirected to an edit page for that entry. On the edit page you can edit the title of the entry and its content text. The content text must be written in `Markdown` format. Click on `Edit` to save the changes. If the edit was successfull, you'll be redirected to the edited entry page. If the edit wasn't successfull, you'll be redirected to an edit page with the original content.  

Click on `Create New Page` to get redirected to an creation page for a new entry. On the creation page you can enter the title of the entry and its content text. The content text must be written in `Markdown` format. Click on `Create` to save the new entry. If the creation was successfull, you'll be redirected to the created entry page. If the creation wasn't successfull, you'll be redirected to a blanc creation page.  

Click on `Random Page` to get redirected to a random entry page.  

## Dependencies

- [CSS 3](https://www.w3.org/Style/CSS/Overview.en.html) or higher  
- [HTML 5.2](https://html.spec.whatwg.org/multipage/) or higher  
- PyPI [Django 4.2.3](https://pypi.org/project/Django/) or higher  
- PyPI [markdown2 2.4.10](https://pypi.org/project/markdown2/) or higher  
- [Python 3.11.3](https://www.python.org/downloads/) or higher  

## Structure

The project is structured as follows:  

- **wiki** (root directory of the entire project)  
  - **encyclopedia** (root directory of the application "encyclopedia")  
    - **migrations** ()  
      - **\_\_init\_\_.py** ()  
    - **static** (directory for the static files of the encyclopedia application)  
      - **encyclopedia** (subdirectory for the static files of the encyclopedia application)  
        - **styles.css** (styles for the encyclopedia application)  
    - **templates** (directory for the HTML templates of the encyclopedia application)  
      - **encyclopedia** (subdirectory for the HTML templates of the encyclopedia application)  
        - **entry.html** (HTML file template for the entries of the encyclopedia application)  
        - **index.html** (HTML file template for the start page of the encyclopedia application)  
        - **layout.html** (HTML file template layout for all pages of the encyclopedia application)  
        - **unfound.html** (HTML file template for unfound entries of the encyclopedia application)  
    - **\_\_init\_\_.py** ()  
    - **admin.py** ()  
    - **apps.py** ()  
    - **models.py** ()  
    - **test.py** ()  
    - **urls.py** (Python file with URLs that can be visited inside the encyclopedia application and are leading to according "views")  
    - **util.py** (Python file with functions to interact with entries of the encyclopedia application)  
    - **views.py** (Python file with functions that return HTTP responses to visited URLs inside the encyclopedia application)  
  - **entries** (directory for the entries of the encyclopedia application)  
    - **CSS.md** (Markdown file with entry for the CSS language)  
    - **Django.md** (Markdown file with entry for the Django framework)  
    - **Git.md** (Markdown file with entry for the Git language)  
    - **HTML.md** (Markdown file with entry for the HTML language)  
    - **Python.md** (Markdown file with entry for the Pythonlanguage)  
  - **wiki** (subdirectory of the project "wiki")  
    - **\_\_init\_\_.py** ()  
    - **asgi.py** ()  
    - **settings.py** (Python file with settings for wiki project)  
    - **urls.py** (Python file with URLs that can be visited inside the project and are leading to according "views")  
    - **wsgi.py** ()  
  - **db.sqlite3** (database of the project)  
  - **manage.py** (controlls commands for the project)  

## Assignment

The assignment was defined as follows:  

> **Getting Started**  
> Download the distribution code from [https://cdn.cs50.net/web/2020/spring/projects/1/wiki.zip](https://cdn.cs50.net/web/2020/spring/projects/1/wiki.zip) and unzip it.  
>
> **Understanding**  
> In the distribution code is a Django project called `wiki` that contains a single app called `encyclopedia`.  
>
> First, open up `encyclopedia/urls.py`, where the URL configuration for this app is defined. Notice that we’ve started you with a single default route that is associated with the `views.index function.  
>`
> Next, look at `encyclopedia/util.py`. You won’t need to change anything in this file, but notice that there are three functions that may prove useful for interacting with encyclopedia entries. `list_entries` returns a list of the names of all encyclopedia entries currently saved. `save_entry` will save a new encyclopedia entry, given its title and some Markdown content. `get_entry` will retrieve an encyclopedia entry by its title, returning its Markdown contents if the entry exists or `None` if the entry does not exist. Any of the views you write may use these functions to interact with encyclopedia entries.  
>
> Each encyclopedia entry will be saved as a Markdown file inside of the `entries/` directory. If you check there now, you’ll see we’ve pre-created a few sample entries. You’re welcome to add more!  
>
> Now, let’s look at `encyclopedia/views.py`. There’s just one view here now, the `index` view. This view returns a template `encyclopedia/index.html`, providing the template with a list of all of the entries in the encyclopedia (obtained by calling `util.list_entries`, which we saw defined in `util.py`).  
>
> You can find the template by looking at `encyclopedia/templates/encyclopedia/index.html`. This template inherits from a base `layout.html` file and specifies what the page’s title should be, and what should be in the body of the page: in this case, an unordered list of all of the entries in the encyclopedia. `layout.html`, meanwhile, defines the broader structure of the page: each page has a sidebar with a search field (that for now does nothing), a link to go home, and links (that don’t yet work) to create a new page or visit a random page.  
>
> **Specification**  
> Complete the implementation of your Wiki encyclopedia. You must fulfill the following requirements:
>
> - **Entry Page:** Visiting `/wiki/TITLE`, where `TITLE` is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.  
>   - The view should get the content of the encyclopedia entry by calling the appropriate `util` function.  
>   - If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.  
>   - If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.  
> - **Index Page:** Update `index.html` such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.  
> - **Search:** Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.  
>   - If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.  
>   - If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were `ytho`, then `Python` should appear in the search results.  
>   - Clicking on any of the entry names on the search results page should take the user to that entry’s page.  
> - **New Page:** Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.  
>   - Users should be able to enter a title for the page and, in a [textarea](https://www.w3schools.com/tags/tag_textarea.asp), should be able to enter the Markdown content for the page.  
>   - Users should be able to click a button to save their new page.  
>   - When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.  
>   - Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.  
> - **Edit Page:** On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a `textarea`.  
>   - The `textarea` should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial `value` of the `textarea`).  
>   - The user should be able to click a button to save the changes made to the entry.  
>   - Once the entry is saved, the user should be redirected back to that entry’s page.  
> - **Random Page:** Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.  
> - **Markdown to HTML Conversion:** On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user. You may use the [python-markdown2](https://github.com/trentm/python-markdown2) package to perform this conversion, installable via `pip3 install markdown2`.  
>   - Challenge for those more comfortable: If you’re feeling more comfortable, try implementing the Markdown to HTML conversion without using any external libraries, supporting headings, boldface text, unordered lists, links, and paragraphs. You may find [using regular expressions in Python](https://docs.python.org/3/howto/regex.html) helpful.  
>
> **Hints**  
>
> By default, when substituting a value in a Django template, Django HTML-escapes the value to avoid outputting unintended HTML. If you want to allow for an HTML string to be outputted, you can do so with the [safe](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#safe) filter (as by adding `|safe` after the variable name you’re substituting).  

## Submission

The following were changed in the distribution code:  

- Inside `views.py` file of the encyclopedia application: added the `entry`, `edit`, `search`, `random` and `create` functions and the `CreateEntry` class  
- Inside `views.py` file of the encyclopedia application: imported the `markdown2`, `random`, `os.path` and `os` modules  
- Inside `urls.py` file of the encyclopedia application: added the `path` functions with names `entry`, `edit`, `search`, `random` and `create` inside the `urlpatterns` list  
- Inside `urls.py` file of the encyclopedia application: added `app_name` variable with value `encyclopedia`
- Inside `layout.html` file in the `encyclopedia` directory in the `templates` directory of the encyclopedia application:  
  - changed `href` attribute of `a` element inside of first `div` element inside of `div` element with class `sidebar col-lg-2 col-md-3` to `"{% url 'encyclopedia:index' %}"`  
  - changed `href` attribute of `a` element inside of first `div` element inside of `div` element with class `sidebar col-lg-2 col-md-3` to `"{% url 'encyclopedia:index' %}"`  
  - embedded value of third `div` element inside of `div` element with class `sidebar col-lg-2 col-md-3` in `a` element  
  - embedded value of second `div` element inside of `div` element with class `sidebar col-lg-2 col-md-3` in `a` element  
- Inside `index.html` file in the `encyclopedia` directory in the `templates` directory of the encyclopedia application: embedded value of `li` element inside of `ul` element in an `a` element with `href` attribute and `"{% url 'encyclopedia:entry' title=entry %}"` as its value  
- Inside the `encyclopedia` directory in the `templates` directory of the encyclopedia application: added the `entry.html`, `unfound.html`, `results.html`, `create.html`, `edit.html` and `exists.html` files  
- Inside the `style.css` file in the `encyclopedia` directory in the `static` directory of the encyclopedia application: deleted the `textarea` selector and added the `.edit_form` selector  
- Inside the `util.py` file inside the encyclopedia application: added a `key` argument to the `sorted` function inside the argument of the `list_entries` function  
