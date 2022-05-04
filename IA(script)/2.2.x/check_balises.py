import os, re

img = {
    'alt': 1
}

btn = {
    'type': 1
}

tbindex = {
    'value' : 1
}

thscope = {
    'scope': 1,
    'good': 1
}

def image(line):
    if line.find("alt=") !=  -1:
        img['alt'] = 0

def button(line):
    if line.find("button") != -1:
        btn['type'] = 0

def tabindex(line):
    if line.find("tabindex=") != -1:
        value = line[line.find("tabindex=") + 2]
    if value != 0:
        tbindex['value'] = 0
    

def lang(line):
    if line.find('lang=') == -1:
        print(f'argument lang manquant dans la balise html: {line}')

def scope(line):
    if line.find('scope') != -1:
        name = line[line.find('scope=') + 7: line.find('"', line.find('scope=') + 7)]
        if name is not ["scope", "col"]:
            thscope['good'] = 0
    else:
        thscope['scope'] = 0


def report_error(line):
    if tbindex['value'] == 0:
        print(f'Problème de tab index\t\t{line.strip()}')
    if btn['type'] == 0:
        print(f'Pas de type dans le button\t\t{line.strip()}')
    if img['alt'] == 0:
        print(f'Pas de alt pour cette image\t\t{line.strip()}')
    if thscope['scope'] == 0:
        print(f'Pas de scope dans la balise th\t\t{line.strip()}')
    if thscope['good'] == 0:
        print(f'Scope non valide sur la balise th\t\t{line.strip()}')
    img['alt'] = btn['type'] = tbindex['value'] = thscope['scope'] = thscope['good'] = 1

def check_tag(lines):
    header = 0
    for line in lines:
        if line.find('<img ') != -1:
            img = image(line)
        elif line.find('<button') != -1:
            button(line)
        if line.find("tabindex") != -1:
            tabindex(line)
        if line.find("<html") != -1:
            lang(line)
        if line.find("<h1 "):
            header += 1
        if line.find("<th ") != -1:
            scope(line)
        report_error(line)
    if header > 1:
        print(f"Plus que 1 balise H1")


