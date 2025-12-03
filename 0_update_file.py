import shutil
import os

def copy_dir(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print("拷贝完成（覆盖模式）！")


def copy_file(src_file, dst_file):
    dst_dir = os.path.dirname(dst_file)
    if dst_dir and not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    shutil.copy2(src_file, dst_file)
    print(f"文件已复制并覆盖（如果存在）")

src = r"D:\xwh\ailab记录\工作\25年10月\cline写作\Overleaf-SuperSFE\imgs"
dst = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\imgs"
copy_dir(src, dst)

src = r"D:\xwh\ailab记录\工作\25年10月\cline写作\Overleaf-SuperSFE\sections"
dst = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\sections"
copy_dir(src, dst)

src = r"D:\xwh\ailab记录\工作\25年10月\cline写作\Overleaf-SuperSFE\googledeepmind.cls"
dst = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\googledeepmind.cls"
copy_file(src, dst)

src = r"D:\xwh\ailab记录\工作\25年10月\cline写作\Overleaf-SuperSFE\main.bib"
dst = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\main.bib"
copy_file(src, dst)

src = r"D:\xwh\ailab记录\工作\25年10月\cline写作\Overleaf-SuperSFE\main.tex"
dst = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\main.tex"
copy_file(src, dst)