# Use of scrapping tool

### Usage

```
USAGE: ./generate.sh [URL]
      -s|--selector [Selector]  Define the precise selector to get instead of getting the full data
      -n|--name [Name]          Define file's name before generation (default = myelem.html)
```

Every call of the generate script require a link URL

### Options list

Every selector to select will be listed according to the a11.md found in the project, they're using the `xpath` synthaxe

-   `img`           Get all img elements
-   `*[@tabindex]`  Get all elements with a `tabindex` attribute in it
-   `head[@title]`  Get all `head` elements with a `title` attribute
-   `button`        Get all `button` elements
-   `h1`
-   `h2`
-   . . .

### More Options

When using the script without adding a `selector` options, the generator will copy the complete html data into your file