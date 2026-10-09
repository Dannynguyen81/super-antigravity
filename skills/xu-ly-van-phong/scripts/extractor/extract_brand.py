import os
import zipfile
import json
import xml.etree.ElementTree as ET
import shutil
import argparse

# XML Namespaces used in OOXML
NAMESPACES = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
}

def extract_color_value(color_element):
    """Trích xuất mã Hex từ node màu (srgbClr) hoặc màu hệ thống (sysClr)."""
    if color_element is None:
        return "000000"
    
    srgb = color_element.find('.//a:srgbClr', NAMESPACES)
    if srgb is not None:
        return srgb.get('val')
    
    sysClr = color_element.find('.//a:sysClr', NAMESPACES)
    if sysClr is not None:
        return sysClr.get('lastClr') or sysClr.get('val')
        
    return "000000"

def extract_brand_kit(file_path, output_dir):
    if not os.path.exists(file_path):
        print(f"File không tồn tại: {file_path}")
        return

    os.makedirs(output_dir, exist_ok=True)
    assets_dir = os.path.join(output_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)

    brand_kit = {
        "company_name": os.path.basename(file_path).split('.')[0],
        "colors": {},
        "fonts": {},
        "assets": {}
    }

    print(f"Đang phân tích file: {file_path}")
    
    try:
        with zipfile.ZipFile(file_path, 'r') as archive:
            # 1. TÌM FILE THEME
            theme_file = None
            if 'word/theme/theme1.xml' in archive.namelist():
                theme_file = 'word/theme/theme1.xml'
            elif 'ppt/theme/theme1.xml' in archive.namelist():
                theme_file = 'ppt/theme/theme1.xml'
            elif 'xl/theme/theme1.xml' in archive.namelist():
                theme_file = 'xl/theme/theme1.xml'

            if theme_file:
                print(f"Đã tìm thấy: {theme_file}")
                theme_xml = archive.read(theme_file)
                root = ET.fromstring(theme_xml)

                # Bóc màu sắc
                clr_scheme = root.find('.//a:clrScheme', NAMESPACES)
                if clr_scheme is not None:
                    color_tags = ['dk1', 'lt1', 'dk2', 'lt2', 'accent1', 'accent2', 'accent3', 'accent4', 'accent5', 'accent6']
                    for tag in color_tags:
                        node = clr_scheme.find(f'a:{tag}', NAMESPACES)
                        brand_kit["colors"][tag] = extract_color_value(node)

                # Bóc Font chữ
                font_scheme = root.find('.//a:fontScheme', NAMESPACES)
                if font_scheme is not None:
                    major = font_scheme.find('.//a:majorFont/a:latin', NAMESPACES)
                    minor = font_scheme.find('.//a:minorFont/a:latin', NAMESPACES)
                    brand_kit["fonts"]["heading"] = major.get('typeface') if major is not None else "Arial"
                    brand_kit["fonts"]["body"] = minor.get('typeface') if minor is not None else "Arial"
            
            # 2. BÓC TÁCH ASSETS (HÌNH ẢNH)
            for item in archive.namelist():
                if item.startswith('word/media/') or item.startswith('ppt/media/'):
                    filename = os.path.basename(item)
                    if filename:
                        source = archive.open(item)
                        target_path = os.path.join(assets_dir, filename)
                        with open(target_path, "wb") as target:
                            shutil.copyfileobj(source, target)
                        # Đăng ký asset đầu tiên tìm thấy làm logo (Tạm thời)
                        if "logo" not in brand_kit["assets"]:
                            brand_kit["assets"]["logo"] = f"assets/{filename}"
                            print(f"Đã xuất file ảnh: {filename}")

    except Exception as e:
        print(f"Lỗi giải nén hoặc phân tích XML: {e}")
        return

    # 3. LƯU BRAND KIT
    json_path = os.path.join(output_dir, "brand_kit.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(brand_kit, f, indent=4, ensure_ascii=False)
    
    print(f"\nThành công! Đã lưu Brand Kit tại: {json_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bóc tách Brand Kit từ file Office (OOXML)")
    parser.add_argument("file", help="Đường dẫn đến file .docx, .pptx, hoặc .xlsx")
    parser.add_argument("--out", default="brand_kit_output", help="Thư mục xuất file (mặc định: brand_kit_output)")
    args = parser.parse_args()
    
    extract_brand_kit(args.file, args.out)
