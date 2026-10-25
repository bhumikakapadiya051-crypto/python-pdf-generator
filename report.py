from reportlab.pdfgen import canvas
c = canvas.Canvas("report.pdf")
c.setFont("Helvetica-Bold" ,20)
c.drawString(150,800,"python report lab")

c.setFont("Helvetica",13)
c.drawString(100,750,"data analysis report")
c.drawString(100,710,"total Students:50 ")
c.drawString(100,680,"average marks:85%")
c.drawString(100,650,"status:excellent")

c.save()
print("pdf report created!")