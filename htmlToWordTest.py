# from htmldocx import HtmlToDocx

# new_parser = HtmlToDocx()
# new_parser.parse_html_file("example.html", "docx_filename")

from html2docx import html2docx

with open("./excels/acressexport.html") as fp:
    html = fp.read()

# html2docx() returns an io.BytesIO() object. The HTML must be valid.
buf = html2docx(html, title="My Document")

with open("my.docx", "wb") as fp:
    fp.write(buf.getvalue())