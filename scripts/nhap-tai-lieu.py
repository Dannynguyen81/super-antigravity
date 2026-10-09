#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script: nhap-tai-lieu.py
Mục đích: Tự động chuyển đổi tài liệu thô (.docx, .xlsx, .pptx, .pdf, .txt) trong 10-inbox sang 20-sources/trich-xuat-inbox.
SecondBrain Knowledge Lifecycle
"""

import os
import sys
import shutil
import datetime
from pathlib import Path

# Đảm bảo in UTF-8 mượt mà trên console Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Thử import markitdown nếu có, nếu không thì dùng fallback native
HAVE_MARKITDOWN = False
try:
    from markitdown import MarkItDown
    md_converter = MarkItDown()
    HAVE_MARKITDOWN = True
except ImportError:
    pass

ROOT_DIR = Path(__file__).resolve().parent.parent
INBOX_DIR = ROOT_DIR / "10-inbox"
ARCHIVE_DIR = ROOT_DIR / "90-archive" / "inbox-da-xu-ly"
PARSED_DIR = ROOT_DIR / "20-sources" / "trich-xuat-inbox"

SUPPORTED_EXTS = {".docx", ".xlsx", ".pptx", ".pdf", ".txt", ".csv"}

def init_folders():
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    PARSED_DIR.mkdir(parents=True, exist_ok=True)

def convert_file(file_path: Path) -> Path:
    stem = file_path.stem
    ext = file_path.suffix.lower()
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    out_file = PARSED_DIR / f"{stem}.md"
    content_body = ""

    if HAVE_MARKITDOWN:
        try:
            result = md_converter.convert(str(file_path))
            content_body = result.text_content
        except Exception as e:
            content_body = f"> [!WARNING] Lỗi chuyển đổi bằng MarkItDown: {e}\n\n*Nội dung file gốc được giữ tại: {file_path.name}*"
    else:
        # Fallback cơ bản khi chưa cài thư viện
        if ext == ".txt" or ext == ".csv":
            try:
                content_body = file_path.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                content_body = f"Lỗi đọc file text: {e}"
        else:
            content_body = f"""
> [!NOTE] Thông Báo Chuyển Đổi
> File `{file_path.name}` thuộc định dạng nhị phân ({ext}).
> Để tự động bóc tách toàn diện nội dung bảng biểu và văn bản, hãy cài đặt `markitdown`:
> ```powershell
> pip install markitdown
> ```
"""

    frontmatter = f"""---
id: SRC-{today}-{stem[:20]}
title: {stem.replace('-', ' ').title()}
source_file: {file_path.name}
import_date: {now_str}
status: source
tags:
  - sources
  - trich-xuat-inbox
---

# {stem.replace('-', ' ').title()}

*Tài liệu nguồn được chuyển đổi tự động từ file gốc: `{file_path.name}` vào lúc {now_str}.*

---

{content_body}
"""

    out_file.write_text(frontmatter, encoding="utf-8")
    return out_file

def main():
    init_folders()
    print("=" * 60)
    print("🚀 ĐỘNG CƠ NHẬP TÀI LIỆU — KNOWLEDGE LIFECYCLE")
    print(f"📂 Thư mục quét: {INBOX_DIR}")
    print(f"🎯 Đích xuất: {PARSED_DIR}")
    print(f"⚙️ Trạng thái MarkItDown: {'Đã sẵn sàng' if HAVE_MARKITDOWN else 'Chưa cài đặt (Dùng Native Fallback)'}")
    print("=" * 60)

    found_files = [f for f in INBOX_DIR.iterdir() if f.is_file() and f.suffix.lower() in SUPPORTED_EXTS]

    if not found_files:
        print("ℹ️ Không tìm thấy file mới nào cần chuyển đổi trong 10-inbox/.")
        print("👉 Hãy copy file .docx, .xlsx, .pdf vào 10-inbox/ rồi chạy lại lệnh này.")
        return 0

    print(f"🔍 Tìm thấy {len(found_files)} tài liệu. Đang xử lý...\n")

    for idx, f in enumerate(found_files, 1):
        print(f"[{idx}/{len(found_files)}] Đang bóc tách: {f.name} ... ", end="")
        try:
            out_md = convert_file(f)
            # Di chuyển file gốc vào archive
            target_archive = ARCHIVE_DIR / f.name
            if target_archive.exists():
                target_archive.unlink()
            shutil.move(str(f), str(target_archive))
            print(f"✅ Xong -> {out_md.name}")
        except Exception as e:
            print(f"❌ Lỗi: {e}")

    print(f"\n🎉 Hoàn tất! Tài liệu Markdown đã được lưu tại 20-sources/trich-xuat-inbox/")
    return 0

if __name__ == "__main__":
    sys.exit(main())
