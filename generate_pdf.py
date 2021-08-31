from flask import Flask, render_template, make_response
import pdfkit as pdf



""" Generate pdf from html 
    MUST To download WKHTMLtoPDF to window from https://wkhtmltopdf.org/downloads.html  
    Steps:
    1. go to advanced enviroment setting, click enviroment variables tab 
    2. choose path in system variables window, click edit button below 
    3. now we need to install wkhtmltopdf installation path 
    4. go to c://program files//wkhtmltopdf//bin , then copy the path
    5. in the 'edit evnironment variables' window, choose 'new', add the path in the window, then click ok 
    6. There is an error to load the wkhtmltopdf path, so added config for pdfkit to find it
    """

app = Flask(__name__)
"""
   TO CONFIG THE PATH of WKHTMLTOPDF
"""
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdf.configuration(wkhtmltopdf=path_wkhtmltopdf)


# pdf.from_string("hello world", 'string.pdf')
# pdf.from_file('myhtmlfile.html', 'file.pdf')
# pdf.from_url('https://pypi.org/project/pdfkit/', 'url.pdf')

@app.route("/")
def index():
    # result = pdf.from_url("https://pypi.org/project/pdfkit/", "out.pdf", configuration=config)

    # Method ONE, turn the template into a string using render_template()
    # rendered = render_template('myhtmlfile.html')
    # pdf_content = pdf.from_string(rendered, False,configuration=config)

    # METHOD TWO: use html file directly
    pdf_content = pdf.from_file('templates/myhtmlfile.html', False, configuration=config)
    # IMPORTANT: instead of return a render_template, return a response, with a clarified header of 'Content-Type'
    response = make_response(pdf_content)
    response.headers['Content-Type'] = 'application/pdf'
     # if want to save the pdf result, use attachment, otherwise no need to have this line
    response.headers['Content-Disposition']= 'attachment; filename=output.pdf'
    return response

if __name__ == "__main__":
    app.run(debug=True)