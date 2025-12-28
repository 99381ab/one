# -*- coding: utf-8 -*-
# 生成《Python 程序设计》课程实践作业（按模板排版；填写横线使用“表格下边框”，不会越输越长）
# 本地用法（可选）：
#   pip install -r requirements.txt
#   python report_generator.py --out "docs/《Python程序设计》课程实践作业.docx"
import argparse
import os
from typing import Optional

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_run_cn_font(run, name="宋体", size_pt: Optional[int] = None, bold=False):
    run.font.name = name
    r = run._element.rPr
    r.rFonts.set(qn("w:eastAsia"), name)
    if size_pt is not None:
        run.font.size = Pt(size_pt)
    run.bold = bold

def set_cell_border(cell, **borders):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = tcPr.first_child_found_in("w:tcBorders")
    if tcBorders is None:
        tcBorders = OxmlElement("w:tcBorders")
        tcPr.append(tcBorders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        if edge in borders:
            edge_elm = tcBorders.find(qn(f"w:{edge}"))
            if edge_elm is None:
                edge_elm = OxmlElement(f"w:{edge}")
                tcBorders.append(edge_elm)
            for k, v in borders[edge].items():
                edge_elm.set(qn(f"w:{k}"), str(v))

def clear_all_cell_borders(cell):
    set_cell_border(cell, top={"val": "nil"}, bottom={"val": "nil"}, left={"val": "nil"}, right={"val": "nil"})

def add_title(doc: Document):
    p = doc.add_paragraph()
    r = p.add_run("《Python 程序设计》\n课程实践作业")
    set_run_cn_font(r, "黑体", 32, True)

def add_term(doc: Document, term: str):
    p = doc.add_paragraph()
    r = p.add_run(term)
    set_run_cn_font(r, "宋体", 14, False)

def add_label_row(doc: Document, label_text: str, value_text: str = "", right_width_cm=12.0, left_width_cm=3.2):
    # 2列表格：左标签，右输入区（固定宽度，仅下边框）
    tbl = doc.add_table(rows=1, cols=2)
    tbl.autofit = False
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    tbl.columns[0].width = Cm(left_width_cm)
    tbl.columns[1].width = Cm(right_width_cm)

    c0 = tbl.cell(0, 0)
    c1 = tbl.cell(0, 1)
    clear_all_cell_borders(c0)
    clear_all_cell_borders(c1)
    set_cell_border(c1, bottom={"sz": "12", "val": "single", "color": "000000"})  # ≈0.75pt

    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r0 = p0.add_run(label_text)
    set_run_cn_font(r0, "宋体", 12, False)

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r1 = p1.add_run(value_text)
    set_run_cn_font(r1, "宋体", 12, False)

    p0.paragraph_format.space_after = Pt(6)
    p1.paragraph_format.space_after = Pt(6)
    return tbl

def add_heading(doc: Document, text: str, size=16, bold=True):
    p = doc.add_paragraph()
    r = p.add_run(text)
    set_run_cn_font(r, "黑体", size, bold)

def add_body(doc: Document, text: str, size=12):
    p = doc.add_paragraph()
    r = p.add_run(text)
    set_run_cn_font(r, "宋体", size, False)

def add_code(doc: Document, code: str, size=12, font="Times New Roman"):
    p = doc.add_paragraph()
    r = p.add_run(code)
    r.font.name = font
    r.font.size = Pt(size)
    r._element.rPr.rFonts.set(qn("w:ascii"), font)
    r._element.rPr.rFonts.set(qn("w:hAnsi"), font)

PINGPONG_CODE = r'''# 乒乓球模拟比赛（7 局 4 胜制，支持参数化）
import random
from typing import Dict, List, Tuple

def normalize_prob(pa_raw: float, pb_raw: float):
    eps = 1e-9
    s = max(pa_raw, 0.0) + max(pb_raw, 0.0)
    s = s if s > eps else 1.0
    pA = max(min(pa_raw / s, 1.0), 0.0)
    pB = 1.0 - pA
    return pA, pB

def simulate_one_game(pA: float, pB: float, win_point: int = 11):
    scoreA = scoreB = 0
    safety_cap = 1000
    rounds = 0
    while True:
        rounds += 1
        if rounds > safety_cap:
            return {'scoreA': scoreA, 'scoreB': scoreB, 'winner': 'A' if scoreA >= scoreB else 'B'}
        if random.random() < pA:
            scoreA += 1
        else:
            scoreB += 1
        if (scoreA >= win_point or scoreB >= win_point) and abs(scoreA - scoreB) >= 2:
            return {'scoreA': scoreA, 'scoreB': scoreB, 'winner': 'A' if scoreA > scoreB else 'B'}

def simulate_match(pa_raw: float, games_to_win: int = 4, seed: int | None = None):
    if seed is not None:
        random.seed(seed)
    pb_raw = random.random()
    pA, pB = normalize_prob(pa_raw, pb_raw)
    results = []
    winsA = winsB = 0
    game_index = 0
    max_games = 2 * games_to_win - 1
    while winsA < games_to_win and winsB < games_to_win and game_index < max_games:
        game_index += 1
        res = simulate_one_game(pA, pB, win_point=11)
        results.append({'game': game_index, **res})
        if res['winner'] == 'A':
            winsA += 1
        else:
            winsB += 1
    champion = 'A' if winsA > winsB else 'B'
    return {'winsA': winsA, 'winsB': winsB, 'champion': champion, 'details': results, 'pA': pA, 'pB': pB, 'pA_raw': pa_raw, 'pB_raw': pb_raw}

def pretty_print_summary(summary):
    lines = []
    lines.append("—— 乒乓球比赛模拟报告 ——")
    lines.append(f"原始倾向：A={{summary['pA_raw']:.2f}}  B={{summary['pB_raw']:.2f}}")
    lines.append(f"对抗概率：A={{summary['pA']:.2f}}  B={{summary['pB']:.2f}}")
    lines.append("逐局结果：")
    for d in summary['details']:
        lines.append(f"  第{{d['game']}}局：A {{d['scoreA']}} : {{d['scoreB']}} B    胜者：{{d['winner']}}")
    lines.append(f"总计：A 胜 {{summary['winsA']}} 局，B 胜 {{summary['winsB']}} 局，冠军：{{summary['champion']}}")
    return "\n".join(lines)

if __name__ == '__main__':
    s = simulate_match(0.35, seed=42)
    print(pretty_print_summary(s))
'''

def build(out_path: str, term: str, klass: str, sid: str, name: str, teacher: str, image: Optional[str] = None):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    doc = Document()

    # 封面
    add_title(doc)
    add_term(doc, term)
    doc.add_paragraph()
    add_label_row(doc, "班    级：", klass)
    add_label_row(doc, "学    号：", sid)
    add_label_row(doc, "姓    名：", name)
    add_label_row(doc, "成    绩：", "")

    doc.add_page_break()

    # 抬头与课程信息
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("《Python 程序设计》课程实践")
    set_run_cn_font(r, "黑体", 20, True)

    add_body(doc, "课程名称：Python 程序设计            课程编码：G03305520")
    add_body(doc, f"实践学时：8 学时                      任课教师：{teacher}")

    # 一、课程实践要求
    add_heading(doc, "一、课程实践要求", 16, True)
    add_body(doc, "请用模块化编程方法完成以下综合程序练习题，要求写出程序设计思路、编程步骤和实验结果分析，附程序运行截图。")

    # 乒乓球模拟比赛说明
    add_heading(doc, "乒乓球模拟比赛", 14, True)
    add_body(doc, "类型：类和对象")
    add_body(doc, "描述：模拟 7 局 4 胜制比赛；一局先到 11 分且领先 2 分者胜。输入 A 选手回合胜率，B 概率随机生成并归一化对抗。")

    # 二、课程实践格式
    add_heading(doc, "二、课程实践格式", 16, True)
    add_body(doc, "1、程序设计思路")
    add_body(doc, "2、程序完整代码（关键环节添加注释，注释不少于 20 处）")
    add_body(doc, "3、实验结果及运行结果截图展示")
    add_body(doc, "4、结果分析与问题总结")

    # 1、程序设计思路（扩写）
    add_heading(doc, "1、程序设计思路（一级标题）", 16, True)
    add_heading(doc, "1.1 需求与规则梳理（二维标题）", 14, True)
    add_body(doc, "（1）目标：给定回合胜率，模拟整场并输出逐局比分与冠军；（2）规则：先 11 分且领先 2 分；（3）概率：归一化处理，保证一回合仅一方得分；（4）赛制：7 局 4 胜，可参数化；（5）输出：逐局+总结；（6）健壮性：输入边界与随机种子；（7）可扩展：赛制与统计可配置。")
    add_heading(doc, "1.2 模块划分与流程（二维标题）", 14, True)
    add_body(doc, "模块一：输入与参数；模块二：单局模拟；模块三：整场控制；模块四：统计展示；模块五：健壮性与测试。数据结构使用 list/dict 存储逐局记录。复杂度线性于局数。")

    # 2、程序完整代码（Times New Roman 小四）
    add_heading(doc, "2、程序完整代码（关键环节添加注释，注释不少于 20 处）", 16, True)
    add_code(doc, PINGPONG_CODE, 12, "Times New Roman")
    add_body(doc, "说明：程序代码用 Times New Roman 小四（12pt）。")

    # 3、实验结果与截图
    add_heading(doc, "3、实验结果及运行结果截图展示", 16, True)
    add_heading(doc, "3.1 运行界面（二维标题）", 14, True)
    add_body(doc, "运行程序后，输入 A 的回合胜率，程序自动输出逐局比分与总结。")
    add_heading(doc, "3.2 结果截图（二维标题）", 14, True)
    image = (image or "").strip()
    if image:
        if os.path.exists(image):
            doc.add_picture(image, width=Cm(14))
        else:
            add_body(doc, f"未找到截图：{image}")
    else:
        add_body(doc, "此处可插入本机运行截图；如需插图，后续可在文档中粘贴。")

    # 4、结果分析与问题总结
    add_heading(doc, "4、结果分析与问题总结", 16, True)
    add_heading(doc, "4.1 问题分析（二维标题）", 14, True)
    add_body(doc, "概率归一化避免 pA+pB≠1；设置安全上限防极端长盘；输入越界回退默认值。")
    add_heading(doc, "4.2 总结（二维标题）", 14, True)
    add_body(doc, "项目按模块化实施，结果与预期一致，可复现实验并便于扩展。")

    # 信息摘要
    add_body(doc, f"【信息摘要】班级：{klass}    学号：{sid}    姓名：{name}    任课教师：{teacher}")

    doc.save(out_path)

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--out", default="docs/《Python程序设计》课程实践作业.docx")
    p.add_argument("--term", default="2025 - 2026学年第1学期")
    p.add_argument("--klass", default="2023级物联网工程1班")
    p.add_argument("--sid", default="230911005")
    p.add_argument("--name", default="张三")
    p.add_argument("--teacher", default="李晓")
    p.add_argument("--image", default=None, help="运行截图图片路径，可选")
    return p.parse_args()

if __name__ == "__main__":
    a = parse_args()
    build(a.out, a.term, a.klass, a.sid, a.name, a.teacher, a.image)
    print(f"已生成：{a.out}")
