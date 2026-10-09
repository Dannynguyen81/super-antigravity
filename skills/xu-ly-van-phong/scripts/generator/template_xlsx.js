/**
 * Generator XLSX — sinh bảng tính mang Brand DNA từ brand_kit.json
 * Chạy: node template_xlsx.js path/to/brand_kit.json
 * Nguyên tắc: Live Formula (không hardcode kết quả), Zero Error, màu nạp từ Brand Kit.
 */
const fs = require('fs');
const path = require('path');
const ExcelJS = require('exceljs');

// 1. NẠP BRAND KIT
const brandKitPath = process.argv[2] || path.join(__dirname, '../../standards/brand_kits/example/brand_kit.json');
const brand = JSON.parse(fs.readFileSync(brandKitPath, 'utf8'));
const C = brand.colors; // dk1, lt1, dk2, lt2, accent1..accent6
const argb = (hex) => ({ argb: 'FF' + hex });

// 2. STYLE TOÀN CỤC TỪ BRAND KIT
const headerStyle = {
    font: { name: brand.fonts.heading, bold: true, size: 11, color: argb(C.lt1) },
    fill: { type: 'pattern', pattern: 'solid', fgColor: argb(C.accent1) },
    alignment: { horizontal: 'center', vertical: 'middle', wrapText: true },
    border: { top: { style: 'thin' }, bottom: { style: 'thin' }, left: { style: 'thin' }, right: { style: 'thin' } }
};
const zebraFill = { type: 'pattern', pattern: 'solid', fgColor: argb(C.lt2) };
const totalStyle = {
    font: { name: brand.fonts.body, bold: true, color: argb(C.accent1) },
    fill: { type: 'pattern', pattern: 'solid', fgColor: argb(C.lt2) }
};

// 3. DỰNG WORKBOOK MẪU (tracking tiến độ)
const wb = new ExcelJS.Workbook();
wb.creator = brand.company_name;
const ws = wb.addWorksheet('Tien do', { views: [{ state: 'frozen', ySplit: 1 }] });

ws.columns = [
    { header: 'STT', key: 'stt', width: 6 },
    { header: 'Hạng mục', key: 'ten', width: 38 },
    { header: 'Trạng thái', key: 'tt', width: 15 },
    { header: 'Ngân sách', key: 'ns', width: 14 },
    { header: 'Đã chi', key: 'chi', width: 14 },
    { header: '% Dùng', key: 'pct', width: 11 }
];

const rows = [
    [1, 'Khảo sát hiện trạng', 'Hoàn thành', 5000, 4800],
    [2, 'Thiết kế giải pháp', 'Đang chạy', 12000, 6500],
    [3, 'Triển khai hệ thống', 'Chưa bắt đầu', 30000, 0]
];
rows.forEach((r, i) => {
    const rowIdx = i + 2;
    const row = ws.addRow(r);
    // Live Formula — không hardcode kết quả
    ws.getCell(`F${rowIdx}`).value = { formula: `IF(D${rowIdx}=0,0,E${rowIdx}/D${rowIdx})` };
    ws.getCell(`F${rowIdx}`).numFmt = '0.0%';
    ['D', 'E'].forEach(col => ws.getCell(`${col}${rowIdx}`).numFmt = '#,##0');
    if (rowIdx % 2 === 0) row.eachCell({ includeEmpty: true }, c => { c.fill = zebraFill; });
    row.font = { name: brand.fonts.body, color: argb(C.dk1) };
});

// Dòng tổng — Live Formula
const totalIdx = rows.length + 2;
ws.getCell(`B${totalIdx}`).value = 'TỔNG';
ws.getCell(`D${totalIdx}`).value = { formula: `SUM(D2:D${totalIdx - 1})` };
ws.getCell(`E${totalIdx}`).value = { formula: `SUM(E2:E${totalIdx - 1})` };
ws.getCell(`F${totalIdx}`).value = { formula: `IF(D${totalIdx}=0,0,E${totalIdx}/D${totalIdx})` };
ws.getCell(`F${totalIdx}`).numFmt = '0.0%';
['D', 'E'].forEach(col => ws.getCell(`${col}${totalIdx}`).numFmt = '#,##0');
ws.getRow(totalIdx).eachCell({ includeEmpty: true }, c => { Object.assign(c, { style: { ...c.style } }); c.font = totalStyle.font; c.fill = totalStyle.fill; });

// Header style áp sau cùng
ws.getRow(1).height = 24;
ws.getRow(1).eachCell(c => { c.style = headerStyle; });

// 4. XUẤT FILE
const outputPath = `Output_${brand.company_name}.xlsx`;
wb.xlsx.writeFile(outputPath).then(() => {
    console.log(`Đã xuất file thành công: ${outputPath} mang Brand DNA của ${brand.company_name}`);
});
