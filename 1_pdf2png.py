import os
import fitz  # PyMuPDF
from PIL import Image

# ============ 配置区 ============
scan_dir = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\imgs"
out_dir  = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\imgs"  # 与 scan_dir 完全一致
zoom_x = 1.5  # 🔥 超高清
zoom_y = 1.5
# ===============================

def get_unique_path(path):
    """若文件已存在，自动添加 _1, _2 后缀（但不改变扩展名规则）"""
    base, ext = os.path.splitext(path)
    i = 1
    new = path
    while os.path.exists(new):
        new = f"{base}_{i}{ext}"
        i += 1
    return new

def convert_pdf_to_png(pdf_path, png_dir, base_name):
    """将 PDF 转成 PNG，保持原始 PDF 名字"""
    doc = fitz.open(pdf_path)
    matrix = fitz.Matrix(zoom_x, zoom_y)

    # 输出文件路径（直接用原名字）
    png_path = os.path.join(png_dir, base_name + ".png")
    png_path = get_unique_path(png_path)  # 仅在有同名时才加 _1/_2

    # 如果多页，合并为长图
    if len(doc) > 1:
        print(f"📚 多页PDF，合并为长图: {base_name}.pdf → {os.path.basename(png_path)}")
        images = []
        for page in doc:
            pix = page.get_pixmap(matrix=matrix)
            img = pix.to_pil()
            images.append(img)

        # 计算合并尺寸
        width = max(img.width for img in images)
        height = sum(img.height for img in images)

        merged = Image.new("RGB", (width, height))
        y = 0
        for img in images:
            merged.paste(img, (0, y))
            y += img.height

        merged.save(png_path)
        print(f"✅ 生成长图PNG: {png_path}")

    else:
        # 只有 1 页 → 直接保存
        page = doc[0]
        pix = page.get_pixmap(matrix=matrix)
        pix.save(png_path)
        print(f"✅ 生成PNG: {png_path}")

    doc.close()

print("🔍 开始扫描 PDF 并转换...")

for root, _, files in os.walk(scan_dir):
    for file in files:
        file_path = os.path.join(root, file)
        base, ext = os.path.splitext(file)

        if ext.lower() == ".pdf":
            print(f"📄 转换 PDF: {file_path}")
            try:
                convert_pdf_to_png(file_path, root, base)
                os.remove(file_path)  # 🗑 删除原PDF
                print(f"🗑 已删除 PDF: {file_path}")
            except Exception as e:
                print(f"⚠️ PDF 转换失败: {file_path} → {e}")

print("🎉 全部 PDF 转换 + 删除完成！")
