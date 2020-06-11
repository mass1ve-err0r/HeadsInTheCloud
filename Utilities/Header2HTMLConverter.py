from pygments import highlight
from pygments.lexers.objective import ObjectiveCLexer as objcLexer
from pygments.formatters.html import HtmlFormatter


class Header2HTMLConverter:
    def __init__(self):
        pass

    def getHTMLString(self, filePath):
        with open(filePath, 'r') as f:
            hdr_content = f.read()
            return highlight(hdr_content, objcLexer(), HtmlFormatter())
