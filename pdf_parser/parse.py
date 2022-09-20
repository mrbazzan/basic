
import re
from bs4 import BeautifulSoup

with open("pdf_parser/app.html", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, "html.parser")

    div_style = soup("div", {"style": re.compile("position:absolute; border: textbox 1px solid; writing-mode:lr-tb; left:\d+px; top:\d+px; width:\d+px; height:\d+px;")})
    
    for i, item in enumerate(div_style):

        span_beginning_title = item.find("span", {"style": "font-family: LiberationSerif; font-size:23px"})
        if span_beginning_title:
            print(f"\n\n\n\n====CHAPTER {span_beginning_title.text}")
        span_number = item("span", {"style": "font-family: GaramondPremrPro; font-size:14px"})
        if not span_number:
            continue

        last_number = int(span_number[-1].text.strip()) + 1
        for number, span_ in enumerate(span_number): # [145] [131, 32] [1,3] [10,11]

            _begin = ""
            first_number = span_number[0].text
            if len(first_number) > 2:
                _begin = first_number[0]
            
            if number == 0:
                print(span_.text)
            else:
                print(_begin + span_.text)
            # count = 0
            # while not span_.text.strip().endswith(str(last_number-count)):
            #     print( int(span_.text.strip()) + count )
            #     texty=''

            #     if count == 0:
            #         if len(span_number) > 1:
            #             if len(span_.text.strip()) == 3:
            #                 count = last_number - 1 - int(span_.text.strip()[len(str(last_number))-1:])
            #             else:
            #                 count = last_number - 1 - int(span_.text.strip())
            #     else:
            #         count = count - 1
            #     # elif count == 1:
            #     #     count = 0

            #     required_content = div_style[i-(count+1)].strings

            #     for num, x in enumerate(required_content):
            #         if num == 0 and len(x) == 1:
            #             # print(len(x), end="\n\n")
            #             continue
            #         texty += x.strip() + " "
            #     print(texty, end="\n\n")

            #     if len(span_number) == 1:
            #         count += 1
            #         continue

            #     if count == 0:
            #         break
            # break

            # print(div_style[i-(number+1)].prettify())
            texty=''
            for num, x in enumerate(div_style[i-(number+1)].strings):
                if num == 0 and len(x) == 1:
                    continue
                texty += x.strip() + " "
            print(texty, end="\n\n")
            # print(div_style[i-(number+1)].decode())
            
            # span_weird_missing = div_style[i-(number+1)]("span", {"style":"font-family: HCSQ-It; font-size:20px"})
            # span_missing = div_style[i-(number+1)]("span", attrs={"style": "font-family: LiberationSerif-Italic; font-size:20px"})
            # span_style = div_style[i-(number+1)]("span", {"style":"font-family: LiberationSerif; font-size:20px"})
            # text = ""
            # for line in span_weird_missing:
            #     text += line.text.strip()
            # for line in span_missing:
            #     text += line.text.strip() + " "
            # for line in span_style:
            #     text += line.text.strip()

            # print(text, end="\n\n")

