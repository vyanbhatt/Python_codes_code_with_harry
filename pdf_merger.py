import PyPDF2  #deals with pdfs

merger = PyPDF2.PdfMerger()

pdf_files = []

n = int(input("How many pdfs you want to merge : "))

for j in range(0,n):
    print(f"Enter {j+1} file path : ")
    pdf_files.append(input(r""))

for i in pdf_files:
    pdfFile = open(i, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)

pdfFile.close()
merger.write("Final.pdf")


