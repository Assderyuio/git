# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, "/home/user/git/ai-report")
from report_lib import *
import math
ASSETS = "/home/user/git/ai-report/assets/"
CHARTS = "/home/user/git/ai-report/charts/"

# ============ PAGE 4 — CH.01 INTRODUCTION ============
chrome(c, 4, TOTAL)
y = section_banner(c, "٠١", "مقدّمة: ما هو الذكاء الاصطناعي؟", "INTRODUCTION")
# pull quote
c.setFillColor(GOLD); c.rect(W - M - 3, y - 46, 3.5, 44, stroke=0, fill=1)
draw_ar(c, W - M - 16, y - 16, "«ليس الذكاء الاصطناعي اختراقًا تقنيًا فحسب،", font="Amiri-BI", size=14.5, color=NAVY, align="right")
draw_ar(c, W - M - 16, y - 36, "بل مرآةٌ نرى فيها أنفسنا من جديد»", font="Amiri-BI", size=14.5, color=NAVY, align="right")
y -= 62

draw_ar(c, W - M, y, "التعريف", font="Amiri-B", size=12.5, color=TEAL, align="right")
y -= 6
y = para_ar(c, M, y, "الذكاء الاصطناعي (Artificial Intelligence) هو قدرةُ الأنظمة الحاسوبية على أداءِ مهامٍ تتطلب عادةً ذكاءً بشريًا — كالتعلّمِ والاستدلالِ والإدراك وفهمِ اللغة والتخطيط — دون أن تُبرمجَ بذلك حرفيًا، بل عبر اكتشاف الأنماط في البيانات.", font="Amiri", size=10.5, leading=19, color=INK)
y -= 4
y = para_en(c, M, y, "“The capability of computational systems to perform tasks typically requiring human intelligence — learning, reasoning, perception, language understanding — by discovering patterns in data rather than following explicit rules.”", font="Amiri-I", size=8.3, leading=13.5, color=GRAY)
y -= 14

draw_ar(c, W - M, y, "ثلاثةُ مستوياتٍ للذكاء", font="Amiri-B", size=12.5, color=TEAL, align="right")
y -= 8
levels = [
    ("ANI", "الذكاء الضيق", "Narrow AI", "يتفوق في مهمةٍ محددة واحدة. كل ما هو موجود اليوم — من ChatGPT إلى توصيات يوتيوب.", "موجود اليوم", TEAL, TEALPALE),
    ("AGI", "الذكاء العام", "General AI", "ذكاءٌ يعادل البشر في أي مهمةٍ معرفية. لم يتحقق — ويتنافس على بنائه الجميع.", "قيد السباق", GOLD, GOLDPALE),
    ("ASI", "الذكاء الفائق", "Superintelligence", "يتجاوز البشر في كل مجال. مفهومٌ افتراضي يفتح أكبر أسئلة الفلسفة والأخلاق.", "افتراضي", GRAY, CREAM),
]
lw = (CW - 20) / 3
for i, (abbr, ar_n, en_n, desc, status, accent, fill) in enumerate(levels):
    lx = M + i * (lw + 10)
    note_box(c, lx, y, lw, 112, fill=fill, stroke=LINE, radius=6)
    c.setFillColor(accent); c.roundRect(lx, y - 5, lw, 5, 2, stroke=0, fill=1)
    draw_ar(c, lx + lw / 2, y - 22, abbr, font="Amiri-B", size=17.5, color=NAVY, align="center")
    draw_ar(c, lx + lw / 2, y - 40, ar_n, font="Amiri-B", size=12.5, color=NAVY, align="center")
    letterspaced(c, lx + lw / 2, y - 52, en_n.upper(), font="Amiri-B", size=5.4, color=GRAY, tracking=1.6, align="center")
    para_ar(c, lx + 8, y - 60, desc, font="Amiri", size=7.6, leading=11.5, max_w=lw - 16, color=INK)
    c.setFillColor(accent)
    c.roundRect(lx + lw/2 - 34, y - 108, 68, 12.5, 6.2, stroke=0, fill=1)
    draw_ar(c, lx + lw / 2, y - 104.6, status, font="Amiri-B", size=7, color=PAPER, align="center")
y -= 128

draw_ar(c, W - M, y, "ستةُ فروعٍ تُشكّل العائلة", font="Amiri-B", size=12.5, color=TEAL, align="right")
y -= 8
pills = [
    ("تعلّم الآلة", "MACHINE LEARNING"), ("التعلّم العميق", "DEEP LEARNING"),
    ("معالجة اللغة الطبيعية", "NLP"), ("الرؤية الحاسوبية", "COMPUTER VISION"),
    ("الروبوتات الذكية", "ROBOTICS"), ("الأنظمة الخبيرة", "EXPERT SYSTEMS"),
]
pw, ph, gap = (CW - 12) / 2, 24, 6
for i, (a, e) in enumerate(pills):
    r, col = divmod(i, 2)
    px = M + col * (pw + 12)
    py = y - r * (ph + gap)
    c.setFillColor(PAPER); c.setStrokeColor(TEAL); c.setLineWidth(1.0)
    c.roundRect(px, py - ph, pw, ph, 12, stroke=1, fill=1)
    draw_ar(c, px + pw - 12, py - 15.5, a, font="Amiri-B", size=9.5, color=NAVY, align="right")
    letterspaced(c, px + 12, py - 15, e, font="Amiri-B", size=5.6, color=TEAL, tracking=1.2, align="left")
y = y - 3 * (ph + gap) - 16

draw_ar(c, W - M, y, "لماذا انفجرَ الاهتمامُ الآن؟", font="Amiri-B", size=12.5, color=TEAL, align="right")
y -= 8
reasons = [
    ("البيانات", "محتوى العالم الرقمي يُقاس اليوم بمئات الإيتابايت؛ وقودُ النماذج لا ينضب."),
    ("القدرة الحاسوبية", "معالجات GPU ومراكز بيانات بحجم الاستادات خفّضت زمن التدريب من سنوات إلى أسابيع."),
    ("الخوارزميات", "معمارية Transformer عام 2017 («الانتباه هو كل ما تحتاجه») أطلقت شرارة العصر التوليدي."),
]
ry = y
for i, (t, d) in enumerate(reasons):
    diamond(c, W - M - 5, ry - 7, 3.1, GOLD)
    draw_ar(c, W - M - 18, ry - 9, t, font="Amiri-B", size=10, color=NAVY, align="right")
    para_ar(c, M, ry - 21, d, font="Amiri", size=8.6, leading=13.5, max_w=CW - 18, color=INK)
    ry -= 42
y = ry - 6
note_box(c, M, y, CW, 132, fill=PAPER, stroke=LINE)
draw_ar(c, W - M - 12, y - 15, "ثلاثُ خرافاتٍ شائعة — وحقائقُها", font="Amiri-B", size=10, color=NAVY, align="right")
myths = [
    ("خرافة · الذكاء الاصطناعي = روبوتات بشرية واعية", "حقيقة · كل ما هو موجود اليوم «ذكاء ضيق» — يتفوق في مهمة واحدة بلا وعي ولا إرادة"),
    ("خرافة · سيستيقظ فجأةً ويسيطر على البشر", "حقيقة · إنه إحصاء احتمالات أنيق — الخطر الحقيقي قرارات تصنعها البشرية لا «تمرّد» الآلة"),
    ("خرافة · سيحل محل كل البشر خلال سنوات", "حقيقة · يحل محل المهام لا المهن — من يتبناه سيحل محل من يرفضه"),
]
my = y - 34
for m, t in myths:
    draw_ar(c, W - M - 12, my, m, font="Amiri-B", size=7.6, color=RED, align="right")
    draw_ar(c, W - M - 24, my - 12, t, font="Amiri", size=7.6, color=TEAL, align="right")
    my -= 30
c.showPage()

# ============ PAGE 5 — CH.02 TIMELINE ============
chrome(c, 5, TOTAL)
y = section_banner(c, "٠٢", "مسيرةُ ٧٥ عامًا: من تورينج إلى اليوم", "1950-2026 · A 75-YEAR JOURNEY")
draw_ar(c, W - M, y, "ثلاثةُ أرباعِ قرن بين سؤالٍ فلسفي وعصرٍ كامل", font="Amiri", size=9.5, color=GRAY, align="right")
y -= 16
milestones = [
    ("1950", "اختبار تورينج", "Can machines think? — سؤال ألان تورينج يؤسس المجال"),
    ("1956", "مؤتمر دارتموث", "صياغة مصطلح «الذكاء الاصطناعي» رسميًا"),
    ("1966", "ELIZA", "أول برنامج محادثة يخدع البشر ويُحاورهم"),
    ("1997", "ديب بلو × كاسپاروف", "الحاسوب يهزم بطل العالم للشطرنج"),
    ("2011", "IBM Watson", "يفوز بمسابقة Jeopardy! بفهم اللغة الطبيعية"),
    ("2012", "AlexNet", "فوز ساحق في ImageNet يطلق ثورة التعلم العميق"),
    ("2016", "AlphaGo", "يهزم سيد لعبة «جو» ذات الـ 3000 عام"),
    ("2017", "Transformer", "ورقة «Attention Is All You Need» تُغيّر كل شيء"),
    ("2022", "ChatGPT", "١٠٠ مليون مستخدم خلال شهرين — أسرع منتج بالتاريخ"),
    ("2024", "نوبل للكيمياء", "Demis Hassabis وJohn Jumper عن AlphaFold"),
    ("2025", "عصر الوكلاء", "وكلاء ذكاء + ذهبية أولمبياد الرياضيات (Gemini Deep Think)"),
    ("2026", "العصر الذهبي", "٨٨٪ من المؤسسات تتبناه — وأنت تقرأ هذا التقرير"),
]
line_x = M + 10
top_line = y + 4
bot_line = y - len(milestones) * 46.5 - 6
c.setStrokeColor(GOLD); c.setLineWidth(2.2)
c.line(line_x, top_line, line_x, bot_line)
my = y
for i, (year, t, d) in enumerate(milestones):
    my = y - i * 46.5
    c.setFillColor(NAVY); c.circle(line_x, my - 4, 5.6, stroke=0, fill=1)
    c.setStrokeColor(GOLD); c.setLineWidth(1.3); c.circle(line_x, my - 4, 5.6, stroke=1, fill=0)
    draw_ar(c, line_x + 14, my - 8, year, font="Amiri-B", size=12.5, color=GOLD if year not in ("2026",) else RED, align="left")
    draw_ar(c, W - M, my + 2, t, font="Amiri-B", size=10, color=NAVY, align="right")
    para_ar(c, line_x + 66, my - 11, d, font="Amiri", size=8.2, leading=12, max_w=W - M - line_x - 66, color=INK)
y = bot_line - 14
note_box(c, M, y, CW, 34, fill=GOLDPALE, stroke=GOLD2, radius=6)
draw_ar(c, W - M - 12, y - 14, "الدرسُ التاريخي:", font="Amiri-B", size=9, color=RED, align="right")
draw_ar(c, W - M - 12, y - 27, "كلُّ موجةِ ضجيجٍ يتبعها «شتاءٌ للذكاء الاصطناعي»، لكن خطَّ التقدم العام تصاعديٌّ دومًا نحو القمة.", font="Amiri", size=8.6, color=INK, align="right")
c.showPage()

# ============ PAGE 6 — CH.03 UNDER THE HOOD ============
chrome(c, 6, TOTAL)
y = section_banner(c, "٠٣", "كيف يعملُ الذكاء الاصطناعي؟", "UNDER THE HOOD")

# --- nested hierarchy (left) + legend (right) ---
nest_top = y
nest_h = 196
ecx, ecy = M + 96, nest_top - nest_h / 2
c.setFillColor(NAVY); c.ellipse(ecx - 118, ecy - 88, ecx + 118, ecy + 88, stroke=0, fill=1)
c.setFillColor(TEAL); c.ellipse(ecx - 92, ecy - 66, ecx + 92, ecy + 66, stroke=0, fill=1)
c.setFillColor(GOLD); c.ellipse(ecx - 67, ecy - 45, ecx + 67, ecy + 45, stroke=0, fill=1)
c.setFillColor(RED);  c.ellipse(ecx - 42, ecy - 25, ecx + 42, ecy + 25, stroke=0, fill=1)
for label, dy, col in [("AI", 66, PAPER), ("ML", 45, PAPER), ("DL", 24, NAVY), ("GenAI", 0, PAPER)]:
    draw_ar(c, ecx, ecy + dy + (6 if label == "GenAI" else 2), label, font="Amiri-B", size=13 if label != "GenAI" else 11.5, color=col, align="center")
leg_x = M + 232
legend = [
    (NAVY, "الذكاء الاصطناعي", "ARTIFICIAL INTELLIGENCE", "المظلة الكبرى: أي آلة تُحاكي الذكاء البشري"),
    (TEAL, "تعلّم الآلة", "MACHINE LEARNING", "تتعلم الأنماط من البيانات بدلًا من قواعد مبرمجة"),
    (GOLD, "التعلّم العميق", "DEEP LEARNING", "شبكات عصبية متعددة الطبقات تحاكي القشرة البصرية"),
    (RED,  "الذكاء التوليدي", "GENERATIVE AI", "يُنشئ نصًا وصورًا وصوتًا وكودًا من الصفر"),
]
ly = nest_top - 6
for col, a, e, d in legend:
    c.setFillColor(col); c.circle(leg_x + 4, ly - 4, 4.6, stroke=0, fill=1)
    draw_ar(c, leg_x + 14, ly - 7, a, font="Amiri-B", size=10.5, color=NAVY, align="left")
    letterspaced(c, leg_x + 14, ly - 17.5, e, font="Amiri-B", size=5, color=GRAY, tracking=1.2, align="left")
    para_ar(c, leg_x + 14, ly - 21, d, font="Amiri", size=7.8, leading=11.5, max_w=CW - (leg_x - M) - 14, color=INK, align="left")
    ly -= 46
y = nest_top - nest_h - 14

# --- pipeline chevrons ---
draw_ar(c, W - M, y, "الرحلةُ من البياناتِ إلى الإجابة", font="Amiri-B", size=12.5, color=TEAL, align="right")
y -= 8
steps = [("البيانات", "DATA"), ("التدريب", "TRAIN"), ("النموذج", "MODEL"), ("التوليد", "GENERATE")]
sw, sh, gap2 = 116, 34, 16
for i, (a, e) in enumerate(steps):
    sx = W - M - (i + 1) * sw - i * gap2
    c.setFillColor(NAVY if i < 3 else GOLD)
    c.roundRect(sx, y - sh, sw, sh, 6, stroke=0, fill=1)
    draw_ar(c, sx + sw / 2, y - 14.5, a, font="Amiri-B", size=12, color=GOLD2 if i < 3 else NAVY, align="center")
    letterspaced(c, sx + sw / 2, y - 27, e, font="Amiri-B", size=6, color=PAPER if i < 3 else NAVY2, tracking=2, align="center")
    if i < 3:
        diamond(c, sx - gap2 / 2, y - sh / 2, 2.6, GRAY)
y = y - sh - 16

# --- bottom split: tokens (right) + neural net (left) ---
half = (CW - 12) / 2
note_box(c, M, y, half, 128, fill=CREAM, stroke=LINE)
draw_ar(c, M + half - 12, y - 16, "كيف تقرأ النماذج الكلام؟", font="Amiri-B", size=10, color=NAVY, align="right")
para_en(c, M + 12, y - 34, "“The cat drinks milk”  »", font="Amiri-B", size=9.5, color=TEAL)
tok_y = y - 52
total_tok_w = sum(pdfmetrics.stringWidth(t, "Amiri", 8.5) + 18 for t in ["The", " cat", " drinks", " milk", " END "])
tx = M + (half - total_tok_w) / 2
for t in ["The", " cat", " drinks", " milk", " END "]:
    tw = pdfmetrics.stringWidth(t, "Amiri", 8.5) + 18
    c.setFillColor(TEALPALE); c.setStrokeColor(TEAL); c.setLineWidth(0.8)
    c.roundRect(tx, tok_y - 15, tw, 16, 8, stroke=1, fill=1)
    c.setFillColor(NAVY); c.setFont("Amiri", 8.5)
    c.drawString(tx + 9, tok_y - 10.5, t)
    tx += tw + 6
para_ar(c, M + 12, tok_y - 26, "كل كلمةٍ تُجزّأ إلى «رموز» (Tokens)، ويتنبأ النموذج بالرمز التالي — مرةً بعد مرة — حتى تكتمل الجملة.", font="Amiri", size=8, leading=12.5, max_w=half - 24, color=INK)

nbx = M + half + 12
note_box(c, nbx, y, half, 128, fill=PAPER, stroke=LINE)
draw_ar(c, nbx + half - 12, y - 16, "الشبكة العصبية — بعيونٍ رياضية", font="Amiri-B", size=10, color=NAVY, align="right")
# neural net drawing
nn_cx = nbx + half / 2
layers = [3, 4, 4, 2]
xn0, xn1 = nbx + 26, nbx + half - 26
col_x = [xn0 + i * (xn1 - xn0) / (len(layers) - 1) for i in range(len(layers))]
ys = []
for li, n in enumerate(layers):
    layer_ys = []
    for ni in range(n):
        yy2 = y - 34 - (ni + 0.5) * 74 / n
        layer_ys.append(yy2)
    ys.append(layer_ys)
c.setLineWidth(0.55)
for li in range(len(layers) - 1):
    for y1 in ys[li]:
        for y2 in ys[li + 1]:
            c.setStrokeColor(Color(0.55, 0.75, 0.74, alpha=0.55))
            c.line(col_x[li], y1, col_x[li + 1], y2)
for li, n in enumerate(layers):
    for yy2 in ys[li]:
        c.setFillColor(TEAL2 if li == 0 else (GOLD2 if li == len(layers) - 1 else NAVY2))
        c.setStrokeColor(PAPER); c.setLineWidth(1)
        c.circle(col_x[li], yy2, 5.2, stroke=1, fill=1)
letterspaced(c, nn_cx, y - 122.5, "INPUT · HIDDEN · OUTPUT", font="Amiri-B", size=5.4, color=GRAY, tracking=1.6, align="center")
y = y - 148
draw_ar(c, W - M, y, "ثلاثةُ أنماطٍ للتعلّم الآلي", font="Amiri-B", size=11.5, color=TEAL, align="right")
y -= 8
learn_rows = [
    ["النمط", "كيف يتعلم", "مثال حي"],
    ["التعلّم بإشراف Supervised", "أمثلة موسومة «صحيح / خطأ» — يصحح أخطاءه عبر التدريب", "التعرف على الصور · فلترة البريد المزعج"],
    ["التعلّم غير المُراقب Unsupervised", "يكتشف المجموعات والبنية بنفسه دون إجابات", "تقسيم العملاء · محركات التوصية"],
    ["التعلّم المعزز Reinforcement", "مكافأة وعقاب عبر التجربة والألعاب والمحاكاة", "AlphaGo · الروبوتات · القيادة الذاتية"],
]
y = table_ar(c, M, y, [CW * 0.27, CW * 0.42, CW * 0.31], learn_rows, header_rows=1, size=7.3, pad=4.5)
y -= 10
draw_ar(c, W - M, y, "ما يتعلمه النموذج ليس حقائقَ محفوظة، بل احتمالاتِ الأنماط — وهذا سرُّ قدرته… ومصدر أخطائه معًا.", font="Amiri-I", size=9, color=GRAY, align="right")
c.showPage()
