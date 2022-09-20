
import re

pattern = re.compile("position:absolute; border: textbox 1px solid; writing-mode:lr-tb; left:\d+px; top:\d+px; width:\d+px; height:\d+px;")

ans = pattern.fullmatch("position:absolute; border: textbox 1px solid; writing-mode:lr-tb; left:10px; top:20px; width:33px; height:444px;")

print(ans.group())
# print(help(ans))
