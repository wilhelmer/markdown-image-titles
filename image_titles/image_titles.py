from markdown.extensions import Extension
from markdown.inlinepatterns import LinkInlineProcessor
from xml.etree import ElementTree

IMAGE_REGEX = r'\!\[(?=[^\]])'

class ImageInlineProcessor(LinkInlineProcessor):

    def handleMatch(self, m, data):
        text, index, handled = self.getText(data, m.end(0))
        if not handled:
            return None, None, None

        src, title, index, handled = self.getLink(data, index)
        if not handled:
            return None, None, None

        img = ElementTree.Element('img')

        img.set('src', src)
        img.set('alt', text)

        if title is None:
            img.set("title", text)

        return img, m.start(0), index

class ImageTitleExtension(Extension):
    def extendMarkdown(self, md):
        md.inlinePatterns.register(ImageInlineProcessor(IMAGE_REGEX, md), 'image_title', 151)

def makeExtension(**kwargs):
    return ImageTitleExtension(**kwargs)
