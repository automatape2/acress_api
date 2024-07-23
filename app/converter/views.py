from django.http import JsonResponse
from django.shortcuts import render
from html2docx import html2docx
from django.conf import settings
import os
import io   
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        html_file = request.FILES['html_file']
        html_content = html_file.read().decode('utf-8')
        
        # Convertir HTML a DOCX
        docx_stream = io.BytesIO()
        html2docx(html_content, docx_stream)
        docx_stream.seek(0)

        response = HttpResponse(docx_stream.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename="output.docx"'
        return response
    # if request.method == 'POST':
    #     request_file = request.FILES.get('file')
        
    #     filepath = os.path.join(settings.MEDIA_ROOT, 'uploads', request_file.name)
    #     with open("./excels/acressexport.html") as fp:
    #         html = fp.read()

    #     # html2docx() returns an io.BytesIO() object. The HTML must be valid.
    #     buf = html2docx(html, title="My Document")

    #     with open("my.docx", "wb") as fp:
    #         fp.write(buf.getvalue())
    
 
    
