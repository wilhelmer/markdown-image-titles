# markdown-image-titles

Adds titles to Markdown images. The title text is taken from the alt text of the image.

The basic syntax for adding images in Markdown is like this:

```
![Alt text](assets/images/my-image.png "My title")
```

However, entering both the alt text and the title can be cumbersome.

With this extension, if no title is given, the alt text will automatically used as the title. 

## Example

```
![Image description](assets/images/my-image.png)
```

becomes 

```html
<img alt="Image description" src="assets/images/my-image.png" title="Image description" />
```

## Usage

```
pip install markdown-image-titles
```

``` python
md = markdown.Markdown(
    extensions=[
        'image_titles'
    ]
)
```
