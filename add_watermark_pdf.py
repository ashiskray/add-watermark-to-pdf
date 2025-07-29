# To add water mark to the pdf we need watermark in pdf form
import PyPDF2
with open (r"C:\Users\ashis\OneDrive\Desktop\Data Automation\pdf_automation\add watermark in pdf\merger_output.pdf","rb") as file,  open (r"C:\Users\ashis\OneDrive\Desktop\Data Automation\pdf_automation\add watermark in pdf\water.pdf","rb") as watermark_file:
    file_reader=PyPDF2.PdfReader(file)
    watermark_reader=PyPDF2.PdfReader(watermark_file)
    writer=PyPDF2.PdfWriter()
    watermark_page=watermark_reader.pages[0]
    for page in file_reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)
with open ("watermarkedfile.pdf","wb") as output_file:
    writer.write(output_file)