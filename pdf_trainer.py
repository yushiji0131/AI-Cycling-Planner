from fpdf import FPDF
from datetime import datetime

# 完整12周训练数据（示例展示前3周，完整数据需展开）
TRAINING_PLAN = {
    "weeks": [
        {   # 第1周 - 基础适应期
            "week_num": 1,
            "phase": "基础适应期",
            "days": {
                "周一": {
                    "type": "阈值爬坡",
                    "duration": "75分钟",
                    "zones": "Z4",
                    "detail": "3组×8分钟Z4爬坡（坡度5%，踏频70rpm）\n组间休息5分钟\n核心训练：平板支撑3x45秒"
                },
                "周二": {
                    "type": "主动恢复",
                    "duration": "45分钟",
                    "zones": "Z1",
                    "detail": "轻松骑行+动态拉伸\n心率≤120bpm"
                },
                "周三": {
                    "type": "爬坡力量+VO2Max",
                    "duration": "80分钟",
                    "zones": "Z3-Z5",
                    "detail": "低踏频爬坡5x5分钟Z3（50rpm）\n高踏频冲刺3x3分钟Z5（100rpm）"
                },
                "周四": {
                    "type": "低强度有氧",
                    "duration": "60分钟",
                    "zones": "Z2",
                    "detail": "稳定平路骑行，踏频85-95rpm"
                },
                "周五": {
                    "type": "阈值耐力",
                    "duration": "75分钟",
                    "zones": "Z3",
                    "detail": "2×20分钟Z3持续输出（坡度3%）"
                },
                "周六": {
                    "type": "长骑整合",
                    "duration": "180分钟",
                    "zones": "Z2-Z3",
                    "detail": "前2小时Z2稳定骑行\n后1小时4x8分钟Z3爬坡（坡度5%）"
                },
                "周日": {
                    "type": "强制休息",
                    "duration": "-",
                    "zones": "-",
                    "detail": "禁止任何训练，建议散步或泡沫轴放松"
                }
            },
            "notes": "重点：适应低踏频爬坡，注意每小时补充60g碳水"
        },
        {   # 第2周 - 基础适应期
            "week_num": 2,
            "phase": "基础适应期",
            "days": {
                "周一": {
                    "type": "阈值爬坡",
                    "duration": "80分钟",
                    "zones": "Z4",
                    "detail": "4组×8分钟Z4爬坡（坡度5%），组间休息5分钟\n核心训练：侧平板支撑2x60秒/侧"
                },
                # 周二至周日结构同第1周，内容渐进调整...
            },
            "notes": "本周增加1组阈值间歇，提升肌肉耐力"
        },
        # 第3-12周数据模板类似，根据阶段调整参数...
    ],
    # 恢复训练数据同上...
}

def generate_full_pdf():
    pdf = FPDF()
    pdf.add_font('NotoSansSC', 'B', 'NotoSansSC-VariableFont_wght.ttf', uni=True)
    # pdf.add_font('NotoSansSC', 'B', 'NotoSansSC-Bold.ttf', uni=True)
    
    # 封面设计
    pdf.add_page()
    pdf.set_font('NotoSansSC', 'B', 24)
    pdf.cell(0, 40, "12周全周期训练计划", 0, 1, 'C')
    pdf.set_font_size(16)
    pdf.cell(0, 10, "FTP 250W | 每周8-10小时", 0, 1, 'C')
    
    # 生成每周计划
    for week in TRAINING_PLAN["weeks"]:
        pdf.add_page()
        pdf.set_font('NotoSansSC', 'B', 14)
        title = f"第{week['week_num']}周 - {week['phase']}"
        pdf.cell(0, 10, title, 0, 1)
        
        # 周计划表格（7天）
        col_width = [22, 25, 20, 100]
        headers = ["星期", "类型", "强度", "训练内容"]
        pdf.set_fill_color(240, 240, 240)
        
        # 表头
        for i, h in enumerate(headers):
            pdf.cell(col_width[i], 10, h, 1, 0, 'C', fill=True)
        pdf.ln()
        
        # 表格内容
        for day in ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]:
            data = week["days"][day]
            pdf.cell(col_width[0], 10, day, 1)
            pdf.cell(col_width[1], 10, data["type"], 1)
            pdf.cell(col_width[2], 10, data["zones"], 1)
            pdf.multi_cell(col_width[3], 10, data["detail"], 1)
            pdf.ln(0)
        
        # 周备注
        pdf.set_font('NotoSansSC', 'NotoSansSC-Regular.ttf', 10)
        pdf.cell(0, 10, f"📌 重点提示: {week['notes']}", 0, 1)
    
    # 生成PDF
    pdf.output("12_Week_Full_Schedule.pdf")

if __name__ == "__main__":
    generate_full_pdf()