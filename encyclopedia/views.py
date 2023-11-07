from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from markdown2 import markdown
from random import choice
from os.path import exists
from os import remove

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    if entry := util.get_entry(title):
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": markdown(entry),
        })
    else:
        return render(request, "encyclopedia/unfound.html", {
            "title": title,
        })


def edit(request, title):
    if request.method == "GET":
        entry_data = {
            "title_field": title,
            "content_field": util.get_entry(title),
        }
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "form": CreateEntry(initial=entry_data),
        })
    elif request.method == "POST":
        form = CreateEntry(request.POST)
        if form.is_valid():
            new_title = form.cleaned_data["title_field"]
            content = form.cleaned_data["content_field"]
            if title != new_title:
                remove(f"entries/{title}.md")
            util.save_entry(new_title, content)
            return HttpResponseRedirect(reverse("encyclopedia:entry", args=[new_title]))
        else:
            return render(request, "encyclopedia/edit.html", {
                "title": title,
                "form": CreateEntry(initial=entry_data),
            })


def search(request):
    query = request.GET["q"]
    query_lower = query.lower().strip()
    entries = util.list_entries()
    entries_lower = map(str.lower, entries)
    if query_lower in entries_lower:
        for entry in entries:
            if query_lower == entry.lower():
                return HttpResponseRedirect(reverse("encyclopedia:entry", args=[entry]))
    else:
        matches = [entry for entry in entries if query_lower in entry.lower()]
        return render(request, "encyclopedia/results.html", {
            "query": query,
            "matches": matches,
        })


def random(request):
    entry = choice(util.list_entries())
    return HttpResponseRedirect(reverse("encyclopedia:entry", args=[entry]))


def create(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create.html", {
            "form": CreateEntry(),
        })
    elif request.method == "POST":
        form = CreateEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title_field"]
            content = form.cleaned_data["content_field"]
            if exists(f"entries/{title}.md"):
                return render(request, "encyclopedia/exists.html", {
                    "title": title,
                })
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse("encyclopedia:entry", args=[title]))
        else:
            return render(request, "encyclopedia/create.html", {
                "form": CreateEntry(),
            })


class CreateEntry(forms.Form):
            title_field = forms.CharField(
                label="Title",
                widget=forms.TextInput(attrs={"placeholder":"Title of the Entry"}),
            )
            content_field = forms.CharField(
                label="Content",
                widget=forms.Textarea(attrs={
                    "placeholder": "Markdown Content of the Entry",
                    "cols": 120,
                    "rows": 10,
                }),
            )
