# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, "/home/user/git/ai-report")
from report_lib import *
import math
ASSETS = "/home/user/git/ai-report/assets/"
CHARTS = "/home/user/git/ai-report/charts/"

# ============ PAGE 11 — CH.07 EGYPT & ARAB WORLD ============
chrome(c, 11, TOTAL)
y = section_banner(c, "٠٧", "مصرُ والعالم العربي: المعركة الصاعدة", "CHAPTER 07 — EGYPT & THE ARAB WORLD")
img_cover_crop(c, ASSETS + "egypt_ai.jpg", M, y - 132, CW, 132, radius=8)
c.setFillColor(Color(0.04, 0.09, 0.16, alpha=0.42)); c.roundRect(M, y - 132, CW, 132, 8, stroke=0, fill=1)
draw_ar(c, W - M - 14, y - 26, "القاهرة — حيث تلتقي الأهراماتُ بالخوارزميات", font="Amiri-B", size=12.5, color=PAPER, align="right")
para_en(c, M + 12, y - 122, "Cairo positioning itself as the regional AI capital of the Middle East & Africa — 2026.", font="Amiri-I", size=7, color=HexColor("#E8EEF3"))
y = y - 146

half = (CW - 12) / 2
note_box(c, M + half + 12, y, half, 218, fill=TEALPALE, stroke=TEAL2, radius=6)
draw_ar(c, W - M - 12, y - 16, "لماذا مصرُ مُهيأةٌ لتقود المنطقة؟", font="Amiri-B", size=10.5, color=TEAL, align="right")
egypt_facts = [
    ("#1 في أفريقيا — مؤشر أكسفورد لجاهزية الحكومة للذكاء الاصطناعي: نضجٌ في السياسات والمهارات والقطاع العام [10]", "#1"),
    ("السوق المصرية اليوم ~$1B، وتصل إلى $5.1B بحلول 2031 — نمو 5× خلال 5 سنوات [11]", "5×"),
    ("750 ألف خريج جامعي سنويًا — أكبر وقود مواهب في أفريقيا والشرق الأوسط [18]", "750 ألف"),
    ("صادرات رقمية مستهدفة $8B بنهاية 2026 — التعهيد يذهب حيث الكفاءات [19]", "$8B"),
    ("الاستراتيجية الوطنية الثانية للذكاء الاصطناعي — صناعة محلية مستدامة بلا تبعية [17]", "AI 2.0"),
]
fx = M + half + 12 + 6
table_ar(c, fx, y - 26, [half - 12 - 58, 58], egypt_facts, header_rows=0, size=6.8, pad=4.5, zebra=True)

note_box(c, M, y, half, 218, fill=PAPER, stroke=LINE, radius=6)
draw_ar(c, M + half - 12, y - 15, "التحديات الصريحة — لا نملك رفاهية تجاهلها", font="Amiri-B", size=10.5, color=RED, align="right")
challenges = [
    ("فجوة المحتوى العربي", "البيانات العربية أقل من 1% من بيانات التدريب العالمية — لهجةٌ فصحى تتعدد ألوانها وتُهمل"),
    ("فجوة المواهب", "الطلب على مهندسي ML يفوق المعروض بمضاعفات — والرواتب تسحب الكفاءات للخارج"),
    ("السيادة والحوسبة", "مراكز بيانات إقليمية وحوسبة سيادية شرطٌ للاستقلال الرقمي (الاستثمارات ترتفع في القاهرة)"),
    ("التنظيم", "إطار تشريعي يتواكب مع السرعة — بين الحماية المفرطة وخنق الابتكار"),
]
my = y - 33
for t, d in challenges:
    draw_ar(c, M + half - 12, my, t, font="Amiri-B", size=8.6, color=NAVY, align="right")
    my = para_ar(c, M + 12, my - 13, d, font="Amiri", size=7.2, leading=10.2, max_w=half - 24, color=INK)
    my -= 5.5
y = y - 232

draw_ar(c, W - M, y, "فرصةُ الجيلِ العربي — THE OPPORTUNITY", font="Amiri-B", size=9.5, color=TEAL, align="right")
y -= 8
op_chips = [
    "بناء نماذج عربية وتقييمها (Arabic LLMs)",
    "RAG ومساعدون للمؤسسات بالعربية",
    "وكلاء AI للحكومة والصحة والتعليم",
    "هندسة بيانات + ضبط دقيق (Fine-tuning)",
    "منتجات AI للسوق المحلي قبل العالمي",
]
py = y
for i, t in enumerate(op_chips):
    tw_ = ar_width(t, "Amiri-B", 8) + 22
    xx = W - M - tw_
    # wrap to next line manually: measure cumulative — keep single line each, right aligned stack
    c.setFillColor(GOLDPALE); c.setStrokeColor(GOLD); c.setLineWidth(0.9)
    c.roundRect(xx, py - 15, tw_, 19, 9.5, stroke=1, fill=1)
    diamond(c, xx + 10, py - 5.5, 2, GOLD)
    draw_ar(c, xx + tw_ - 8, py - 10.5, t, font="Amiri-B", size=8, color=NAVY, align="right")
    py -= 25
note_box(c, M, y, 218, 128, fill=NAVY, stroke=NAVY, radius=8)
draw_ar(c, M + 218 - 12, y - 15, "أرقامُ المنطقة", font="Amiri-B", size=9.5, color=GOLD2, align="right")
reg_stats = [
    "$30.87B — سوق AI والأمن السيبراني والبيانات في MEA خلال 2026، ونمو 19.85% سنويًا حتى 2031 [12]",
    "$1.5T — مساهمة AI المحتملة في الناتج الأفريقي بنهاية العقد (UNDP) [18]",
    "2026 — AI Everything MEA Egypt: القاهرة تستضيف أكبر منصة ذكاء اصطناعي في المنطقة [18]",
]
my = y - 34
for txt in reg_stats:
    my = para_ar(c, M + 10, my, txt, font="Amiri", size=6.7, leading=10, max_w=218 - 20, color=HexColor("#DCE6EE"))
    my -= 4
note_box(c, M, y - 132, CW, 44, fill=GOLDPALE, stroke=GOLD2)
draw_ar(c, W - M - 12, y - 149, "حصة الشرق الأوسط من الناتج العالمي لن تتجاوز 2% بحلول 2030، بينما يربح العالم 14% —", font="Amiri-B", size=8.8, color=RED, align="right")
draw_ar(c, W - M - 12, y - 164, "الفارق ليس الحظ: إنه صناعةُ القرار الرقمي اليوم [6][17]", font="Amiri-B", size=8.8, color=NAVY, align="right")
c.showPage()

# ============ PAGE 12 — CH.08 BENEFITS & VALUE ============
chrome(c, 12, TOTAL)
y = section_banner(c, "٠٨", "الفوائد: ما الذي نشتريه بالفعل؟", "CHAPTER 08 — THE VALUE AT STAKE")
card_h, gap = 92, 12
cw = (CW - 2 * gap) / 3
big_cards = [
    ("$15.7T", "مساهمة AI المتوقعة في الناتج العالمي بحلول 2030 — ~14% من الناتج — PwC", "PWC + استراتيجية مصر 2.0 [6][17]", GOLD),
    ("$2.6–4.4T", "قيمة سنوية من الذكاء التوليدي عبر 63 استخدامًا في 16 وظيفة — McKinsey", "MCKINSEY GLOBAL INSTITUTE [7]", TEAL),
    ("+78M", "وظيفة صافي إضافية بحلول 2030 (170 تُخلق · 92 تُزاح) — WEF", "WEF FUTURE OF JOBS 2025 [8]", NAVY),
]
for i, (big, lab, sub, col) in enumerate(big_cards):
    x0 = M + i * (cw + gap)
    note_box(c, x0, y, cw, card_h, fill=PAPER, stroke=LINE)
    c.setFillColor(col); c.rect(x0, y - card_h, 4, card_h, stroke=0, fill=1)
    draw_ar(c, x0 + cw / 2, y - 26, big, font="Amiri-B", size=21 if len(big) <= 8 else 17, color=col, align="center")
    para_ar(c, x0 + 10, y - 38, lab, font="Amiri", size=7.3, leading=10.5, max_w=cw - 20, color=INK)
    letterspaced(c, x0 + cw / 2, y - card_h + 8, sub, font="Amiri-B", size=4.4, color=GRAY, tracking=0.7, align="center")
y = y - card_h - 12

c.drawImage(CHARTS + "chart_jobs.png", M, y - 175, width=CW, height=175, preserveAspectRatio=False)
para_en(c, M, y - 180, "Fig. 3 — WEF Future of Jobs 2025: 170M new roles vs 92M displaced; net +78M; 22% of the formal-jobs base churns. [8]", font="Amiri-I", size=6.6, color=GRAY)
y = y - 198

half = (CW - 12) / 2
draw_ar(c, W - M, y, "من أين تأتي القيمة؟ أربعةُ محركات", font="Amiri-B", size=11.5, color=TEAL, align="right")
y -= 8
engines = [
    ("أتمتة ٦٠ إلى ٧٠٪", "من وقت الموظف قابلٌ للأتمتة تقنيًا — MGI"),
    ("قرارٌ أسرع", "تحليل ملايين السجلات في ثوانٍ لا أسابيع"),
    ("تخصيص 1:1", "كل عميل يُدار كشركةٍ قائمةٍ بذاتها"),
    ("ابتكار ×10", "تجربة الفرضيات أقصر بعشر مرات في R&D"),
]
for i, (t, d) in enumerate(engines):
    ry = y - i * 21
    draw_ar(c, W - M, ry - 4, t, font="Amiri-B", size=9, color=NAVY, align="right")
    bw = ar_width(t, "Amiri-B", 9)
    para_ar(c, M, ry - 4, d, font="Amiri", size=8.2, leading=12, max_w=CW - bw - 30, color=GRAY)

note_box(c, M, y - 96, CW, 76, fill=TEALPALE, stroke=TEAL2)
draw_ar(c, W - M - 12, y - 110, "الواقعية أولًا — العائد على الاستثمار ليس مضمونًا", font="Amiri-B", size=10, color=TEAL, align="right")
roi_items = [("19%", "رفعت إيراداتها أكثر من 5%"), ("36%", "لم ترَ تغييرًا في الإيرادات"), ("23%", "تحسّن واضح في التكاليف"), ("87%", "تتوقع نموًا خلال 3 سنوات")]
rx = M + CW - 12
for i, (big, lab) in enumerate(roi_items):
    xx = M + 14 + i * ((CW - 28) / 4)
    draw_ar(c, xx + (CW - 28) / 8, y - 130, big, font="Amiri-B", size=16, color=NAVY, align="center")
    para_ar(c, xx + (CW - 28) / 8, y - 141, lab, font="Amiri", size=7, leading=10.5, max_w=(CW - 28) / 4, color=INK, align="center")
draw_ar(c, W - M - 12, y - 166, "— استطلاع McKinsey/MGI للتنفيذيين [16]", font="Amiri-I", size=6.5, color=GRAY, align="right")

half = (CW - 12) / 2
y2 = y - 210
note_box(c, M + half + 12, y2, half, 108, fill=CREAM, stroke=LINE)
draw_ar(c, W - M - 12, y2 - 14, "أين يفشل AI؟ ثلاثةُ أسباب متكررة", font="Amiri-B", size=9.5, color=RED, align="right")
fail = ["لا مشكلة محددة — «AI نبحث عن مشكلة له» بدلًا من حلّ مسألة قابلة للقياس", "بيانات سيئة لا يعرفها أحد — الفشل الصامت في التدريب", "تبنّي ضعيف: الفريق لم يُدرَّب ولا يثق حتى بأفضل النتائج"]
fy = y2 - 34
for i, t in enumerate(fail):
    draw_ar(c, W - M - 12, fy, f"٠{i+1}", font="Amiri-B", size=8.5, color=RED, align="right")
    fy = para_ar(c, M + half + 12 + 8, fy, t, font="Amiri", size=7.4, leading=11.5, max_w=half - 44, color=INK)
    fy -= 4
note_box(c, M, y2, half, 108, fill=TEALPALE, stroke=TEAL2)
draw_ar(c, M + half - 12, y2 - 14, "أين ينجح؟ الوصفة المجربة", font="Amiri-B", size=9.5, color=TEAL, align="right")
win = ["هدف واحد قابل للقياس بعد ٩٠ يومًا — ليس «نحو AI الشامل»", "بيانات نظيفة + إنسان مسؤول عن جودتها وصيانتها", "تبنّي تدريجي مع مراجعة بشرية لكل قرار حرج"]
wy = y2 - 34
for i, t in enumerate(win):
    diamond(c, M + half - 16, wy - 3.5, 2.2, TEAL)
    wy = para_ar(c, M + 10, wy, t, font="Amiri", size=7.4, leading=11.5, max_w=half - 22, color=INK)
    wy -= 4
c.showPage()

# ============ PAGE 13 — CH.09 RISKS ============
chrome(c, 13, TOTAL)
y = section_banner(c, "٠٩", "المخاطر والتحديات السبعة", "CHAPTER 09 — SEVEN RISKS YOU MUST MANAGE")
risk_rows = [
    ["الخطر", "ماذا يحدث", "الحدّة", "المعالجة"],
    ["التحيز الخوارزمي", "قرارات ظالمة ضد فئات سكانية معينة", "عالية", "بيانات متوازنة + تدقيق دوري للعدالة"],
    ["الهلوسة", "النموذج يخترع حقائق بثقةٍ كاملة", "عالية", "تحقق بشري + RAG بمصادر موثقة"],
    ["تسرب الخصوصية", "بيانات حساسة تتسلل إلى التدريب والأوامر", "عالية", "حوكمة بيانات + نماذج محلية معزولة"],
    ["التزييف العميق", "انتحال الصوت والصورة والفيديو باحتراف", "عالية", "توثيق رقمي + تشريعات ولوائح"],
    ["إزاحة الوظائف المبتدئة", "تراجع توظيف المطورين 22–25 عامًا بنحو 20% منذ 2024 [4]", "متوسطة+", "إعادة تأهيل + مسارات تدريبية"],
    ["الأمن و«تسميم» النماذج", "حقن بيانات خبيثة في التدريب والاستدلال", "متوسطة", "اختبار اختراق للنماذج + مراقبة"],
    ["فجوة الثقة العامة", "٧٣٪ من الخبراء متفائلون مقابل ٢٣٪ فقط من الجمهور [4]", "متوسطة", "شفافية + تواصل مسؤول"],
]
col_ws = [CW * 0.21, CW * 0.335, CW * 0.105, CW * 0.34]
y = table_ar(c, M, y, col_ws, risk_rows, header_rows=1, size=8.0, pad=5.5)
y -= 8
draw_ar(c, W - M, y, "الحدة: عالية = تتطلب حوكمةً فورية · متوسطة = تتطلب خطةً ورقابة", font="Amiri-I", size=7, color=GRAY, align="right")
y -= 12

c.drawImage(CHARTS + "chart_invest.png", M, y - 92, width=CW, height=92, preserveAspectRatio=False)
para_en(c, M, y - 97, "Fig. 4 — The investment race is uneven: US private AI funding ($285.9B) dwarfs China ($12.4B) 23× in 2025. [4]", font="Amiri-I", size=6.6, color=GRAY)
y = y - 108

note_box(c, M, y, CW, 92, fill=CREAM, stroke=LINE)
draw_ar(c, W - M - 12, y - 15, "ثلاثةُ مبادئ للتعامل مع أي نظام AI في مؤسستك", font="Amiri-B", size=9.5, color=TEAL, align="right")
rules = [
    ("ثق ثم تحقق", "كل مخرجٍ ذكاءٍ اصطناعي مسودة — القرار البشري هو النسخة النهائية دائمًا"),
    ("الأقل صلاحية أولًا", "ابدأ بأضيق صلاحيات ممكنة، ووسّعها بعد القياس لا قبله"),
    ("سجّل وتعلّم", "كل خطأ AI فرصة مجانية لتوثيق نقطة ضعف النموذج وتصحيحها"),
]
ry = y - 34
for i, (t, d) in enumerate(rules):
    draw_ar(c, W - M - 12, ry, f"٠{i+1}  {t}", font="Amiri-B", size=8.2, color=NAVY, align="right")
    para_ar(c, M + 10, ry, d, font="Amiri", size=7.3, leading=10.5, max_w=CW - 120, color=INK)
    ry -= 18
y = y - 104
c.setFillColor(GOLD); c.rect(M, y - 32, 4, 32, stroke=0, fill=1)
draw_ar(c, W - M - 12, y - 13, "«ليس السؤال: هل الذكاء الاصطناعي خطير؟", font="Amiri-BI", size=13, color=NAVY, align="right")
draw_ar(c, W - M - 12, y - 30, "بل: من يحرسُ الحارسَ — ويدقّق الخوارزمية؟»", font="Amiri-BI", size=13, color=NAVY, align="right")
c.showPage()
