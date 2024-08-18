from django.http import JsonResponse
from django.shortcuts import render
from html2docx import html2docx
from django.conf import settings
import os
import io   
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        
        html = (request.FILES['html_file']).read().decode('utf-8')

        # with open("my.docx", "wb") as fp:
        #     fp.write(
        #         buffer = html2docx(content = html).getvalue()
        #     )

        docx_stream = io.BytesIO()

        html2docx(html, docx_stream)
        docx_stream.seek(0)

        response = HttpResponse(
            content = docx_stream.read(), 
            content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        
        response['Content-Disposition'] = 'attachment; filename="output.docx"'
        return response
    
 
    
