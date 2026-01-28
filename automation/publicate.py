import csv
import random
from datetime import date

CSV_FILE = "C:\\Users\\jcorn\\OneDrive\\Desktop\\Analytics\\automation\\quotes.csv"
OUTPUT_HTML = "C:\\Users\\jcorn\\OneDrive\\Documents\\personal_website\\Portfolio\\quote.html"

quotes = []

with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f) # read each row as a dictionary instead of a list. 
    quotes = list(reader)

#read the quotes

unused = [q for q in quotes if q["used"] == "false"]
# for unused 
if not unused:
    raise Exception("No unused quotes left")


quote = random.choice(unused)
quote["used"] = "true"

# Update CSV
with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=quotes[0].keys())
    writer.writeheader()
    writer.writerows(quotes)

today = date.today()
a = str(today)
month = a[6:7]
day = a[8:10]
# Update HTML
html = f"""
<br>
<p>
{month}.{day} "{quote['text']}" - {quote['author']} <p class = "quote-highlight1"> (automation) 
</p>  
"""


with open(OUTPUT_HTML,  encoding="utf-8") as f:
    html1 = f.read()
    html1 = html1.replace("</body>", html + "</body>")
with open(OUTPUT_HTML, "w", encoding="utf-8") as f:    
    f.write(html1)

print("Quote published:", quote["text"])
