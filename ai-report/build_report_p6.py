# -*- coding: utf-8 -*-
import sys; sys.path.insert(0, "/home/user/git/ai-report")
from report_lib import *
import math
ASSETS = "/home/user/git/ai-report/assets/"
CHARTS = "/home/user/git/ai-report/charts/"

# ============ PAGE 18 — CH.14 THE ROAD AHEAD ============
chrome(c, 18, TOTAL)
y = section_banner(c, "١٤", "المستقبل ٢٠٢٦–٢٠٣٥: عصرُ الوكلاء", "THE ROAD AHEAD")
img_cover_crop(c, ASSETS + "future_agi.jpg", M, y - 118, CW, 118, radius=8)
c.setFillColor(Color(0.03, 0.08, 0.15, alpha=0.32)); c.roundRect(M, y - 118, CW, 118, 8, stroke=0, fill=1)
draw_ar(c, W - M - 14, y - 24, "الفجرُ الذي تتسابق إليه البشرية جمعاء", font="Amiri-B", size=11.5, color=PAPER, align="right")
para_en(c, M + 12, y - 106, "From chatbots to agents that plan, act and verify — the defining decade of AI.", font="Amiri-I", size=7, color=HexColor("#E8EEF3"))
y = y - 134

c.drawImage(CHARTS + "chart_bench.png", M, y - 112, width=CW, height=112, preserveAspectRatio=False)
para_en(c, M, y - 117, "Fig. 5 — Frontier capability jumped in one year: SWE-bench Verified 60%→~98%; OSWorld 12%→66%. [4]", font="Amiri-I", size=6.6, color=GRAY)
y = y - 130

draw_ar(c, W - M, y, "خمسةُ تحوّلاتٍ تقود العقدَ القادم", font="Amiri-B", size=11, color=TEAL, align="right")
y -= 8
trends = [
    ("وكلاء الذكاء (Agentic AI)", "من روبوتات محادثة إلى منفذي مهام: ٣٣٪ من تطبيقات المؤسسات ستضم وكلاء بحلول 2028 (من \u200E<1%\u200E في 2024) — لكن أكثر من ٤٠٪ من مشاريع الوكلاء ستُلغى قبل 2027. [14]"),
    ("نماذج متخصصة وسيادية", "نماذج صغيرة رخيصة لكل قطاع ولغة — «سيادة النموذج» شرط استراتيجي للدول"),
    ("ذكاء على الجهاز (On-Device)", "خصوصية وسرعة صفر سحابة — في هاتفك وسيارتك ومصنعك"),
    ("الذكاء الفيزيائي: AI × روبوتات", "أذرع تفهم العالم لا تتبع قواعده — المصانع والجراحة والزراعة"),
    ("AI4Science: العلم الذاتي", "أدوية ومواد وطاقات جديدة تُكتشف بسرعةٍ لم يعرفها التاريخ (AlphaFold النموذج)"),
]
yy = y
for i, (t, d) in enumerate(trends):
    diamond(c, W - M - 4, yy - 5, 2.5, GOLD)
    draw_ar(c, W - M - 14, yy - 7, t, font="Amiri-B", size=8.8, color=NAVY, align="right")
    yy = para_ar(c, M, yy - 17.5, d, font="Amiri", size=7.2, leading=10.5, max_w=CW - 14, color=INK)
    yy -= 3.5
y = yy - 4

pred_rows = [
    ["الأفق", "ما نتوقعه"],
    ["2027", "الوكلاء معيارٌ في كل SaaS · أول أزمات تنظيمية كبرى · النماذج أرخص بـ 10× · نهاية عصر «النموذج الواحد للجميع»"],
    ["2030", "AI ≈ 14% من الناتج العالمي (~$15.7T) [17] · بنية تحتية تتجاوز $1T [15] · تعليم وقضاء وصحة معاد تصميمها بالذكاء"],
    ["2035", "اقتصادُ وكلاءٍ شبه مستقل · AGI موضوعٌ يومي لا أكاديمي · سؤال الحضارة: ما دور الإنسان حين تعمل الآلة؟"],
]
y = table_ar(c, M, y, [CW * 0.11, CW * 0.89], pred_rows, header_rows=1, size=7.3, pad=4.5)
y -= 12
c.setFillColor(GOLD); c.rect(M, y - 26, 4, 26, stroke=0, fill=1)
draw_ar(c, W - M - 12, y - 11, "«من يظن أن الذكاء الاصطناعي تقنيةٌ ستنتهي،", font="Amiri-BI", size=12, color=NAVY, align="right")
draw_ar(c, W - M - 12, y - 24, "كمن ظن أن الكهرباء مجرّد إضاءة»", font="Amiri-BI", size=12, color=NAVY, align="right")
c.showPage()

# ============ PAGE 19 — CH.15 FAQ & GLOSSARY ============
chrome(c, 19, TOTAL)
y = section_banner(c, "١٥", "أسئلةٌ شائعة + مسرد المصطلحات", "FAQ & GLOSSARY")

draw_ar(c, W - M, y, "ستُ أسئلةٍ يسألها الجميع", font="Amiri-B", size=11.5, color=TEAL, align="right")
y -= 8
faqs = [
    ("هل سيسرق الذكاء الاصطناعي وظيفتي؟", "الأرجح أن من يستخدم الذكاء بإتقان سيحل محل من لا يستخدمه — ليس العكس. 170 مليون وظيفة تُخلق مقابل 92 مليون تُزاح عالميًا (WEF) [8]. طوّر مهارتين متتاليتين: مهنتك + الذكاء."),
    ("كيف أبدأ من الصفر دون خبرة تقنية؟", "هذا بالضبط ما صُمم له الفصل 12: ٩٠ يومًا وثلاث مراحل. ابدأ بأدوات مجانية ومهمة حقيقية — التعلم بالممارسة لا بالمشاهدة."),
    ("ما الفرق بين ChatGPT وClaude وGemini؟", "كلها «نماذج لغوية عملاقة». تتنافس على نفس المقاعد: GPT أقوى انتشارًا، Claude أقوى في الكود والكتابة الطويلة، Gemini أقوى في الوسائط المتعددة ومنظومة Google. جرّب الثلاثة بمشروعٍ واحد واحكم بنفسك."),
    ("هل المحتوى المُولّد بالذكاء آمنٌ قانونيًا؟", "يتغير الوضع شهريًا. القاعدة الذهبية: أنت مسؤول عن كل ما تنشره. استخدم AI للمسودة، وراجع الحقائق، ولا تنتحل — القوانين تتشدد (EU AI Act وغرامات حتى 7% من الإيرادات) [20]."),
    ("كيف أتحقق من معلومة ذكرها الذكاء الاصطناعي؟", "اطلب المصدر، افتح المصدر، قارن بمصدرين آخرين. «واثقٌ وخاطئ» هي أخطر خصائص النماذج — والحل ليس ذكاءً أعلى بل عادة تحقق أقوى."),
    ("هل اللغة العربية ممثَّلة جيدًا في النماذج؟", "أقل من حقها بكثير — والفجوة فرصةٌ تجارية ضخمة. Qwen وLlama والنماذج العربية المتخصصة تتقدم سريعًا؛ من سيتقن «الذكاء بالعربية» سيقود السوق العربي [18]."),
]
for i, (q, a) in enumerate(faqs):
    draw_ar(c, W - M, y - 2, f"س{i+1} · {q}", font="Amiri-B", size=9.0, color=NAVY, align="right")
    y = para_ar(c, M, y - 16, a, font="Amiri", size=7.9, leading=12.0, max_w=CW - 8, color=INK)
    y -= 6.5
y -= 2

draw_ar(c, W - M, y, "مسردُ المصطلحات — عربي · English", font="Amiri-B", size=11.5, color=TEAL, align="right")
y -= 8
glossary = [
    ("الذكاء الاصطناعي", "Artificial Intelligence", "قدرة الآلة على محاكاة الذكاء البشري"),
    ("تعلّم الآلة", "Machine Learning", "التعلم من البيانات دون برمجة صريحة"),
    ("التعلّم العميق", "Deep Learning", "شبكات عصبية متعددة الطبقات"),
    ("النموذج اللغوي الكبير", "Large Language Model", "نموذج مدرّب على تريليونات الكلمات"),
    ("الذكاء التوليدي", "Generative AI", "ذكاء يُنشئ نصًا وصورًا لا يصنف فقط"),
    ("الهلوسة", "Hallucination", "اختلاق حقائق بثقة كاملة"),
    ("الوكيل الذكي", "Agent", "نموذج يخطط وينفذ ويتحقق من أهدافه"),
    ("RAG", "Retrieval-Augmented Generation", "تغذية النموذج بمصادر لحظة الإجابة"),
    ("الضبط الدقيق", "Fine-tuning", "إعادة تدريب النموذج لمجال محدد"),
    ("المواءمة", "Alignment", "جعل النموذج مفيدًا وآمنًا وصادقًا"),
    ("الشبكة العصبية", "Neural Network", "وحدات حسابية تحاكي الخلايا العصبية"),
    ("المعيار القياسي", "Benchmark", "اختبار موحد لمقارنة النماذج"),
]
col_w = (CW - 10) / 2
for i, (a, e, d) in enumerate(glossary):
    col = 0 if i % 2 == 0 else 1
    row = i // 2
    x0 = M + (CW - col_w) if col == 0 else M
    yy = y - row * 24.5
    c.setFillColor(CREAM if row % 2 == 0 else PAPER)
    c.roundRect(x0, yy - 23.5, col_w, 23.5, 3.5, stroke=0, fill=1)
    draw_ar(c, x0 + col_w - 6, yy - 9, a, font="Amiri-B", size=7.7, color=NAVY, align="right")
    letterspaced(c, x0 + 6, yy - 8.5, e.upper(), font="Amiri-B", size=4.4, color=TEAL, tracking=0.6, align="left")
    para_ar(c, x0 + 6, yy - 13, d, font="Amiri", size=6.4, leading=9, max_w=col_w - 12, color=GRAY)
y = y - 6 * 27 - 18
note_box(c, M, y, CW, 58, fill=NAVY, stroke=NAVY, radius=8)
diamond(c, W - M - 20, y - 14, 3.2, GOLD)
draw_ar(c, W - M - 30, y - 18, "ما زلت محتارًا؟", font="Amiri-B", size=11, color=GOLD2, align="right")
draw_ar(c, W - M - 14, y - 36, "اكتب للذكاء الاصطناعي: «اشرح لي تعلّم الآلة بمثال من عملي كمبتدئ»", font="Amiri-B", size=9, color=PAPER, align="right")
draw_ar(c, W - M - 14, y - 50, "ثم عُد إلى هذه الفصول كمواد إعادة لا كبداية — الفارق هائل", font="Amiri", size=8, color=HexColor("#C7D3DE"), align="right")
c.showPage()

# ============ PAGE 20 — CONCLUSION & REFERENCES ============
chrome(c, 20, TOTAL)
y = H - 72
letterspaced(c, W - M, y, "CLOSING", font="Amiri-B", size=6.8, color=TEAL, tracking=3, align="right")
y -= 8
draw_ar(c, W - M, y - 24, "كلمةٌ أخيرة", font="Amiri-B", size=27, color=NAVY, align="right")
c.setStrokeColor(GOLD); c.setLineWidth(2.4); c.line(W - M, y - 42, W - M - 74, y - 42)
y -= 62
y = para_ar(c, M, y, "كل تقنيةٍ عظيمة في التاريخ — النار، الطباعة، الكهرباء، الإنترنت — بدأت كفرضيةٍ مريبة وانتهت كهواءٍ نتنفسه دون أن نشعر. الذكاء الاصطناعي يقطع هذه الرحلة بسرعةٍ لم تعرفها أي تقنيةٌ قبله: ثلاث سنوات فقط فصلت بين لحظة الإطلاق والانتشار الشامل.", font="Amiri", size=10.5, leading=19.5, color=INK)
y -= 4
y = para_ar(c, M, y, "نحن لا نعيش نهاية البشر، بل بداية شراكةٍ غير مسبوقة بين العقل البشري والآلة: من يُحسّن من؟ والإجابة الصادقة: كلاهما يحسّن الآخر — بشرط أن ندخل هذه الشراكة أعينَنا مفتوحة، وحدودَنا أخلاقية، وشجاعتَنا عملية.", font="Amiri", size=10.5, leading=19.5, color=INK)
y -= 4
y = para_ar(c, M, y, "رسالتُنا لك قارئًا عربيًا: هذه ليست موجةً أمريكية أو صينية تشاهدها من الشرفة — مصر والأمة العربية تملك المواهب والموقع والسوق. القطار يتحرك الآن، وأنت — بسؤالك هذا البحث — على الرصيف الصحيح. اركب.", font="Amiri-B", size=10.5, leading=19.5, color=NAVY)
y -= 12

draw_ar(c, W - M, y, "المراجع والمصادر — 20 مصدرًا موثقًا", font="Amiri-B", size=11, color=TEAL, align="right")
y -= 10
refs = [
    "Grand View Research — Artificial Intelligence Market Size & Share Report, 2026–2033. grandviewresearch.com/industry-analysis/artificial-intelligence-ai-market",
    "MarketsandMarkets — Artificial Intelligence Market Report 2026–2033. marketsandmarkets.com",
    "ArticSledge — AI Market Size 2026: $376B–$900B Estimates Explained (Fortune BI · GVR · Statista · Precedence · Gartner · IDC). articsledge.com/post/ai-market-size",
    "Stanford Institute for Human-Centered AI — AI Index Report 2026 (adoption 88% · $581.7B corporate investment · 53% GenAI penetration · SWE-bench · OSWorld · $285.9B US private funding · Singapore 61% · UAE 54% · -20% junior devs). Via smarterx.ai · dapta.ai · businessmodelanalyst.com · relvai.com (Apr–Jun 2026)",
    "Relvai — AI Enterprise Adoption 2026: 12 Key Findings from Stanford's Index Report. relvai.com (Apr 2026)",
    "PwC — Sizing the Prize: What's the Real Value of AI for Your Business and How Can You Capitalise? ($15.7T by 2030).",
    "McKinsey Global Institute — The Economic Potential of Generative AI: The Next Productivity Frontier ($2.6–4.4T/yr · 63 use cases · 60–70% time automatable). (Jun 2025 / Jan 2026 reprints)",
    "World Economic Forum — Future of Jobs Report 2025 (170M created · 92M displaced · +78M net · 39% core skills change).",
    "International Monetary Fund — AI Will Transform the Global Economy (Jan 2024); Managing Director's 40%-of-jobs warning, Oct 2026. technext24.com",
    "Oxford Insights — Government AI Readiness Index (Egypt: #1 in Africa). Via Tech X Media Arabic, Jan 2026.",
    "Fintech Gate — «سوق الذكاء الاصطناعي في مصر يصل إلى 5.1 مليار دولار بحلول 2031» — م. محمد نجاتي. fintechgate.net (5 Nov 2026)",
    "بوابة الأهرام / Fixed Solutions — «30.87 مليار دولار حجم سوق AI والأمن السيبراني والبيانات في MEA خلال 2026». gate.ahram.org.eg (14 Mar 2026)",
    "Menlo Ventures — The State of Generative AI in the Enterprise 2025 ($37B · 3.2× YoY). Via report-ai.org (Jun 2026)",
    "Gartner — Hype Cycle for Agentic AI 2026; 33% of enterprise apps by 2028 · >40% of agentic projects canceled by 2027. Via report-ai.org",
    "IDC — Worldwide AI infrastructure spending: $487B in 2026 (+53%), to exceed $1T by 2029. Via report-ai.org",
    "JobRoute — AI and Jobs in 2026: What the Data Actually Says (WEF · McKinsey · IMF synthesis). jobroute.ai (4 Jun 2026)",
    "اليوم السابع — «مصر تستهدف تحويل الذكاء الاصطناعي إلى محرك للنمو الاقتصادي» — الاستراتيجية الوطنية الثانية للذكاء الاصطناعي. youm7.com (3 Nov 2026)",
    "Tech X Media Arabic — «الاستراتيجية الرقمية في مصر تدفع الاستثمارات في بنية الذكاء الاصطناعي» ($1.5T لناتج أفريقيا · AI Everything MEA Egypt · 750 ألف خريج). techxmediaarabic.com (21 Jan 2026)",
    "EgyIn — «مستقبل الصناعة الرقمية في مصر 2026.. التكنولوجيا والـAI المحرك الرئيسي للنمو» ($8B صادرات رقمية · المنصة الصناعية الرقمية). egyin.com (10 Sep 2026)",
    "Regulation (EU) 2024/1689 — Artificial Intelligence Act. artificialintelligenceact.eu",
]
ref_lines = []
for i, r in enumerate(refs, 1):
    ref_lines.append(f"[{i}]  {r}")
col_w2 = (CW - 18) / 2
half_refs = 10
for i, line in enumerate(ref_lines):
    col = 0 if i < half_refs else 1
    row = i if i < half_refs else i - half_refs
    x0 = M + (CW - col_w2) if col == 0 else M
    yy = y - row * 30.5
    draw_ar(c, x0 + 14, yy - 4, f"[{i+1}]", font="Amiri-B", size=6.4, color=GOLD if False else TEAL, align="left")
    para_en(c, x0 + 22, yy, line[4:], font="Amiri", size=5.9, leading=8.6, max_w=col_w2 - 26, color=GRAY)
y = y - half_refs * 30.5 - 4

# colophon
note_box(c, M, y, CW, 88, fill=NAVY, stroke=NAVY, radius=8)
diamond(c, W / 2, y - 12, 4, GOLD)
draw_ar(c, W / 2, y - 30, "صُنع في مصر — لكل قارئ عربي يحلم بغدٍ أذكى", font="Amiri-B", size=10, color=GOLD2, align="center")
draw_ar(c, W / 2, y - 48, "أُعِدَّ هذا التقريرُ في نوفمبر ٢٠٢٦ · الأرقام كما وردت في مصادرها وقت الإعداد · الآراء لا تمثل جهةً بعينها", font="Amiri", size=7.6, color=HexColor("#C7D3DE"), align="center")
letterspaced(c, W / 2, y - 66, "AI RESEARCH DESK · FIRST EDITION · 2026", font="Amiri-B", size=6, color=TEAL2, tracking=2.2, align="center")
draw_ar(c, W / 2, y - 81, "— FIN —", font="Amiri-B", size=8, color=GRAY, align="center")
c.showPage()

c.save()
print("PDF saved.")
