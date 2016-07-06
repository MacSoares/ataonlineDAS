"""Module of PDF converter."""
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template


class PdfConverter:
    """Class to convert html page to a pdf file."""

    def convert(self, page, output, data):
        """Function to convert."""
        target = get_template(page)
        html = target.render(Context(data))

        file = open(output, "w+b")
        pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8')

        file.seek(0)
        pdf = file.read()
        file.close()
        return HttpResponse(pdf, 'application/pdf')
