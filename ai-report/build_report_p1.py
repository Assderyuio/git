# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, "/home/user/git/ai-report")
from report_lib import *
import math

ASSETS = "/home/user/git/ai-report/assets/"
CHARTS = "/home/user/git/ai-report/charts/"
c = canvas.Canvas("/home/user/git/ai-report/AI_Report_2026.pdf", pagesize=A4)
c.setTitle("الذكاء الاصطناعي — Artificial Intelligence | بحث شامل 2026")
c.setAuthor("AI Research Desk")
c.setSubject("A comprehensive 20-page research report on Artificial Intelligence, bilingual Arabic/English")

TOTAL = 20

# ============ PAGE 1 — COVER ============
c.setFillColor(DEEP)
c.rect(0, 0, W, H, stroke=0, fill=1)
# hero image full height on the LEFT third (visual), text anchored RIGHT
img_w = W * 0.44
img_cover_crop(c, ASSETS + "cover_hero.jpg", 0, 0, img_w, H)
# soft gradient fade: overlay right edge of image into DEEP
for i, alpha in enumerate([0.06, 0.10, 0.16, 0.24, 0.34, 0.46, 0.60, 0.78, 1.0]):
    pass  # keep art pure; a gold hairline divides instead
c.setStrokeColor(GOLD); c.setLineWidth(2.2)
c.line(img_w, 60, img_w, H - 60)
c.setStrokeColor(GOLD2); c.setLineWidth(0.7)
c.line(img_w + 4, 90, img_w + 4, H - 90)

TX = W - M  # right anchor
# small brand mark top-right
c.setFillColor(TEAL)
c.roundRect(W - M - 34, H - 84, 34, 22, 4, stroke=0, fill=1)
letterspaced(c, W - M - 17, H - 77, "AI", font="Amiri-B", size=11.5, color=PAPER, tracking=1, align="center")
letterspaced(c, W - M - 42, H - 74, "R E S E A R C H   D E S K", font="Amiri-B", size=5.6, color=GOLD2, tracking=1.6, align="right")

letterspaced(c, TX, H - 128, "RESEARCH REPORT · NOVEMBER 2026", font="Amiri-B", size=6.8, color=GOLD2, tracking=2.6, align="right")
avail = TX - (img_w + 18)
tsize = 84
while tsize > 40:
    if ar_width("الاصطناعي", "Amiri-B", tsize) <= avail:
        break
    tsize -= 2
y1 = H - 208
y2 = y1 - tsize * 1.02
draw_ar(c, TX, y1, "الذكاء", font="Amiri-B", size=tsize, color=CREAM, align="right")
draw_ar(c, TX, y2, "الاصطناعي", font="Amiri-B", size=tsize, color=CREAM, align="right")
letterspaced(c, TX, y2 - 46, "A R T I F I C I A L   I N T E L L I G E N C E", font="Amiri-B", size=8.0, color=GOLD, tracking=1.9, align="right")
c.setStrokeColor(GOLD); c.setLineWidth(2.4)
c.line(TX, y2 - 58, TX - 96, y2 - 58)
draw_ar(c, TX, y2 - 84, "من اختبارِ تورينج إلى وكلاءِ الذكاءِ الاصطناعيّ،", font="Amiri", size=13, color=CREAM, align="right")
draw_ar(c, TX, y2 - 104, "رحلةٌ شاملة في أعمقِ تقنيةٍ تُعيد تشكيلَ الحضارة", font="Amiri", size=13, color=CREAM, align="right")
para_en(c, img_w + 26, y2 - 128, "A comprehensive, evidence-based research report on the technology rewriting humanity — Arabic & English.", font="Amiri-I", size=8.6, leading=13.5, max_w=W - img_w - 26 - M, color=HexColor("#9FB4C7"), align="right")

# meta stat row
meta_y = H - 545
col_w = (W - img_w - 26 - M) / 4
mx = img_w + 26
for i, (big, small_en, small_ar) in enumerate([("20", "PAGES", "صفحة"), ("15", "CHAPTERS", "فصلًا"), ("20+", "SOURCES", "مصدرًا"), ("AR/EN", "BILINGUAL", "ثنائي اللغة")]):
    xx = mx + i * col_w
    draw_ar(c, xx + col_w - 6, meta_y, big, font="Amiri-B", size=17 if i < 3 else 12.5, color=GOLD2, align="left")
    draw_ar(c, xx + col_w - 6, meta_y - 13, small_ar, font="Amiri", size=8.6, color=HexColor("#C7D3DE"), align="left")
    letterspaced(c, xx + col_w - 6, meta_y - 25, small_en, font="Amiri-B", size=5, color=GRAY, tracking=1.3, align="left")

# bottom block
c.setStrokeColor(HexColor("#274361")); c.setLineWidth(1)
c.line(img_w + 26, 118, W - M, 118)
draw_ar(c, TX, 96, "الإصدارُ الأوّل · نوفمبر ٢٠٢٦", font="Amiri-B", size=12, color=GOLD2, align="right")
draw_ar(c, TX, 76, "إعدادُ: AI Research Desk — وحدةُ أبحاثِ الذكاءِ الاصطناعيّ", font="Amiri", size=9.5, color=HexColor("#C7D3DE"), align="right")
draw_ar(c, TX, 58, "صيغَ هذا التقريرُ بالتعاونِ مع نماذجِ الذكاءِ الاصطناعيّ ومراجعةٍ تحريريةٍ بشرية", font="Amiri-I", size=7.6, color=HexColor("#7E93A8"), align="right")
# vertical spine text on image
c.saveState()
c.translate(26, H / 2)
c.rotate(90)
letterspaced(c, 0, 0, "ARTIFICIAL INTELLIGENCE — A COMPREHENSIVE RESEARCH REPORT — 2026", font="Amiri-B", size=7, color=HexColor("#5E7A93"), tracking=3.2, align="center")
c.restoreState()
c.showPage()

# ============ PAGE 2 — EXECUTIVE SUMMARY ============
chrome(c, 2, TOTAL)
y = H - 78
letterspaced(c, W - M, y, "FRONT MATTER", font="Amiri-B", size=6.6, color=TEAL, tracking=3, align="right")
y -= 8
draw_ar(c, W - M, y - 26, "الملخّص التنفيذي", font="Amiri-B", size=30, color=NAVY, align="right")
letterspaced(c, M, y - 24, "E X E C U T I V E   S U M M A R Y", font="Amiri-B", size=8, color=GRAY, tracking=1.6, align="left")
c.setStrokeColor(GOLD); c.setLineWidth(2.4); c.line(W - M, y - 46, W - M - 90, y - 46)
y -= 66

y = para_ar(c, M, y, "يقفُ العالمُ في عامِ ٢٠٢٦ أمامَ لحظةٍ فاصلةٍ في تاريخِه: الذكاءُ الاصطناعيّ لم يعد تجربةً مخبريةً أو وعودَ مؤتمرات، بل أصبحَ بنيةً تحتيةً اقتصاديةً تقرأ عبرَها الشركاتُ بياناتِها، وتُشخّصُ المستشفياتُ بها المرضى، وتكتبُ الحواسيبُ بها الشيفرةَ، وتُعيدُ الحكوماتُ — ومنها مصر — رسم استراتيجياتِها حولَها. خلال ثلاث سنوات فقط تجاوز تبنّي الذكاء الاصطناعي التوليدي تبنّي الإنترنت والحاسوب الشخصي معًا.", font="Amiri", size=11, leading=20, color=INK)
y -= 6
y = para_ar(c, M, y, "يجمعُ هذا التقريرُ أحدثَ بياناتِ المؤسساتِ البحثية العالمية — من ستانفورد إلى McKinsey وWEF وIMF وPwC وOxford Insights — ويقدّمها بلغةٍ عربيةٍ رصينة مع مصطلحاتِها الإنجليزية، في عشرين صفحةً تغطّي: التعريف، التاريخ، آلية العمل، الأرقام، القطاعات — من الطبّ إلى القاهرة الجديدة — الفرص، المخاطر، الحوكمة، الوظائف، وخارطةَ طريقٍ عملية للبدء خلال ٩٠ يومًا.", font="Amiri", size=10, leading=18, color=INK)
y -= 14

letterspaced(c, W - M, y, "THE REPORT IN NUMBERS", font="Amiri-B", size=7, color=TEAL, tracking=1.6, align="right")
draw_ar(c, W - M, y - 12, "التقريرُ في أرقام", font="Amiri-B", size=9, color=GRAY, align="right")
y -= 18
card_h, gap = 84, 10
cw = (CW - 3 * gap) / 4
cards = [
    ("88%", "من المؤسسات تستخدم الذكاء الاصطناعي فعليًا", "ORG ADOPTION 2026", TEAL),
    ("$581.7B", "استثمار الشركات العالمية في AI خلال 2025", "CORP. INVESTMENT ×2", NAVY),
    ("$15.7T", "مساهمة AI المتوقعة في الناتج العالمي 2030", "PwC — SIZING THE PRIZE", GOLD),
    ("+78M", "وظيفة صافي إضافية عالميًا بحلول 2030", "WEF FUTURE OF JOBS", RED),
]
for i, (big, lab, sub, col) in enumerate(cards):
    stat_card(c, M + i * (cw + gap), y, cw, card_h, big, lab, sub, big_color=col)
y -= card_h + 16

# five-axis map strip
axes = [("١", "الفهم", "UNDERSTAND"), ("٢", "الأرقام", "MEASURE"), ("٣", "التطبيق", "APPLY"), ("٤", "الحوكمة", "GOVERN"), ("٥", "الانطلاق", "LAUNCH")]
ax_w = (CW - 4 * 26) / 5
ax_y = y
for i, (n, a, e) in enumerate(axes):
    x0 = W - M - (i + 1) * ax_w - i * 26
    c.setFillColor(NAVY2)
    c.roundRect(x0, ax_y - 34, ax_w, 34, 6, stroke=0, fill=1)
    draw_ar(c, x0 + ax_w - 8, ax_y - 13, n, font="Amiri-B", size=10, color=GOLD2, align="right")
    draw_ar(c, x0 + ax_w / 2, ax_y - 14, a, font="Amiri-B", size=9.5, color=PAPER, align="center")
    letterspaced(c, x0 + ax_w / 2, ax_y - 27, e, font="Amiri-B", size=4.6, color=TEAL2, tracking=1.5, align="center")
    if i < 4:
        draw_ar(c, x0 - 13, ax_y - 20, "›", font="Amiri-B", size=15, color=GOLD, align="center")
y = y - 46

# how-to-read audience row
aud = [("كطالب", "ابدأ بالفصول ١–٥ ومسرد المصطلحات (ص١٩)، ثم نفّذ مشروعك بمساعدة AI"), ("كمهني", "اقفز إلى الفصلين ١٢ و١٣: أداة لكل مهمة، وأتمتة حقيقية هذا الأسبوع"), ("كرائد أعمال", "اقرأ الفصول ٧–٩: أين السوق فعلًا؟ وأين تفشل ٨٠٪ من المشاريع؟")]
au_w = (CW - 16) / 3
for i, (t, d) in enumerate(aud):
    x0 = M + (2 - i) * (au_w + 8)   # RTL: first on the right
    note_box(c, x0, y, au_w, 54, fill=CREAM, stroke=LINE, radius=6)
    draw_ar(c, x0 + au_w - 10, y - 12, t, font="Amiri-B", size=9, color=TEAL, align="right")
    para_ar(c, x0 + 8, y - 16, d, font="Amiri", size=7.0, leading=10, max_w=au_w - 16, color=INK)
y = y - 66

note_box(c, M, y, CW, 128, fill=NAVY, stroke=NAVY, radius=8)
letterspaced(c, W - M - 18, y - 16, "IN ENGLISH — THE REPORT IN 60 SECONDS", font="Amiri-B", size=7.2, color=GOLD2, tracking=1.4, align="right")
en_lines = [
    "• AI is no longer a lab experiment — 88% of organizations use it, and GenAI reached 53% population adoption faster than the PC or the internet.",
    "• The prize: up to $15.7T added to global GDP by 2030 (PwC) and $2.6–4.4T per year from generative AI alone (McKinsey).",
    "• The catch: biased models, hallucinations, privacy leaks, deepfakes — and a 50-point trust gap between experts (73%) and the public (23%).",
    "• For Egypt & the Arab world: #1 in Africa's Government AI Readiness (Oxford Insights), a market set to grow ~5× to $5.1B by 2031.",
    "• What to do: read Chapters 9–12 — risks, governance, jobs, and a 90-day roadmap to start safely, today.",
]
yy = y - 33
for ln in en_lines:
    yy = para_en(c, M + 16, yy, ln, font="Amiri", size=7.7, leading=12.4, max_w=CW - 32, color=HexColor("#DCE6EE"))
y -= 128 + 16
# closing quote strip
c.setFillColor(GOLD)
c.rect(M, y - 30, 4, 30, stroke=0, fill=1)
draw_ar(c, W - M - 14, y - 12, "«الذكاءُ الاصطناعيّ لم يعُد تكنولوجيا المستقبل؛", font="Amiri-BI", size=14, color=NAVY, align="right")
draw_ar(c, W - M - 14, y - 30, "إنه كهرباءُ العصرِ الجديد»", font="Amiri-BI", size=14, color=NAVY, align="right")
c.showPage()

# ============ PAGE 3 — TABLE OF CONTENTS ============
chrome(c, 3, TOTAL)
y = H - 78
letterspaced(c, W - M, y, "TABLE OF CONTENTS", font="Amiri-B", size=7, color=TEAL, tracking=2.4, align="right")
draw_ar(c, W - M, y - 10, "المحتويات", font="Amiri-B", size=9, color=GRAY, align="right")
y -= 8
draw_ar(c, W - M, y - 26, "فهرسُ البحث", font="Amiri-B", size=28, color=NAVY, align="right")
c.setStrokeColor(GOLD); c.setLineWidth(2.4); c.line(W - M, y - 44, W - M - 74, y - 44)
y -= 62

toc = [
    ("٠١", "مقدمة: ما هو الذكاء الاصطناعي؟", "INTRODUCTION", 4),
    ("٠٢", "مسيرة ٧٥ عامًا: من تورينج إلى اليوم", "A 75-YEAR JOURNEY", 5),
    ("٠٣", "كيف يعمل الذكاء الاصطناعي؟", "UNDER THE HOOD", 6),
    ("٠٤", "الذكاء الاصطناعي بالأرقام", "AI BY THE NUMBERS", 7),
    ("٠٥", "الثورة التوليدية والنماذج اللغوية", "THE GENAI REVOLUTION", 9),
    ("٠٦", "الذكاء الاصطناعي في القطاعات", "AI ACROSS INDUSTRIES", 10),
    ("٠٧", "مصر والعالم العربي: المعركة الصاعدة", "EGYPT & THE ARAB WORLD", 11),
    ("٠٨", "الفوائد والقيمة الاقتصادية", "BENEFITS & THE VALUE AT STAKE", 12),
    ("٠٩", "المخاطر والتحديات السبعة", "SEVEN RISKS & CHALLENGES", 13),
    ("١٠", "الأخلاق والحوكمة: AI Act وما بعده", "ETHICS & GOVERNANCE", 14),
    ("١١", "الوظائف والمهارات: من يُؤتمت؟", "JOBS & SKILLS", 15),
    ("١٢", "خارطة طريق ٩٠ يومًا للبدء", "YOUR 90-DAY ROADMAP", 16),
    ("١٣", "حالات نجاح: حين يعمل AI فعلًا", "SUCCESS STORIES", 17),
    ("١٤", "المستقبل ٢٠٢٦–٢٠٣٥: عصر الوكلاء", "THE ROAD AHEAD — THE AGENTIC AGE", 18),
    ("١٥", "أسئلة شائعة + مسرد المصطلحات", "FAQ & GLOSSARY", 19),
    ("◆", "الخاتمة والمراجع والمصادر", "CONCLUSION & REFERENCES", 20),
]
col_w2 = (CW - 26) / 2
row_h = 41
start_y = y
for i, (num, ar_t, en_t, page) in enumerate(toc):
    col = 0 if i < 8 else 1
    row = i if i < 8 else i - 8
    cx0 = M + (CW - col_w2) if col == 0 else M
    cy = start_y - row * row_h
    if num == "◆":
        diamond(c, cx0 + col_w2 - 7, cy - 6, 7, GOLD)
    else:
        draw_ar(c, cx0 + col_w2, cy - 11, num, font="Amiri-B", size=15, color=GOLD, align="right")
    title_anchor = cx0 + col_w2 - 27
    tw = ar_width(ar_t, "Amiri-B", 9.6)
    draw_ar(c, title_anchor, cy - 10.5, ar_t, font="Amiri-B", size=9.6, color=NAVY, align="right")
    letterspaced(c, title_anchor, cy - 21.5, en_t, font="Amiri-B", size=4.3, color=GRAY, tracking=0.8, align="right")
    draw_ar(c, cx0, cy - 10.5, str(page), font="Amiri-B", size=11.5, color=TEAL, align="left")
    dots_x0 = cx0 + 15
    dots_x1 = title_anchor - tw - 10
    if dots_x1 > dots_x0:
        c.setFillColor(HexColor("#B9C6D2"))
        dx = dots_x0
        while dx < dots_x1:
            c.circle(dx, cy - 13.2, 0.6, stroke=0, fill=1)
            dx += 5.4

y = start_y - 8 * row_h - 6
note_box(c, M, y, CW, 108, fill=CREAM, stroke=LINE, radius=6)
draw_ar(c, W - M - 12, y - 16, "عن هذا التقرير وكيف تقرأه", font="Amiri-B", size=10.5, color=NAVY, align="right")
about = [
    "المنهجية — جمعٌ وتحليلٌ لأحدث التقارير الدولية (Stanford AI Index 2026 · GVR · MarketsandMarkets · McKinsey · WEF · IMF · PwC · Oxford Insights) ومصادر عربية موثوقة، حتى 16 نوفمبر 2026.",
    "النطاق — بحثٌ موجّه للقارئ العام والمهني والطالب؛ علمي في مصادره، عملي في توصياته، ولا يفترض خلفية تقنية.",
    "تنبيه مهم — تقديرات السوق تتباين بين المؤسسات باختلاف المنهجية؛ لذا نذكر المصدر بجانب كل رقم بدلًا من المتوسط المضلل.",
    "علامات — [n] مرجعٌ في قائمة المصادر (ص٢٠) · المربعات الملونة أرقامٌ مفصلية · M/F = مليون/مليار.",
]
yy = y - 33
for b in about:
    diamond(c, W - M - 14, yy - 4, 2.2, GOLD)
    yy = para_ar(c, M + 12, yy, b, font="Amiri", size=8.0, leading=13, max_w=CW - 34, color=INK)
    yy -= 3
# decorative art strip to close the contents page
img_cover_crop(c, ASSETS + "cover_hero.jpg", M, 64, CW, 88, radius=8)
c.setFillColor(Color(0.03, 0.08, 0.15, alpha=0.45)); c.roundRect(M, 64, CW, 88, 8, stroke=0, fill=1)
draw_ar(c, W - M - 14, 118, "كل ما تحتاج معرفته عن الذكاء الاصطناعي", font="Amiri-B", size=12, color=PAPER, align="right")
letterspaced(c, M + 14, 76, "AI RESEARCH REPORT · 2026 · 20 PAGES", font="Amiri-B", size=6, color=TEAL2, tracking=1.8, align="left")
c.showPage()
