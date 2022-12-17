from pdfreader import PDFDocument, SimplePDFViewer
fd = open("assets/school_1.pdf", "rb")
viewer = SimplePDFViewer(fd)
print(viewer)