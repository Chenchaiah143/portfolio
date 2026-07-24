import base64, os

# Full portfolio HTML encoded to avoid shell quoting issues
html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Thatha Chenchaiah | VLSI Aspirant &amp; Automation Tester</title>
<meta name="description" content="Portfolio of Thatha Chenchaiah - B.Tech ECE student specializing in VLSI design and Selenium automation testing."/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet"/>
</head>
<body>
<h1>PLACEHOLDER - SCRIPT WORKS</h1>
</body>
</html>"""

path = r"C:\Users\THATHA CHENCHAIAH\.gemini\antigravity\scratch\portfolio\index.html"
with open(path,"w",encoding="utf-8") as f:
    f.write(html)
print("Written:", len(html), "chars")
