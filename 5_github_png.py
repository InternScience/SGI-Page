import shutil
import os


def copy_file(src_file, dst_file):
    dst_dir = os.path.dirname(dst_file)
    if dst_dir and not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    shutil.copy2(src_file, dst_file)
    print(f"文件已复制并覆盖（如果存在）")

src = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\imgs\evaluation-framework.png"
dst = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\github_images"
copy_file(src, dst)

src = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\imgs\teaser.png"
dst = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\github_images"
copy_file(src, dst)

src = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\imgs\subjects.png"
dst = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\github_images"
copy_file(src, dst)

src = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\imgs\grpo_reward_curves.png"
dst = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\github_images"
copy_file(src, dst)

src = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\paper\imgs\pipeline.png"
dst = r"D:\xwh\ailab记录\工作\25年10月\cline网页\SGI-Page\github_images"
copy_file(src, dst)