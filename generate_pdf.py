from flask import Flask
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

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdf.configuration(wkhtmltopdf=path_wkhtmltopdf)


# pdf.from_string("hello world", 'string.pdf')
# pdf.from_file('myhtmlfile.html', 'file.pdf')
# pdf.from_url('https://pypi.org/project/pdfkit/', 'url.pdf')

@app.route("/")
def index():
    # result = pdf.from_url("https://pypi.org/project/pdfkit/", "out.pdf", configuration=config)
    result = pdf.from_file('myhtmlfile.html', 'out.pdf',configuration=config)
    return result

if __name__ == "__main__":
    app.run(debug=True)