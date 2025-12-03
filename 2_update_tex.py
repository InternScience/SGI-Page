import os
import re

scan_tex_dir = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\sections"

# 匹配 imgs/...pdf，并把 .pdf/.PDF 统一改成 .png，同时捕获完整路径
pattern = re.compile(r"(imgs/[^}]+?)\.pdf", re.IGNORECASE)

print("🔧 开始替换 tex 中的 PDF 引用为 PNG，并添加 paper/ 前缀...\n")

for root, _, files in os.walk(scan_tex_dir):
    for file in files:
        if file.lower().endswith(".tex"):
            tex_path = os.path.join(root, file)
            print(f"📄 处理: {tex_path}")

            with open(tex_path, "r", encoding="utf-8") as f:
                content = f.read()

            # 替换：在路径前加上 paper/，并把后缀换成 .png
            new_content, n = pattern.subn(r"paper/\1.png", content)

            if n > 0:
                with open(tex_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"✅ 已替换 {n} 处\n")
            else:
                print("🔹 未找到 imgs/*.pdf 引用\n")

print("🎉 全部 tex 引用替换完成！")
