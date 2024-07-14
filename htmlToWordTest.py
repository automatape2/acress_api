from htmldocx import HtmlToDocx

new_parser = HtmlToDocx()
new_parser.parse_html_file("example.html", "docx_filename")
#Files extensions not needed, but tolerated
