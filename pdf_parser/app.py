
from io import StringIO, BytesIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

output = BytesIO()

with open('/home/bazzan/Documents/TheStudyQuranANewTranslationAndCommentary.pdf', "rb") as fp:
    extract_text_to_fp(fp, output, laparams=LAParams(),
                       output_type='html')

data = output.getvalue().decode("utf-8", errors="ignore")
print(data)
