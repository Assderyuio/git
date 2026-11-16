# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, "/home/user/git/ai-report")
from report_lib import *
import math
ASSETS = "/home/user/git/ai-report/assets/"
CHARTS = "/home/user/git/ai-report/charts/"

# ============ PAGE 7 — CH.04 AI BY THE NUMBERS ============
chrome(c, 7, TOTAL)
y = section_banner(c, "٠٤", "الذكاء الاصطناعي بالأرقام", "AI BY THE NUMBERS")
c.drawImage(CHARTS + "chart_market.png", M, y - 205, width=CW, height=205, preserveAspectRatio=False)
para_en(c, M, y - 210, "Fig. 1 — Market actuals 2025/26 and projection to 2033 at 30.6% CAGR. Source: Grand View Research; 2027–2032 interpolated. [1]", font="Amiri-I", size=6.6, color=GRAY)
y = y - 232
card_h, gap = 76, 10
cw = (CW - 3 * gap) / 4
for i, (big, lab, sub, col) in enumerate([
    ("$539.5B", "حجم السوق العالمية المقدّرة لعام 2026", "GRAND VIEW RESEARCH", TEAL),
    ("$3.5T", "السوق المتوقعة بحلول 2033", "6.5× GROWTH IN A DECADE", NAVY),
    ("30.6%", "معدل النمو السنوي المركب 2026–2033", "CAGR — COMPOUNDING", GOLD),
    ("$15.7T", "الأثر المحتمل على الناتج العالمي 2030", "PWC — SIZING THE PRIZE", RED),
]):
    stat_card(c, M + i * (cw + gap), y, cw, card_h, big, lab, sub, big_color=col)
y -= card_h + 14
draw_ar(c, W - M, y, "كيف تقرأ هذه الأرقام بذكاء؟", font="Amiri-B", size=11.5, color=TEAL, align="right")
y -= 8
reading = [
    "تقديرات 2026 تتراوح بين $376B (Fortune BI) و$539.5B (GVR) و$707B (Statista) و$900B (Precedence) — الفارق في التعريف لا في الواقع. [3]",
    "Gartner تعدّ $2.67T «إنفاقًا كليًا على AI» (بنية تحتية وخدمات) — ليس إيرادات سوق، ولا يُدمج مع تقديرات GVR. [3]",
    "IDC: إنفاق بنية AI التحتية وحده $487B في 2026 (+53%) وسيتجاوز $1T بحلول 2029 — الشركات تشتري المجارف لا الذهب. [15]",
]
for b in reading:
    diamond(c, W - M - 5, y - 6, 2.4, TEAL)
    y = para_ar(c, M, y, b, font="Amiri", size=8.6, leading=13.5, max_w=CW - 16, color=INK)
    y -= 5
y -= 6
note_box(c, M, y, CW, 88, fill=NAVY, stroke=NAVY, radius=8)
draw_ar(c, W - M - 16, y - 16, "الاستثمار الشركاتي العالمي في AI تضاعف ليتجاوز", font="Amiri", size=9, color=HexColor("#C7D3DE"), align="right")
draw_ar(c, W / 2, y - 44, "$581.7B", font="Amiri-B", size=27, color=GOLD2, align="center")
para_en(c, M + 40, y - 56, "Corporate AI investment more than doubled in 2025 (Stanford AI Index 2026) — private investment up 127.5%, now 60% of the total, with GenAI capturing nearly half of every private AI dollar. [4]", font="Amiri", size=7.2, leading=11, max_w=CW - 80, color=HexColor("#DCE6EE"), align="center")
y = y - 100
note_box(c, M, y, CW, 42, fill=CREAM, stroke=LINE)
draw_ar(c, W - M - 12, y - 15, "حقيقة سريعة — في كل ثانية تمر، يُولّد العالم بياناتٍ تكفي لتدريب نموذج ذكي كامل.", font="Amiri-B", size=8.8, color=NAVY, align="right")
draw_ar(c, W - M - 12, y - 30, "الوقود لا ينفد — والسؤال فقط: من يحوّله إلى ذكاء؟", font="Amiri-I", size=7.6, color=GRAY, align="right")
c.showPage()

# ============ PAGE 8 — CH.04 CONTINUED ============
chrome(c, 8, TOTAL)
letterspaced(c, W - M, H - 70, "CHAPTER 04 — CONTINUED", font="Amiri-B", size=6.8, color=TEAL, tracking=2.2, align="right")
# barriers kicker drawn above the cards

draw_ar(c, W - M, H - 94, "التبنّي: من التجربة إلى التيار الرئيسي", font="Amiri-B", size=20, color=NAVY, align="right")
c.setStrokeColor(GOLD); c.setLineWidth(2.2); c.line(W - M, H - 104, W - M - 74, H - 104)
y = H - 118
c.drawImage(CHARTS + "chart_adoption.png", M, y - 208, width=CW, height=208, preserveAspectRatio=False)
para_en(c, M, y - 213, "Fig. 2 — Adoption snapshot 2026: organizations 88% · students 4-of-5 · GenAI population penetration 53% in 3 years. [4]", font="Amiri-I", size=6.6, color=GRAY)
y = y - 232

half = (CW - 12) / 2
# right column (RTL first): "must-know numbers"
note_box(c, M + half + 12, y, half, 218, fill=CREAM, stroke=LINE)
draw_ar(c, W - M - 12, y - 16, "أرقامٌ يجب أن تعرفها", font="Amiri-B", size=11, color=NAVY, align="right")
mustknow = [
    ("$37B", "إنفاق المؤسسات على GenAI في 2025 — نمو 3.2× عن 2024 (Menlo Ventures) [13]"),
    ("1,953", "شركة AI مصرّحة التمويل في أمريكا 2025 — 10× أقرب منافس [4]"),
    ("+90%", "من النماذج الرائدة في 2025 صدرت من الصناعة لا الأكاديمية [4]"),
    ("4 من 5", "من طلاب الجامعات يستخدمون GenAI بانتظام — جيلٌ وُلد ذكيًا [4]"),
    ("23×", "فجوة الاستثمار الخاص بين أمريكا ($285.9B) والصين ($12.4B) [4]"),
]
my = y - 34
for big, txt in mustknow:
    draw_ar(c, W - M - 12, my, big, font="Amiri-B", size=13, color=TEAL, align="right")
    bw = ar_width(big, "Amiri-B", 13)
    my = para_ar(c, M + half + 12 + 12, my, txt, font="Amiri", size=7.4, leading=11, max_w=half - 24 - bw - 8, color=INK)
    my -= 4.5

# left column: segment donut
note_box(c, M, y, half, 218, fill=PAPER, stroke=LINE)
cid = c.drawImage(CHARTS + "chart_segment.png", M + 6, y - 172, width=half - 12, height=150, preserveAspectRatio=True, anchor="c")
draw_ar(c, M + half / 2, y - 184, "تعلّم الآلة يسيطر — والذكاء التوليدي يلتهم المؤسسات", font="Amiri-B", size=8.4, color=NAVY, align="center")
para_en(c, M + 12, y - 201, "ML ~37% · NLP ~30% — shares vary by source. [3][5]", font="Amiri-I", size=6, color=GRAY, align="left")
y = y - 232

# barriers trio
draw_ar(c, W - M, y, "لماذا يتعثر الكبار أحيانًا؟ ثلاثة حواجز — وحلولها", font="Amiri-B", size=10, color=TEAL, align="right")
y -= 8
barriers = [
    ("تكلفة البنية التحتية", "ادفع بقدر الاستخدام السحابي — لا تشترِ مجارف قبل أن تجد ذهبًا"),
    ("جودة البيانات", "80% من فشل مشاريع AI سببه البيانات — نظّف قبل أن تبني أي نموذج"),
    ("فجوة المواهب", "ابدأ بأدوات بلا كود، ودرّب فريقك داخليًا — لا تنتظر «الخبير المثالي»"),
]
bb_w = (CW - 16) / 3
for i, (t, d) in enumerate(barriers):
    x0 = M + (2 - i) * (bb_w + 8)
    note_box(c, x0, y, bb_w, 78, fill=CREAM, stroke=LINE, radius=6)
    c.setStrokeColor(RED); c.setLineWidth(2.0)
    c.line(x0 + 12, y - 2.2, x0 + 44, y - 2.2)
    draw_ar(c, x0 + bb_w - 10, y - 14, t, font="Amiri-B", size=8.6, color=NAVY, align="right")
    para_ar(c, x0 + 8, y - 20, d, font="Amiri", size=6.8, leading=10, max_w=bb_w - 16, color=INK)
y = y - 92

c.setFillColor(GOLD); c.rect(M, y - 30, 4, 30, stroke=0, fill=1)
draw_ar(c, W - M - 12, y - 12, "الخلاصة: الذكاء الاصطناعي لم يعد تكنولوجياً مستقبلية —", font="Amiri-BI", size=13, color=NAVY, align="right")
draw_ar(c, W - M - 12, y - 29, "إنه بنيةٌ تحتيةٌ اقتصاديةٌ تُقرأ في ميزانيات الدول اليوم.", font="Amiri-BI", size=13, color=NAVY, align="right")
c.showPage()

# ============ PAGE 9 — CH.05 GENAI REVOLUTION ============
chrome(c, 9, TOTAL)
y = section_banner(c, "٠٥", "الثورةُ التوليدية والنماذجُ اللغوية", "THE GENAI REVOLUTION")
img_cover_crop(c, ASSETS + "genai_wave.jpg", M, y - 108, CW, 108, radius=8)
c.setFillColor(Color(0.04, 0.10, 0.18, alpha=0.52)); c.roundRect(M, y - 108, CW, 108, 8, stroke=0, fill=1)
c.setFillColor(Color(0.03, 0.08, 0.15, alpha=0.55)); c.roundRect(M + 8, y - 46, CW - 16, 26, 6, stroke=0, fill=1)
draw_ar(c, W - M - 20, y - 28.5, "الذكاء الذي «يرى» و«يكتب» و«يلحّن» — لا مجرد «يقرأ»", font="Amiri-B", size=11.5, color=PAPER, align="right")
para_en(c, M + 12, y - 96, "GenAI surged past 53% population adoption faster than the PC — and captured nearly half of private AI funding. [4]", font="Amiri", size=7, color=HexColor("#E8EEF3"))
y = y - 124

draw_ar(c, W - M, y, "كيف تفكّر النماذج اللغوية العملاقة؟ خمسُ خطوات", font="Amiri-B", size=11.5, color=TEAL, align="right")
y -= 8
steps5 = [
    ("١", "التقطيع", "النص » رموز (Tokens)"),
    ("٢", "الانتباه", "كل كلمة توازن كلمات السياق"),
    ("٣", "التنبؤ", "ترجيح احتمال الرمز التالي"),
    ("٤", "التكرار", "رمزًا رمزًا حتى نهاية الفكرة"),
    ("٥", "الإخراج", "نص · كود · صورة · صوت · فيديو"),
]
sw5, sh5, gap5 = (CW - 4 * 8) / 5, 52, 8
for i, (n, t, d) in enumerate(steps5):
    sx = W - M - (i + 1) * sw5 - i * gap5
    c.setFillColor(NAVY2 if i % 2 == 0 else STEEL)
    c.roundRect(sx, y - sh5, sw5, sh5, 6, stroke=0, fill=1)
    draw_ar(c, sx + sw5 - 8, y - 11, n, font="Amiri-B", size=10, color=GOLD2, align="right")
    draw_ar(c, sx + sw5 / 2, y - 22, t, font="Amiri-B", size=9.5, color=PAPER, align="center")
    para_ar(c, sx + 4 + (sw5 - 8) / 2, y - 29, d, font="Amiri", size=6.2, leading=9, max_w=sw5 - 8, color=HexColor("#C7D3DE"), align="center")
y = y - sh5 - 14

draw_ar(c, W - M, y, "مشهدُ النماذج العالمي — خريطةُ ٢٠٢٦", font="Amiri-B", size=11.5, color=TEAL, align="right")
y -= 8
model_rows = [
    ["النموذج", "الشركة", "موطن القوة"],
    ["GPT (الإصدارات الحديثة)", "OpenAI · أمريكا", "التوازن العام وأوسع انتشار عالميًا"],
    ["Claude", "Anthropic · أمريكا", "البرمجة والوكلاء والكتابة الطويلة"],
    ["Gemini", "Google DeepMind · أمريكا", "تعدد الوسائط وسلسلة Gemini 3 وDeep Think الذهبية"],
    ["Llama", "Meta · أمريكا", "مفتوح الأوزان — سيادة المؤسسات والبحث"],
    ["DeepSeek", "DeepSeek · الصين", "كفاءة وتكلفة — رهان «الأقل بالذكاء أكثر»"],
    ["Mistral", "Mistral AI · فرنسا", "السيادة الأوروبية والنماذج المفتوحة الصغيرة"],
    ["Grok", "xAI · أمريكا", "المعلومات اللحظية من منصة X"],
    ["Qwen", "Alibaba · الصين", "الأقوى في العربية والصينية ضمن الفئة المفتوحة"],
]
y = table_ar(c, M, y, [CW * 0.30, CW * 0.27, CW * 0.43], model_rows, header_rows=1, size=8.0, pad=4.5)
y -= 8
note_box(c, M, y, CW, 30, fill=GOLDPALE, stroke=GOLD2)
draw_ar(c, W - M - 12, y - 13, "الصين تُغلق الفجوة: أقرب نموذج صيني يتأخر 2.7% فقط عن الأفضل أمريكيًا (مارس 2026) [4]", font="Amiri-B", size=8.6, color=RED, align="right")
draw_ar(c, W - M - 12, y - 25, "وهذا يعني: السباق لم يعد حكرًا على طرف — المنافسة تُخفض الأسعار وترفع الجودة للجميع.", font="Amiri", size=7.6, color=INK, align="right")
y = y - 42
half9 = (CW - 12) / 2
for i, (t, d, accent, fill) in enumerate([
    ("نموذج مفتوح الأوزان", "Llama · Mistral · Qwen — خصوصية كاملة وصفر تكلفة ترخيص، لكنه يحتاج فريقًا وقدرة تشغيلية — وأفضل قيمة للحجم الكبير", TEAL, TEALPALE),
    ("نموذج مغلق (API)", "GPT · Claude · Gemini — أذكى فورًا والدفع بالاستخدام — خصوصية عبر عقود المؤسسات — الأفضل للذروة وللبداية السريعة", NAVY, CREAM),
]):
    x0 = M + (1 - i) * (half9 + 12)   # RTL: first on the right
    note_box(c, x0, y, half9, 66, fill=fill, stroke=LINE, radius=6)
    c.setFillColor(accent); c.rect(x0, y - 66, 4, 66, stroke=0, fill=1)
    draw_ar(c, x0 + half9 - 10, y - 13, t, font="Amiri-B", size=9, color=NAVY, align="right")
    para_ar(c, x0 + 8, y - 19, d, font="Amiri", size=7.2, leading=11, max_w=half9 - 16, color=INK)
c.showPage()

# ============ PAGE 10 — CH.06 AI ACROSS INDUSTRIES ============
chrome(c, 10, TOTAL)
y = section_banner(c, "٠٦", "الذكاء الاصطناعي في القطاعات", "AI ACROSS INDUSTRIES")
cards = [
    ("01", "الرعاية الصحية", "HEALTHCARE", ["AlphaFold: أكثر من 200M بنية بروتينية متاحة مجانًا للعلم — نوبل 2024", "تشخيص أشعةٍ وصور طبية بدقةٍ تضاهي الأطباء في مهام محددة", "أدوية تُطوَّر في سنوات بدلًا من عقد"], TEAL),
    ("02", "التعليم", "EDUCATION", ["معلم خصوصي على مدار الساعة لكل طالب — بشرط الإشراف", "4 من 5 طلاب جامعيين يستخدمون GenAI بانتظام [4]", "تقييم أذكى وتغذية راجعة فورية"], GOLD),
    ("03", "الخدمات المالية", "FINANCE & BFSI", ["كشف احتيال لحظي عبر مليارات المعاملات", "Morgan Stanley: استرجاع موثق من 100 ألف وثيقة للمستشارين", "محافظ ذكية ومخاطر ائتمانية أدق"], NAVY),
    ("04", "الزراعة", "AGRICULTURE", ["رؤية حاسوبية تكشف أمراض المحاصيل قبل انتشارها", "ريٌّ ذكي بالاستشعار والنماذج — توفير حتى 90% مياه في تجارب", "توقع إنتاج وأسعار أدق للمزارع المصري"], GREEN),
    ("05", "النقل واللوجستيات", "TRANSPORT & LOGISTICS", ["أنظمة مثل UPS ORION توفر ~100M ميل سنويًا", "شحن ذاتية القيادة وإدارة أساطيل لحظية", "مضاعفة قدرة الموانئ والجمارك بالتحليل التنبؤي"], RED),
    ("06", "الطاقة والصناعة", "ENERGY & INDUSTRY", ["صيانة تنبؤية تخفض الأعطال 30–50% وتطيل عمر المعدات", "شبكات كهرباء ذكية توازن الحمل والطاقة المتجددة", "روبوتات و«مصانعُ المواضيع المظلمة» تعمل بلا إضاءة"], STEEL),
]
cw3, ch3, gap3 = (CW - 12) / 2, 132, 12
for i, (num, ar_t, en_t, bullets, accent) in enumerate(cards):
    r, col = divmod(i, 2)
    cx0 = M + col * (cw3 + gap3)
    cy = y - r * (ch3 + 10)
    note_box(c, cx0, cy, cw3, ch3, fill=PAPER, stroke=LINE)
    c.setFillColor(accent); c.rect(cx0, cy - ch3, 4, ch3, stroke=0, fill=1)
    draw_ar(c, cx0 + cw3 - 12, cy - 15, num, font="Amiri-B", size=15, color=accent, align="right")
    draw_ar(c, cx0 + cw3 - 38, cy - 15.5, ar_t, font="Amiri-B", size=12.5, color=NAVY, align="right")
    letterspaced(c, cx0 + 12, cy - 16, en_t, font="Amiri-B", size=5.6, color=GRAY, tracking=1.5, align="left")
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(cx0 + 10, cy - 26, cx0 + cw3 - 10, cy - 26)
    by = cy - 40
    for b in bullets:
        c.setFillColor(accent); c.circle(cx0 + cw3 - 14, by - 3, 1.5, stroke=0, fill=1)
        by = para_ar(c, cx0 + 10, by, b, font="Amiri", size=7.6, leading=11.5, max_w=cw3 - 26, color=INK)
        by -= 2.5
y = y - 3 * (ch3 + 10) - 6
note_box(c, M, y, CW, 46, fill=GOLDPALE, stroke=GOLD2)
draw_ar(c, W - M - 12, y - 14, "أين تتركز القيمة؟", font="Amiri-B", size=9.5, color=RED, align="right")
draw_ar(c, W - M - 12, y - 28, "75% من قيمة الذكاء التوليدي تتركز في 4 وظائف: خدمة العملاء · التسويق والمبيعات · هندسة البرمجيات · البحث والتطوير", font="Amiri-B", size=8.4, color=INK, align="right")
draw_ar(c, W - M - 12, y - 40, "— McKinsey Global Institute [7]", font="Amiri-I", size=7, color=GRAY, align="right")
y = y - 62
draw_ar(c, W - M, y, "كيف تختار أول حالة استخدام AI في قطاعك؟ أربعة أسئلة", font="Amiri-B", size=10.5, color=TEAL, align="right")
y -= 8
steps_q = ["أين تتكدس ساعات فريقك على مهام متكررة؟", "أين أغلى خطأ يمكن أن يقع؟", "أين بياناتك أنظف وأكتمل؟", "ابدأ تجربة ٩٠ يومًا — وقِس بالأدلة"]
qw = (CW - 3 * 10) / 4
for i, q in enumerate(steps_q):
    x0 = W - M - (i + 1) * qw - i * 10
    c.setFillColor([NAVY, STEEL, TEAL, GOLD][i])
    c.roundRect(x0, y - 44, qw, 44, 6, stroke=0, fill=1)
    draw_ar(c, x0 + qw - 8, y - 11, f"٠{i+1}", font="Amiri-B", size=9.5, color=GOLD2 if i < 3 else NAVY, align="right")
    para_ar(c, x0 + 8, y - 17, q, font="Amiri-B" if i == 3 else "Amiri", size=7.3, leading=10.5, max_w=qw - 16, color=PAPER if i < 3 else NAVY)
c.showPage()
