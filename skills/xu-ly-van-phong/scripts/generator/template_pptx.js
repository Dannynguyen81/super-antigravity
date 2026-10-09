/**
 * Generator PPTX — sinh slide mang Brand DNA từ brand_kit.json
 * Chạy: node template_pptx.js path/to/brand_kit.json
 * Nguyên tắc: Master Slide thiết lập 1 lần, mỗi slide có yếu tố thị giác, chart vẽ "sống".
 */
const fs = require('fs');
const path = require('path');
const PptxGenJS = require('pptxgenjs');

// 1. NẠP BRAND KIT
const brandKitPath = process.argv[2] || path.join(__dirname, '../../standards/brand_kits/example/brand_kit.json');
const brand = JSON.parse(fs.readFileSync(brandKitPath, 'utf8'));
const C = brand.colors; // dk1, lt1, dk2, lt2, accent1..accent6
const brandDir = path.dirname(brandKitPath);

// 2. MASTER SLIDE — thiết lập 1 lần duy nhất
const pptx = new PptxGenJS();
pptx.defineLayout({ name: 'WIDE', width: 13.33, height: 7.5 });
pptx.layout = 'WIDE';

const masterObjects = [
    { rect: { x: 0, y: 7.0, w: '100%', h: 0.5, fill: { color: C.accent1 } } }
];
// Logo có thể vắng mặt — kiểm tra trước khi nhúng
const logoPath = brand.assets && brand.assets.logo ? path.resolve(brandDir, brand.assets.logo) : null;
if (logoPath && fs.existsSync(logoPath)) {
    masterObjects.push({ image: { x: 12.0, y: 0.3, w: 1.0, h: 0.5, path: logoPath } });
}
pptx.defineSlideMaster({ title: 'MASTER', background: { color: C.lt1 }, objects: masterObjects });

// 3. SLIDE TIÊU ĐỀ — stat callout lớn (yếu tố thị giác)
const s1 = pptx.addSlide({ masterName: 'MASTER' });
s1.addText(`${brand.company_name}`, {
    x: 0.8, y: 1.2, w: 11.7, h: 1.2,
    fontFace: brand.fonts.heading, fontSize: 40, bold: true, color: C.accent1
});
s1.addText('Mẫu Slide sinh tự động từ Brand Kit', {
    x: 0.8, y: 2.4, w: 11.7, h: 0.8,
    fontFace: brand.fonts.body, fontSize: 20, color: C.dk2
});
s1.addShape(pptx.ShapeType.roundRect, { x: 0.8, y: 3.6, w: 3.6, h: 2.2, fill: { color: C.lt2 }, line: { color: C.accent2, width: 1.5 } });
s1.addText('100%', { x: 0.8, y: 3.8, w: 3.6, h: 1.2, align: 'center', fontFace: brand.fonts.heading, fontSize: 60, bold: true, color: C.accent1 });
s1.addText('Màu & font nạp từ JSON', { x: 0.8, y: 5.0, w: 3.6, h: 0.6, align: 'center', fontFace: brand.fonts.body, fontSize: 13, color: C.dk2 });

// 4. SLIDE BIỂU ĐỒ — chart "sống", màu theo brand
const s2 = pptx.addSlide({ masterName: 'MASTER' });
s2.addText('Biểu đồ vẽ sống bằng Data thô', {
    x: 0.8, y: 0.5, w: 11.7, h: 0.9,
    fontFace: brand.fonts.heading, fontSize: 28, bold: true, color: C.accent1
});
s2.addChart(pptx.ChartType.bar, [
    { name: 'Doanh thu', labels: ['Q1', 'Q2', 'Q3', 'Q4'], values: [120, 180, 150, 220] }
], {
    x: 0.8, y: 1.6, w: 11.7, h: 5.0,
    chartColors: [C.accent1, C.accent2, C.accent3, C.accent4],
    catAxisLabelColor: C.dk2, valAxisLabelColor: C.dk2,
    dataLabelColor: C.dk1, showValue: true
});

// 5. XUẤT FILE
const outputPath = `Output_${brand.company_name}.pptx`;
pptx.writeFile({ fileName: outputPath }).then(() => {
    console.log(`Đã xuất file thành công: ${outputPath} mang Brand DNA của ${brand.company_name}`);
});
