# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, "/home/user/git/ai-report")
from report_lib import *
import math
ASSETS = "/home/user/git/ai-report/assets/"
CHARTS = "/home/user/git/ai-report/charts/"

# ============ PAGE 14 — CH.10 ETHICS & GOVERNANCE ============
chrome(c, 14, TOTAL)
y = section_banner(c, "١٠", "الأخلاق والحوكمة — AI Act وما بعده", "ETHICS & GOVERNANCE")

half = (CW - 14) / 2
# right panel: EU AI Act timeline
note_box(c, M + half + 14, y, half, 238, fill=NAVY, stroke=NAVY, radius=8)
px = W - M - 14
letterspaced(c, px, y - 17, "REGULATION 2024/1689", font="Amiri-B", size=5.6, color=GOLD2, tracking=1.6, align="right")
draw_ar(c, px, y - 34, "القانون الأوروبي للذكاء (EU AI Act)", font="Amiri-B", size=11.5, color=PAPER, align="right")
timeline = [
    ("فبراير 2025", "دخول حظر «الممارسات غير المقبولة» حيّز التنفيذ — كالتلاعب السلوكي والتنقيط الاجتماعي"),
    ("أغسطس 2025", "التزامات النماذج العامة GPAI — الشفافية، حقوق النشر، السلامة"),
    ("أغسطس 2026", "غالبية الأحكام والتنفيذ الكامل بما فيها أنظمة عالية المخاطر"),
    ("2027+", "غرامات حتى €35M أو 7% من الإيرادات العالمية — الأغلى في التاريخ التنظيمي"),
]
ty = y - 48
line_x = W - M - 22
c.setStrokeColor(GOLD2); c.setLineWidth(1.4)
c.line(line_x, ty + 2, line_x, ty - 158)
for i, (t, d) in enumerate(timeline):
    yy = ty - i * 42
    c.setFillColor(GOLD); c.circle(line_x, yy, 3.4, stroke=0, fill=1)
    draw_ar(c, line_x - 8, yy - 2, t, font="Amiri-B", size=8.6, color=GOLD2, align="right")
    para_ar(c, M + half + 14 + 10, yy - 13, d, font="Amiri", size=6.9, leading=10, max_w=half - 20, color=HexColor("#DCE6EE"))

# left: six principles
draw_ar(c, M + half - 14, y - 2, "ستةُ مبادئَ لا تقبل التفاوض", font="Amiri-B", size=11.5, color=TEAL, align="right")
principles = [
    ("الشفافية", "قابلية تفسير القرار — لا «الصندوق الأسود»"),
    ("العدالة", "النتائج متساوية عبر الفئات — تدقيق تحيز"),
    ("الخصوصية", "أقل قدر من البيانات — بالغرض نفسه فقط"),
    ("المساءلة", "من يملك القرار النهائي دائمًا إنسان"),
    ("السلامة", "اختبارات ضغط و«تسميم» قبل النشر"),
    ("الرقابة البشرية", "Human-in-the-loop في القرارات الحرجة"),
]
py = y - 22
for i, (t, d) in enumerate(principles):
    note_box(c, M, py, half - 14, 30, fill=CREAM, stroke=LINE, radius=5)
    draw_ar(c, M + half - 26, py - 12, f"٠{i+1}", font="Amiri-B", size=10, color=GOLD, align="right")
    draw_ar(c, M + half - 40, py - 12.5, t, font="Amiri-B", size=9, color=NAVY, align="right")
    para_ar(c, M + 6, py - 17.5, d, font="Amiri", size=6.8, leading=9.5, max_w=half - 24, color=GRAY)
    py -= 37
y = y - 250

# checklist
note_box(c, M, y, CW, 118, fill=GOLDPALE, stroke=GOLD2)
draw_ar(c, W - M - 12, y - 15, "قائمة فحص: قبل إطلاق أي نظام AI في مؤسستك", font="Amiri-B", size=10.5, color=RED, align="right")
checklist = [
    "هل مصدر البيانات قانونيٌّ وأخلاقي وخزّن بموافقة؟",
    "هل يوجد «مالك قرار» بشري لكل مخرج حرج؟",
    "هل تستطيع شرح «لماذا» للمتأثر بالقرار؟",
    "كيف تكتشف التحيز والانحراف (Drift) مبكرًا؟",
    "ما خطة التراجع والإغلاق الآمن عند الفشل؟",
    "هل أُخبر المستخدمون أنهم يتفاعلون مع AI؟",
]
for i in range(3):
    for j in range(2):
        idx = i * 2 + j
        if idx >= len(checklist): break
        bx = W - M - 14 - j * (CW / 2)
        yy = y - 40 - i * 24
        c.setStrokeColor(TEAL); c.setLineWidth(1.2)
        c.rect(bx - 7, yy - 6, 9.5, 9.5, stroke=1, fill=0)
        t = checklist[idx]
        lines = wrap_ar(t, "Amiri", 7.4, CW / 2 - 40)
        draw_ar(c, bx - 14, yy, t, font="Amiri", size=7.4, color=INK, align="right")
y = y - 130
note_box(c, M, y, CW, 46, fill=PAPER, stroke=LINE)
draw_ar(c, W - M - 12, y - 15, "فجوةُ الـ 50 نقطة", font="Amiri-B", size=9.5, color=NAVY, align="right")
draw_ar(c, W - M - 12, y - 31, "73% من خبراء AI يتوقعون أثرًا إيجابيًا على الوظائف — مقابل 23% فقط من الجمهور. الثقة تُبنى بالشفافية لا بالدعاية. [4]", font="Amiri", size=8, color=INK, align="right")
y = y - 56
tool_rows = [
    ["عدة الحوكمة المجانية", "ماذا تفعل"],
    ["OECD AI Principles", "5 قيم دولية متوافقة تتبناها 50+ دولة — خريطة طريق للسياسات"],
    ["NIST AI Risk Management Framework", "إطار عملي مجاني لإدارة مخاطر AI عبر دورة حياة النظام"],
    ["artificialintelligenceact.eu", "شرح مبسط ومحدّث للقانون الأوروبي مع الأسئلة الشائعة"],
    ["Google Model Cards", "توثيق ومقارنة النماذج — من درّب؟ على ماذا؟ وبأي انحياز؟"],
    ["Microsoft Responsible AI Toolbox", "قوالب تدقيق وعدالة وشفافية جاهزة للفرق العملية"],
]
y = table_ar(c, M, y, [CW * 0.42, CW * 0.58], tool_rows, header_rows=1, size=7.0, pad=4)
y -= 10
c.setFillColor(GOLD); c.rect(M, y - 24, 4, 24, stroke=0, fill=1)
draw_ar(c, W - M - 12, y - 10, "«الحوكمة الجيدة ليست عائقًا للابتكار — إنها شرطُ استدامته»", font="Amiri-BI", size=11, color=NAVY, align="right")
draw_ar(c, W - M - 12, y - 22, "— EU AI Act · Oxford Insights · تجربتا سنغافورة والإمارات", font="Amiri-I", size=6.6, color=GRAY, align="right")
c.showPage()

# ============ PAGE 15 — CH.11 JOBS & SKILLS ============
chrome(c, 15, TOTAL)
y = section_banner(c, "١١", "الوظائف والمهارات: من يتغيّر؟", "JOBS & SKILLS")

draw_ar(c, W - M, y, "أ) مهاراتٌ يصعدُ نجمها — بقوة", font="Amiri-B", size=11.5, color=TEAL, align="right")
y -= 8
up_rows = [
    ["المهارة", "لماذا؟"],
    ["وكلاء AI والأنظمة المتعددة", "أعلى طلبٍ في السوق — زيادة +280% في إعلانات الوظائف (Stanford AI Index 2026) [4]"],
    ["Python وSQL", "حجر الأساس المتين لكل أدوار الذكاء الاصطناعي بلا استثناء"],
    ["النشر والسحابة والأمان (AWS…)", "من يبني AI؟ لا يكفي — السوق يدفع لمن يُشغّله بأمان وعلى نطاق"],
    ["تقييم النماذج وهندسة الأوامر", "الدقة تُشترى بالتجربة والقياس — ليس بالحظ"],
    ["أمان AI ومواءمة النماذج", "سوقٌ ناشئ محترق — وعد منحةٍ في كل مختبر رائد"],
    ["الحكم المهني والتفكير النقدي", "الشيء الوحيد الذي لن يُصادَف — ولا يُؤتمت"],
]
y = table_ar(c, M, y, [CW * 0.34, CW * 0.66], up_rows, header_rows=1, size=7.6, pad=4.5)
y -= 12

draw_ar(c, W - M, y, "ب) مهامٌ يتراجعُ الطلبُ عليها", font="Amiri-B", size=11.5, color=RED, align="right")
y -= 8
down_rows = [
    ["المهمة", "الإشارة"],
    ["البرمجة الروتينية للمبتدئين", "تراجع توظيف المطورين 22–25 سنة بنحو 20% منذ 2024 [4]"],
    ["كتابة المحتوى التسويقي العام", "تشبعٌ كامل — المحتوى الذكي يحتاج بصيرةً لا كلمات"],
    ["الترجمة والتوثيق العام", "الآلة تتفوق في الكم والسرعة — الإنسان يتفوق في السياق"],
    ["الدعم الفني المستوى الأول", "روبوتات محادثة تحل ~70% من التذاكر دون بشر"],
    ["إدخال البيانات والتصنيف", "أول ضحايا الأتمتة منذ الجيل الأول للـ RPA"],
]
y = table_ar(c, M, y, [CW * 0.34, CW * 0.66], down_rows, header_rows=1, size=7.6, pad=4.5)
y -= 12

note_box(c, M, y, CW, 74, fill=NAVY, stroke=NAVY, radius=8)
draw_ar(c, W - M - 14, y - 15, "كيف تحمي مسارك المهني؟ أربعُ خطواتٍ غير قابلة للتفاوض", font="Amiri-B", size=10, color=GOLD2, align="right")
steps4 = [
    "كُنْ مستخدمًا محترفًا للذكاء في مهنتك الحالية — لا تنتظر «الذكاء المثالي»",
    "تخصّصٌ نادر + ذكاء اصطناعي = قيمةٌ لا تُنسى في السوق",
    "ابنِ معرض أعمال حقيقي: مشروعان عمليان أقوى من عشر شهادات",
    "٣ ساعات أسبوعيًا تعلّمًا = ١٥٠ ساعة سنويًا تبعدك عن كل المنافسين",
]
for i, s in enumerate(steps4):
    col, row = i % 2, i // 2
    xx = M + 14 + col * (CW / 2 - 6)
    yy = y - 34 - row * 19
    diamond(c, xx + ar_width(s, "Amiri", 7.6) + 6, yy - 2, 2, TEAL2)
    draw_ar(c, xx + CW / 2 - 20, yy, s, font="Amiri", size=7.6, color=HexColor("#DCE6EE"), align="right")
y = y - 88
draw_ar(c, W - M, y, "٣٩٪ من المهارات الأساسية للعاملين ستتغير بحلول 2030 — WEF [8]", font="Amiri-B", size=8.8, color=RED, align="right")

# AI-literacy ladder
y -= 40
letterspaced(c, W - M, y, "THE 2026 AI-CAREER LADDER", font="Amiri-B", size=6.6, color=TEAL, tracking=2, align="right")
draw_ar(c, W - M, y - 12, "سلّمُ الكفاءة الذكية في 2026 — أربعة طوابق", font="Amiri-B", size=11, color=NAVY, align="right")
y -= 20
ladder = [
    ("قارئ واعٍ", "AI LITERACY", "تفهم الحدود والقدرات — لا تنخدع ولا تُرهب"),
    ("مستخدم معزز", "AI-AUGMENTED", "تضاعف إنتاجيتك اليومية بأدوات الدردشة والتحليل"),
    ("مختص منفذ", "AI-OPERATOR", "تدير سير عمل كامل بمساعدة AI مع توثيق وقياس"),
    ("مهندس وكلاء", "AGENTIC ENGINEER", "تبني أنظمة تنفذ وتتحقق — أعلى قيمة في السوق"),
]
lw2 = (CW - 3 * 10) / 4
ladder_h = 96
for i, (t, e, d) in enumerate(ladder):
    x0 = W - M - (i + 1) * lw2 - i * 10
    c.setFillColor([NAVY, STEEL, TEAL, GOLD][i])
    c.roundRect(x0, y - ladder_h, lw2, ladder_h, 6, stroke=0, fill=1)
    draw_ar(c, x0 + lw2 - 8, y - 16, f"٠{i+1}", font="Amiri-B", size=11, color=GOLD2 if i < 3 else NAVY, align="right")
    draw_ar(c, x0 + lw2 / 2, y - 34, t, font="Amiri-B", size=11, color=PAPER if i < 3 else NAVY, align="center")
    letterspaced(c, x0 + lw2 / 2, y - 47, e, font="Amiri-B", size=4.8, color=TEAL2 if i < 3 else NAVY2, tracking=1.1, align="center")
    para_ar(c, x0 + lw2 / 2, y - 57, d, font="Amiri", size=6.6, leading=9.5, max_w=lw2 - 12, color=HexColor("#DCE6EE") if i < 3 else NAVY2, align="center")
letterspaced(c, M, y - ladder_h - 12, "THE JUMPS ARE MEASURED IN PROJECTS, NOT CERTIFICATES — BUILD TWO PROJECTS PER FLOOR", font="Amiri-B", size=4.8, color=GRAY, tracking=1.0, align="left")
c.showPage()

# ============ PAGE 16 — CH.12 90-DAY ROADMAP ============
chrome(c, 16, TOTAL)
y = section_banner(c, "١٢", "خارطةُ طريقِ ٩٠ يومًا — ابدأ اليوم", "YOUR 90-DAY ROADMAP")
road = [
    ("٣٠", "الأيام 1–30", "ابْنِ الأساس", [
        "افهم المفاهيم: AI / ML / LLM / RAG — اقرأ الفصول ٣ و٥ مرتين",
        "سجّل حسابات مجانية: ChatGPT + Claude + Perplexity + Gemini",
        "10 برومتات فعلية في عملك: بريد، تلخيص، تحليل، تخطيط",
        "مشروعك الأول: سيرتك الذاتية وخطتك المهنية بمساعدة AI",
    ]),
    ("٦٠", "الأيام 31–60", "طبّق في الواقع", [
        "اختر مشكلة حقيقية واحدة من عملك أو دراستك",
        "ابنِ أول أتمتة: n8n / Make / Zapier بلا كود",
        "قِس قبل وبعد: وقتٌ · دقةٌ · تكلفة — الأرقام لا المشاعر",
        "وثّق النتيجة في عرض من 5 شرائح وشاركه مع فريقك",
    ]),
    ("٩٠", "الأيام 61–90", "تعمّق وقُد", [
        "ابنِ RAG بسيطًا على مستنداتك — تسأل معرفتك الخاصة",
        "جرّب التقييم: 20 سؤالًا معياريًا — هل يتحسن أداؤك أسبوعيًا؟",
        "استكشف Python + مكتبة OpenAI/Anthropic بدروس مجانية",
        "خطتك التالية: تخصصك الدقيق + AI — شهادة أم مشروع؟",
    ]),
]
cw3 = (CW - 16) / 3
for i, (num, d1, d2, items) in enumerate(road):
    x0 = M + i * (cw3 + 8)
    note_box(c, x0, y, cw3, 218, fill=PAPER, stroke=LINE)
    c.setFillColor(NAVY); c.roundRect(x0, y - 34, cw3, 34, 6, stroke=0, fill=1)
    draw_ar(c, x0 + 12, y - 15, num, font="Amiri-B", size=19, color=GOLD2, align="left")
    draw_ar(c, x0 + cw3 - 12, y - 13, d1, font="Amiri-B", size=10.5, color=PAPER, align="right")
    letterspaced(c, x0 + cw3 - 12, y - 26, d2.upper(), font="Amiri-B", size=5.2, color=TEAL2, tracking=1.2, align="right")
    yy = y - 50
    for j, item in enumerate(items):
        c.setStrokeColor(TEAL); c.setLineWidth(1.1)
        c.rect(x0 + cw3 - 17, yy - 6, 8, 8, stroke=1, fill=0)
        para_ar(c, x0 + 8, yy, item, font="Amiri", size=7.0, leading=10.5, max_w=cw3 - 34, color=INK)
        yy -= len(wrap_ar(item, "Amiri", 7.0, cw3 - 34)) * 10.5 + 7.5
y = y - 232

draw_ar(c, W - M, y, "عدّةُ الأدوات الكاملة — 2026", font="Amiri-B", size=11.5, color=TEAL, align="right")
y -= 8
tool_rows = [
    ["المهمة", "الأداة", "البديل المجاني"],
    ["بحث فوري موثق بالمصادر", "Perplexity Pro", "Perplexity Free / Google AI Mode"],
    ["كتابة وتحليل وتخطيط", "ChatGPT · Claude", "المستويان المجانيان + Gemini"],
    ["البرمجة والمساعد الذكي", "Claude Code · Copilot", "Cursor Free · Qwen Coder"],
    ["توليد الصور", "Midjourney · DALL·E", "SDXL · Flux schnell (مجاني)"],
    ["الصوت والنسخ", "ElevenLabs · Whisper", "Whisper مفتوح المصدر"],
    ["الفيديو التوليدي", "Sora · Runway Gen-4", "Kling · Luma (تجربة مجانية)"],
    ["الأتمتة بلا كود", "n8n (self-hosted) · Make", "n8n Community Edition مجاني"],
]
y = table_ar(c, M, y, [CW * 0.36, CW * 0.34, CW * 0.30], tool_rows, header_rows=1, size=7.4, pad=4)
y -= 10
gold_band = ["ابدأ صغيرًا وكرّر بسرعة", "قِس قبل وبعد دائمًا", "البيانات أولًا ثم الخوارزمية", "الإنسان صاحب القرار الأخير", "الأخلاق ليست رفاهية"]
row_y = y
bx = M
for t in gold_band:
    tw_ = ar_width(t, "Amiri-B", 7.3) + 24
    if bx + tw_ > W - M:
        row_y -= 23
        bx = M
    c.setFillColor(NAVY); c.roundRect(bx, row_y - 19, tw_, 16.5, 8.2, stroke=0, fill=1)
    draw_ar(c, bx + tw_ / 2, row_y - 13.5, t, font="Amiri-B", size=7.3, color=GOLD2, align="center")
    bx += tw_ + 6
y = row_y - 34
note_box(c, M, y, CW, 64, fill=NAVY, stroke=NAVY, radius=8)
diamond(c, W - M - 22, y - 16, 3.4, GOLD)
draw_ar(c, W - M - 34, y - 20, "خطوتُك الأولى — الليلة", font="Amiri-B", size=12, color=GOLD2, align="right")
draw_ar(c, W - M - 14, y - 40, "افتح perplexity.ai واسأله: «ما أفضل ٥ مهام في عملي يمكن أتمتتها بالذكاء الاصطناعي؟»", font="Amiri-B", size=9.5, color=PAPER, align="right")
draw_ar(c, W - M - 14, y - 55, "نفّذ نصفها هذا الأسبوع — النتيجة الأولى تخرج خلال ٣٠ دقيقة، لا ٣٠ يومًا", font="Amiri", size=8.5, color=HexColor("#C7D3DE"), align="right")
c.showPage()

# ============ PAGE 17 — CH.13 SUCCESS STORIES ============
chrome(c, 17, TOTAL)
y = section_banner(c, "١٣", "حين يعمل الذكاء: حالاتُ نجاح", "SUCCESS STORIES")
cases = [
    ("العلم", "SCIENCE", "AlphaFold — DeepMind", "تنبؤ ببنية أي بروتين من تسلسله الأحماضي", "200 مليون بنية بروتينية أُتيحت مجانًا للعلم — ونوبل كيمياء 2024", TEAL),
    ("النقل", "LOGISTICS", "UPS ORION", "خوارزمية تجميع طرق التسليم لكل سائق يوميًا", "~100 مليون ميل و~10 ملايين جالون وقود تُوفَّر كل سنة", GOLD),
    ("المال", "FINANCE", "AI @ Morgan Stanley", "مساعد ذكي يسترجع إجابات موثقة من 100 ألف وثيقة", "مستشارو الإدارة الثرية يجيبون في ثوانٍ — بلا هلوسة", NAVY),
    ("الترفيه", "ENTERTAINMENT", "Netflix Recommendation", "نموذج تنبؤ بذائقة كل مشترك على مستوى الفرد", "\u200E~80%\u200E من المشاهدة تأتي من التوصية — مليارات ساعات موفّرة", RED),
    ("الحكومة", "GOVERNMENT — EGYPT", "مصر 2026: من الاستراتيجية إلى التنفيذ", "الاستراتيجية الوطنية الثانية للذكاء الاصطناعي + المنصة الصناعية الرقمية", "مصر الأولى أفريقيًا في جاهزية AI الحكومية — وهدف $8B صادرات رقمية", GREEN),
]
card_h = 82
for i, (sector, sector_en, title, challenge, result, accent) in enumerate(cases):
    note_box(c, M, y, CW, card_h, fill=PAPER, stroke=LINE)
    c.setFillColor(accent); c.roundRect(M, y - card_h, 5, card_h, 2, stroke=0, fill=1)
    c.setFillColor(accent)
    c.roundRect(W - M - 64, y - 20, 52, 13, 6.5, stroke=0, fill=1)
    draw_ar(c, W - M - 38, y - 16, sector, font="Amiri-B", size=7.5, color=PAPER, align="center")
    draw_ar(c, W - M - 76, y - 16.5, title, font="Amiri-B", size=12, color=NAVY, align="right")
    letterspaced(c, M + 12, y - 16, sector_en, font="Amiri-B", size=5, color=GRAY, tracking=1.3, align="left")
    draw_ar(c, W - M - 18, y - 36, "التحدي:", font="Amiri-B", size=7.3, color=TEAL, align="right")
    bw = ar_width("التحدي:", "Amiri-B", 7.3)
    para_ar(c, M + 12, y - 36, challenge, font="Amiri", size=8, leading=11.5, max_w=CW - bw - 42, color=INK)
    draw_ar(c, W - M - 18, y - 56, "النتيجة:", font="Amiri-B", size=7.3, color=RED, align="right")
    para_ar(c, M + 12, y - 56, result, font="Amiri-B", size=8, leading=11.5, max_w=CW - 40, color=NAVY)
    y -= card_h + 8
note_box(c, M, y - 4, CW, 34, fill=CREAM, stroke=LINE)
draw_ar(c, W - M - 12, y - 16, "القاسمُ المشترك بين كل حالةٍ ناجحة:", font="Amiri-B", size=8.6, color=NAVY, align="right")
draw_ar(c, W - M - 12, y - 29, "بياناتٌ نظيفة + مسألةٌ محددة + مقياسُ نجاحٍ واضح — وليس «AI» بحد ذاته.", font="Amiri", size=8, color=INK, align="right")
y = y - 50
draw_ar(c, W - M, y, "أين تقف مؤسستك على منحنى نضج AI؟", font="Amiri-B", size=11, color=TEAL, align="right")
y -= 8
phases = [("الإنكار", "«الذكاء موضة ستمر»", GRAY), ("الاستكشاف", "«نجرب… لا نعرف بعد»", TEAL), ("التنفيذ", "«أداة في كل فريق»", STEEL), ("القياس والتوسع", "«AI جزء من قرار الشركة»", GOLD)]
pw = (CW - 3 * 8) / 4
for i, (t, d, col) in enumerate(phases):
    x0 = W - M - (i + 1) * pw - i * 8
    c.setFillColor(col)
    c.roundRect(x0, y - 54, pw, 54, 6, stroke=0, fill=1)
    draw_ar(c, x0 + pw - 8, y - 13, f"٠{i+1}", font="Amiri-B", size=10, color=PAPER, align="right")
    draw_ar(c, x0 + pw / 2, y - 28, t, font="Amiri-B", size=10.5, color=PAPER, align="center")
    para_ar(c, x0 + 5 + (pw - 10) / 2, y - 33, d, font="Amiri-I", size=6.7, leading=10, max_w=pw - 10, color=HexColor("#F2F5F8"), align="center")
    if i == 1:
        draw_ar(c, x0 + pw / 2, y - 64, "معظم المؤسسات العربية هنا", font="Amiri-B", size=7, color=RED, align="center")
c.showPage()
