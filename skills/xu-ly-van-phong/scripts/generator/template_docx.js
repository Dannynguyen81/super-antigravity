const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, BorderStyle, WidthType, ShadingType } = require('docx');

// 1. NẠP BRAND KIT TỪ JSON
const brandKitPath = process.argv[2] || '../../standards/brand_kits/example/brand_kit.json';
const brand = JSON.parse(fs.readFileSync(brandKitPath, 'utf8'));

// 2. THIẾT LẬP STYLE TOÀN CỤC (GLOBAL THEME)
const doc = new Document({
    creator: brand.company_name,
    styles: {
        paragraphStyles: [
            {
                id: "Normal",
                name: "Normal",
                basedOn: "Normal",
                next: "Normal",
                run: { font: brand.fonts.body, size: 24, color: brand.colors.dk2 }, // 12pt
                paragraph: { spacing: { after: 120, line: 240 } }
            },
            {
                id: "Heading1",
                name: "Heading 1",
                basedOn: "Normal",
                next: "Normal",
                run: { font: brand.fonts.heading, size: 36, color: brand.colors.accent1, bold: true }, // 18pt
                paragraph: { spacing: { before: 240, after: 120 } }
            },
            {
                id: "Heading2",
                name: "Heading 2",
                basedOn: "Normal",
                next: "Normal",
                run: { font: brand.fonts.heading, size: 32, color: brand.colors.accent2, bold: true }, // 16pt
                paragraph: { spacing: { before: 200, after: 100 } }
            }
        ]
    },
    sections: [{
        properties: {},
        children: [
            new Paragraph({ text: `${brand.company_name} - Mẫu Đề xuất Kỹ thuật`, heading: HeadingLevel.HEADING_1 }),
            new Paragraph({ text: "Đây là ví dụ về việc văn bản tự động nhận màu sắc và font chữ từ Brand Kit JSON mà không cần gõ cứng (hardcode) bất kỳ mã màu Hex nào trong code Node.js." }),
            new Paragraph({ text: "Heading 2: Ứng dụng vẽ UI", heading: HeadingLevel.HEADING_2 }),
            
            // Vẽ Callout Box dùng màu Brand
            new Table({
                width: { size: 100, type: WidthType.PERCENTAGE },
                rows: [
                    new TableRow({
                        children: [
                            new TableCell({
                                children: [new Paragraph({ text: "Callout Box mang DNA doanh nghiệp", style: "Normal" })],
                                shading: { fill: brand.colors.lt2, type: ShadingType.CLEAR },
                                borders: {
                                    top: { style: BorderStyle.NIL },
                                    bottom: { style: BorderStyle.NIL },
                                    right: { style: BorderStyle.NIL },
                                    left: { style: BorderStyle.SINGLE, size: 24, color: brand.colors.accent1 }
                                },
                                margins: { top: 200, bottom: 200, left: 200, right: 200 }
                            })
                        ]
                    })
                ]
            })
        ]
    }]
});

// 3. XUẤT FILE
const outputPath = `Output_${brand.company_name}.docx`;
Packer.toBuffer(doc).then((buffer) => {
    fs.writeFileSync(outputPath, buffer);
    console.log(`Đã xuất file thành công: ${outputPath} mang Brand DNA của ${brand.company_name}`);
});
