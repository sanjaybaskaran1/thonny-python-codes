from PyPDF2 import PdfReader, PdfWriter

def merge_pdf(pdf_list,output_path):
    pdfwriter = PdfWriter()
    for pdf in pdf_list:
        pdfreader = PdfReader(pdf)
        print(len(pdfreader.pages))
       
        for pg_no in range(0,len(pdfreader.pages)):
            pdfwriter.add_page(pdfreader.pages[pg_no])
            
        with open(output_path, "wb") as out_put:
            pdfwriter.write(out_put)
        print(f"merged pdf saved in {output_path}")
        
merge_pdf(["C:\\Users\\Sanjay\\OneDrive\\Desktop\\12 to 2pm python.pdf",
           "C:\\Users\\Sanjay\\OneDrive\\Desktop\\SPIRO PROJECT TITLES 2024-2025.pdf"],
           "C:\\Users\\Sanjay\\OneDrive\\Desktop\\merged.pdf")