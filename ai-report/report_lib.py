# -*- coding: utf-8 -*-
"""Shared helpers + brand system for the AI research report (A4, RTL Arabic + English)."""
import math
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.utils import ImageReader
import arabic_reshaper
from bidi.algorithm import get_display

W, H = A4  # 595.27 x 841.89 pt
M = 46                      # side margin
CW = W - 2 * M              # content width

# ---------- Brand palette ----------
NAVY      = HexColor("#0F2740")
DEEP      = HexColor("#0A1A2B")
NAVY2     = HexColor("#1C3B57")
STEEL     = HexColor("#33506E")
TEAL      = HexColor("#0E7C86")
TEAL2     = HexColor("#2EC4B6")
TEALPALE  = HexColor("#E4F1F0")
GOLD      = HexColor("#D9A441")
GOLD2     = HexColor("#E9C46A")
GOLDPALE  = HexColor("#FBF3DE")
INK       = HexColor("#22313F")
GRAY      = HexColor("#62758A")
LINE      = HexColor("#D9E1E8")
PAPER     = HexColor("#FFFFFF")
CREAM     = HexColor("#F8F6EF")
RED       = HexColor("#C4572E")
GREEN     = HexColor("#1F7A4D")

# ---------- Fonts (Amiri = Arabic + elegant Latin) ----------
FDIR = "/home/user/git/ai-report/fonts/"
pdfmetrics.registerFont(TTFont("Amiri",  FDIR + "Amiri-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Amiri-B", FDIR + "Amiri-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Amiri-I", FDIR + "Amiri-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Amiri-BI", FDIR + "Amiri-BoldItalic.ttf"))

def ar(t):
    """Shape + bidi-reorder any (mixed) text for rendering."""
    return get_display(arabic_reshaper.reshape(str(t)))

def ar_width(t, font, size):
    return pdfmetrics.stringWidth(ar(t), font, size)

def draw_ar(c, anchor_x, y, t, font="Amiri", size=11, color=INK, align="right"):
    """Draw a single RTL line. align: right (anchor=right edge) | left | center."""
    s = ar(t)
    c.setFont(font, size)
    c.setFillColor(color)
    w = pdfmetrics.stringWidth(s, font, size)
    if align == "right":
        c.drawString(anchor_x - w, y, s)
    elif align == "left":
        c.drawString(anchor_x, y, s)
    else:
        c.drawCentredString(anchor_x, y, s)
    return w

def wrap_ar(t, font, size, max_w):
    words = str(t).split()
    lines, cur = [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if not cur or ar_width(trial, font, size) <= max_w:
            cur = trial
        else:
            lines.append(cur); cur = w_
    if cur:
        lines.append(cur)
    return lines

def para_ar(c, x, y_top, t, font="Amiri", size=10.5, leading=17, max_w=CW, color=INK, align="right"):
    y = y_top
    for line in wrap_ar(t, font, size, max_w):
        draw_ar(c, x + max_w if align == "right" else x, y - size, line, font=font, size=size, color=color, align=align)
        y -= leading
    return y

def para_en(c, x, y_top, t, font="Amiri", size=8.5, leading=13.5, max_w=CW, color=GRAY, align="left"):
    """Paragraph for English text; ar() is identity on pure Latin, so mixed lines shape correctly too."""
    words = str(t).split()
    lines, cur = [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if not cur or pdfmetrics.stringWidth(ar(trial), font, size) <= max_w:
            cur = trial
        else:
            lines.append(cur); cur = w_
    if cur:
        lines.append(cur)
    y = y_top
    c.setFont(font, size); c.setFillColor(color)
    for line in lines:
        if align == "left":
            c.drawString(x, y - size, ar(line))
        elif align == "right":
            c.drawRightString(x + max_w, y - size, ar(line))
        else:
            c.drawCentredString(x + max_w / 2, y - size, ar(line))
        y -= leading
    return y

def letterspaced(c, x, y, t, font="Amiri-B", size=8, color=GRAY, tracking=2.0, align="left"):
    if any("\u0600" <= ch <= "\u06FF" for ch in str(t)):
        # Arabic glyphs must not be drawn one-by-one; fall back to shaped line
        return draw_ar(c, x, y, t, font=font, size=size * 1.15, color=color, align=("right" if align == "right" else ("center" if align == "center" else "left")))
    c.setFont(font, size); c.setFillColor(color)
    total = sum(pdfmetrics.stringWidth(ch, font, size) + tracking for ch in t) - tracking
    if align == "right":
        start = x - total
    elif align == "center":
        start = x - total / 2
    else:
        start = x
    cx = start
    for ch in t:
        c.drawString(cx, y, ch)
        cx += pdfmetrics.stringWidth(ch, font, size) + tracking

# ---------- Page chrome ----------
def chrome(c, page_no, total, section_ar="", section_en=""):
    # header
    letterspaced(c, M, H - 34, "AI RESEARCH REPORT · 2026", font="Amiri-B", size=6.6, color=GRAY, tracking=2.2, align="left")
    draw_ar(c, W - M, H - 33, "تقريرُ الذكاءِ الاصطناعيّ", font="Amiri-B", size=10.5, color=NAVY, align="right")
    c.setStrokeColor(GOLD); c.setLineWidth(1.6)
    c.line(M, H - 44, W - M, H - 44)
    c.setStrokeColor(LINE); c.setLineWidth(0.6)
    c.line(M, H - 47.5, W - M, H - 47.5)
    # footer
    c.setStrokeColor(LINE); c.setLineWidth(0.7)
    c.line(M, 46, W - M, 46)
    draw_ar(c, W - M, 31, "الذكاء الاصطناعي — بحثٌ شامل · ٢٠٢٦", font="Amiri", size=8, color=GRAY, align="right")
    letterspaced(c, M, 31.5, "AR · EN — NOV 2026", font="Amiri-B", size=6.2, color=GRAY, tracking=2.0, align="left")
    c.setFillColor(GOLD)
    c.saveState(); c.translate(W / 2, 35.5); c.rotate(45); c.rect(-3.4, -3.4, 6.8, 6.8, stroke=0, fill=1); c.restoreState()
    draw_ar(c, W / 2 - 14, 31.5, f"{page_no:02d}", font="Amiri-B", size=8.5, color=NAVY, align="right")
    letterspaced(c, W / 2 + 12, 32, f"/ {total:02d}", font="Amiri-B", size=7, color=GRAY, tracking=1.5, align="left")

def section_banner(c, chips, ar_title, en_title, y_top=None):
    """Chapter banner: navy chip (Arabic-Indic number) + AR title + EN small caps. Returns next y."""
    y = (y_top or H - 64)
    chip = 46
    cx = W - M - chip
    c.setFillColor(NAVY)
    c.roundRect(cx, y - chip, chip, chip, 7, stroke=0, fill=1)
    c.setStrokeColor(GOLD); c.setLineWidth(1.4)
    c.roundRect(cx, y - chip, chip, chip, 7, stroke=1, fill=0)
    draw_ar(c, cx + chip / 2, y - chip / 2 - 8.5, chips, font="Amiri-B", size=17, color=GOLD2, align="center")
    draw_ar(c, cx - 14, y - 17, "الفصل " + chips, font="Amiri", size=8, color=GRAY, align="right")
    draw_ar(c, cx - 14, y - 37, ar_title, font="Amiri-B", size=20.5, color=NAVY, align="right")
    letterspaced(c, M, y - 34, en_title, font="Amiri-B", size=6.0, color=TEAL, tracking=1.15, align="left")
    c.setStrokeColor(GOLD); c.setLineWidth(2.4)
    c.line(W - M, y - chip - 10, W - M - 74, y - chip - 10)
    c.setStrokeColor(TEAL2); c.setLineWidth(1.0)
    c.line(W - M - 78, y - chip - 10, W - M - 176, y - chip - 10)
    return y - chip - 22

def note_box(c, x, y_top, w, h, fill=CREAM, stroke=LINE, radius=6):
    c.setFillColor(fill); c.setStrokeColor(stroke); c.setLineWidth(0.8)
    c.roundRect(x, y_top - h, w, h, radius, stroke=1, fill=1)

def stat_card(c, x, y_top, w, h, big, label_ar, sub_en="", big_color=TEAL, fill=PAPER, stroke=LINE):
    c.setFillColor(fill); c.setStrokeColor(stroke); c.setLineWidth(0.9)
    c.roundRect(x, y_top - h, w, h, 6, stroke=1, fill=1)
    c.setStrokeColor(GOLD); c.setLineWidth(2.0)
    c.line(x + 14, y_top - 2.2, x + 54, y_top - 2.2)
    draw_ar(c, x + w / 2, y_top - 26, big, font="Amiri-B", size=20, color=big_color, align="center")
    ly = y_top - 40
    for line in wrap_ar(label_ar, "Amiri-B", 7.9, w - 14)[:2]:
        draw_ar(c, x + w / 2, ly, line, font="Amiri-B", size=7.9, color=INK, align="center")
        ly -= 10.5
    if sub_en:
        letterspaced(c, x + w / 2, y_top - h + 6.5, sub_en, font="Amiri-B", size=4.6, color=GRAY, tracking=0.7, align="center")

def img_cover_crop(c, path, x, y, w, h, radius=0):
    """Draw image filling (x, y, w, h), center-cropped to the box."""
    ir = ImageReader(path)
    iw, ih = ir.getSize()
    box_ratio = w / h
    img_ratio = iw / ih
    if img_ratio > box_ratio:   # image wider -> crop sides
        draw_h = h
        draw_w = h * img_ratio
        dx = x - (draw_w - w) / 2
        dy = y
    else:                        # image taller -> crop top/bottom
        draw_w = w
        draw_h = w / img_ratio
        dx = x
        dy = y - (draw_h - h) / 2
    c.saveState()
    p = c.beginPath()
    if radius:
        p.roundRect(x, y, w, h, radius)
    else:
        p.rect(x, y, w, h)
    c.clipPath(p, stroke=0, fill=0)
    c.drawImage(ir, dx, dy, width=draw_w, height=draw_h)
    c.restoreState()

def table_ar(c, x, y_top, col_ws, rows, header_rows=1, font="Amiri", size=8.6,
             header_fill=NAVY, header_color=PAPER, zebra=True, pad=5.5, align_center=True):
    """RTL-friendly table; columns laid left->right as given (pass visual order). Returns next y."""
    leading = size * 1.45
    # pre-wrap
    wrapped, heights = [], []
    for r, row in enumerate(rows):
        is_head = r < header_rows
        fnt = "Amiri-B" if is_head else font
        row_cells, max_lines = [], 1
        for ci, cell in enumerate(row):
            lines = wrap_ar(cell, fnt, size, col_ws[ci] - 2 * pad) if not (align_center and False) else wrap_ar(cell, fnt, size, col_ws[ci] - 2 * pad)
            row_cells.append(lines)
            max_lines = max(max_lines, len(lines))
        wrapped.append(row_cells)
        heights.append(max_lines * leading + 2 * pad)
    total_w = sum(col_ws)
    y = y_top
    for r, row in enumerate(rows):
        is_head = r < header_rows
        rh = heights[r]
        # background
        if is_head:
            c.setFillColor(header_fill)
        elif zebra and (r - header_rows) % 2 == 1:
            c.setFillColor(CREAM)
        else:
            c.setFillColor(PAPER)
        c.rect(x, y - rh, total_w, rh, stroke=0, fill=1)
        # vertical separators
        c.setStrokeColor(LINE); c.setLineWidth(0.5)
        # text
        cx = x
        fnt = "Amiri-B" if is_head else font
        tcol = header_color if is_head else INK
        c.setFont(fnt, size)
        c.setFillColor(tcol)
        for ci, cell in enumerate(row):
            ty = y - pad - size
            for line in wrapped[r][ci]:
                s = ar(line)
                wline = pdfmetrics.stringWidth(s, fnt, size)
                if align_center:
                    c.drawString(cx + (col_ws[ci] - wline) / 2, ty, s)
                else:
                    c.drawString(cx + col_ws[ci] - pad - wline, ty, s)
                ty -= leading
            cx += col_ws[ci]
        y -= rh
    # frame + inner verticals
    table_h = y_top - y
    c.setStrokeColor(LINE); c.setLineWidth(1.0)
    c.rect(x, y, total_w, table_h, stroke=1, fill=0)
    cx = x
    for w_ in col_ws[:-1]:
        cx += w_
        c.setStrokeColor(LINE); c.setLineWidth(0.5)
        c.line(cx, y, cx, y_top)
    # header separator
    hh = sum(heights[:header_rows])
    c.setStrokeColor(GOLD); c.setLineWidth(1.6)
    c.line(x, y_top - hh, x + total_w, y_top - hh)
    return y

def diamond(c, x, y, s=4, color=GOLD):
    c.setFillColor(color)
    c.saveState(); c.translate(x, y); c.rotate(45); c.rect(-s, -s, 2*s, 2*s, stroke=0, fill=1); c.restoreState()

def to_arabic_indic(n):
    return str(n).translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))
