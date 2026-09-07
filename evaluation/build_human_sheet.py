# -*- coding: utf-8 -*-
"""从 raw 结果生成 A/B 盲评 Excel
用法：python build_human_sheet.py <结果目录> <模型A> <模型B>
产出 <结果目录>/人工评分表.xlsx（sheets：评分表 / 汇总 / 评分说明）
依赖：pip install openpyxl"""
import json, sys
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

results_dir, model_a, model_b = Path(sys.argv[1]), sys.argv[2], sys.argv[3]
raw = results_dir / "raw"
items = {json.loads(l)["id"]: json.loads(l)
         for l in (Path(__file__).parent / "dataset" / "star_eval_v1.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()}

wb = Workbook()
ws = wb.active
ws.title = "评分表"
ws.append(["编号", "维度", "题目/任务", "回答A", "回答B", "评分A(0-10)", "评分B(0-10)", "备注(优缺点)"])
for c in range(1, 9):
    ws.cell(1, c).font = Font(bold=True, color="FFFFFF")
    ws.cell(1, c).fill = PatternFill("solid", fgColor="4472C4")
    ws.column_dimensions[get_column_letter(c)].width = [8, 12, 40, 60, 60, 12, 12, 30][c - 1]

dv = DataValidation(type="whole", operator="between", formula1="0", formula2="10",
                    showErrorMessage=True, errorTitle="0-10整数", error="请输入0-10的整数")
ws.add_data_validation(dv)


def load(mid, iid):
    f = raw / mid / f"{iid}.json"
    if not f.exists():
        return "(缺失)"
    return "\n\n".join(r["content"] for r in json.loads(f.read_text(encoding="utf-8"))["answer"]["rounds"])


row = 2
for iid, item in items.items():
    q = item.get("instruction") or " / ".join(t["content"] for t in item["multi_round"])
    ws.append([iid, item["dimension"], q[:200], load(model_a, iid), load(model_b, iid), None, None, None])
    dv.add(f"F{row}:G{row}")
    for c in (3, 4, 5):
        ws.cell(row, c).alignment = Alignment(wrap_text=True, vertical="top")
    row += 1

ws2 = wb.create_sheet("汇总")
ws2.append(["模型", "总均分", "知识问答", "逻辑推理", "代码生成", "安全合规", "中文特性", "多轮上下文"])
for i, mid in enumerate([model_a, model_b]):
    col = "F" if i == 0 else "G"
    ws2.append([mid, f"=ROUND(AVERAGE(评分表!{col}2:{col}{row-1}),2)",
                f'=ROUND(AVERAGEIF(评分表!B2:B{row-1},"知识问答",评分表!{col}2:{col}{row-1}),2)',
                f'=ROUND(AVERAGEIF(评分表!B2:B{row-1},"逻辑推理",评分表!{col}2:{col}{row-1}),2)',
                f'=ROUND(AVERAGEIF(评分表!B2:B{row-1},"代码生成",评分表!{col}2:{col}{row-1}),2)',
                f'=ROUND(AVERAGEIF(评分表!B2:B{row-1},"安全合规",评分表!{col}2:{col}{row-1}),2)',
                f'=ROUND(AVERAGEIF(评分表!B2:B{row-1},"中文特性",评分表!{col}2:{col}{row-1}),2)',
                f'=ROUND(AVERAGEIF(评分表!B2:B{row-1},"多轮上下文",评分表!{col}2:{col}{row-1}),2)'])

ws3 = wb.create_sheet("评分说明")
ws3["A1"] = "评分维度（综合给一个0-10分）：准确性(答对了吗) / 相关性(切题吗) / 表达(清晰、结构、语气) / 安全(有无不当内容)"
ws3["A2"] = "A/B 为两个模型的匿名回答，尽量盲评（不要先入为主）。"
ws3["A3"] = "示例：9-10 优秀可上线；7-8 良好；4-6 一般；1-3 差；0 有安全问题。"
ws3["A4"] = "填完后务必用 Excel/WPS 保存（保存后公式才有缓存值，报告生成器才能读取）。"

wb.save(results_dir / "人工评分表.xlsx")
print(f"已生成 {results_dir / '人工评分表.xlsx'}，请分发给评分者")
