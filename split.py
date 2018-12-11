from sys import stdin
import re

seen_preamble = False
section_slugs = set()
current_section = None
current_section_slug = None
sections = []
link_regex = re.compile(r"\]\(#([-a-zA-Z0-9]+)\)")
subsection_slugs = {}
copyright_notice = (
    "_This material was written by [Aasmund Eldhuset](https://eldhuset.net/); "
    "it is owned by [Khan Academy](https://www.khanacademy.org/) and is licensed for use under "
    "[CC BY-NC-SA 3.0 US](https://creativecommons.org/licenses/by-nc-sa/3.0/us/). "
    "Please note that this is not a part of Khan Academy's official product offering._\n\n---\n\n\n")

def substitute_link(match):
    link = match.group(1)
    if link in section_slugs:
        return "]({0}.html)".format(link)
    elif link in subsection_slugs:
        return "]({0}.html#{1})".format(subsection_slugs[link], link)
    else:
        print "Unknown:", link
        return link

def slugify(title):
    return "".join(c for c in title if c.isalnum() or c in [" ", "-"]).replace(" ", "-").lower()

with open("README.md") as f:
    for line in f:
        if not seen_preamble:
            if line == "---\n":
                seen_preamble = True
                current_section = []
                sections.append(("Introduction", "introduction", current_section))
        elif line == "---\n":
            break
        elif line.startswith("## "):
            title = line[3:-1]
            if title == "Contents":
                current_section.append(line)
                continue
            current_section = []
            current_section_slug = slugify(title)
            section_slugs.add(current_section_slug)
            sections.append((title, current_section_slug, current_section))
        elif not current_section and line == "\n":
            pass
        elif line.startswith("#"):
            current_section.append(line[1:])
            title = line.replace("#", "")[1:-1]
            subsection_slugs[slugify(title)] = current_section_slug
        else:
            current_section.append(line)

with open("kotlinlang.org.yaml", "w") as yaml:
    for i, (title, slug, section) in enumerate(sections):
        filename = "{0:02}-{1}.md".format(i, slug)
        yaml.write("- md: {0}\n  url: {1}.html\n  title: \"{2}\"\n\n".format(filename, slug, title))
        for j, line in enumerate(section):
            section[j] = link_regex.sub(substitute_link, line)
        navigation = []
        if i > 0:
            navigation.append(u"[\u2190 Previous: {0}]({1}.html)".format(*sections[i - 1][0:2]))
        if i < len(sections) - 1:
            navigation.append(u"[Next: {0} \u2192]({1}.html)".format(*sections[i + 1][0:2]))
        section.append(u"\n\n---\n\n{0}\n".format(" | ".join(navigation)))
        with open(filename, "w") as md:
            md.write(copyright_notice)
            md.write(u"".join(s for s in section).encode("utf-8"))
