#from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.colors import Color, black,green, white, blue, red, lightblue,pink,lavender,orange,limegreen,khaki,beige
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image,TableStyle
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER, inch
from reportlab.graphics.shapes import Line, LineShape, Drawing
from reportlab.lib.colors import Color
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.barcharts import VerticalBarChart
#import xlrd
def invoice(c):

    c.setFillColorRGB(1,0,0) 
    c.setFont("Helvetica", 30) 
    c.drawString(50,1090,"Tax Invoice")
    #-----------------------------Address1---------------------------
    c.setFillColorRGB(0,0,0) 
    c.setFont("Helvetica",20 )
    c.drawString(50,1250,"[company name]") 
    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica", 20) 
    c.drawString(50,1225,"Office No 101, 1st Floor, B3 Building,")
    c.drawString(50,1200,"subash Park, lulu M25")
    c.drawString(50,1175,"PO Box 133702, Abu Dhabi, UAE")
    c.drawString(50,1150,"Fax: no fax")
    c.drawString(50,1125,"Phone: +91 7025752005")
    #c.drawString(50,1130,"Address1")
    #----------------------------Address2-----------------------------
    c.drawString(50,1060,"BILL TO")
    c.drawString(50,1035,"[company name]")
    c.drawString(50,1010,"Office No 1421, 4th Floor, infopark,")
    c.drawString(50,990,"Kozhikode, Kerala – 673014")
    c.drawString(50,965,"Email:mail@gmail.com")
    #c.drawString(50,1000,"Address1")

    #----------------------------Invoice details----------------------
    c.drawString(700,1100,"INVOICE NO:")
    c.drawString(850,1100,"2009")
    c.drawString(700,1080,"DATE:")
    c.drawString(850,1080,"22/33/23")
    c.drawString(700,1060,"DUE DATE:")
    c.drawString(850,1060,"22/11/11")
    c.drawString(700,1040,"TERMS:")
    c.drawString(850,1040,"#$%#@@")
    #--------------------------table------------------------------------
    line1 = ["NO","DESCRIPTION","HBN/SAC","QTY","RATE","AMOUNT","TAX",]
    line2 = ["1", "HKvision", "u78787", "566755","5757567","576556","765655"]
    line3 = ["2", "True tv", "187,533", "224,351","978089","987865","5687895654"]
    line4 = ["3", "ELLEYS", "154", "-","657887789","765665","75675"]
    line5 = ["4", "Pharma", "187,687", "224,351","76787","765443","76543"]
    line6 = ["" , "Total", "12345667","76565454","654543324","09876543","86585543"]
    data=[line1,line2,line3,line4,line5,line6]
    

    table = Table(data,rowHeights =35, colWidths=[ 70, 250, 110, 110, 110,110,110])
    tStyle = TableStyle([
    #('FONTNAME',(0, 1),(3, 1), 'Helvetica-Bold'),
    
    ('FONTNAME',(0, -1),(-1, -1), 'Helvetica-Bold'),
    ('VALIGN',(0, 0), (-1, 0), 'CENTER'),
    ('VALIGN',(0,0),(-1,-1), 'TOP'),
    #('TEXTCOLOR',(0,0),(-1,0),white),
    ('BACKGROUND',(0, -1),(-1, -1), lavender),
    #('BACKGROUND',(1, 1),(0, 0), green),
    ('GRID',(-1,-1),(-1,-1),0.5, '#CFEAD4'),
    ('FONTSIZE',(0, 0),(-1, -1), 20),
    ('BACKGROUND',(0, 0), (-1, 0),lightblue)])
    table.setStyle(tStyle)
    table.wrapOn(c, 100, 100)
    table.drawOn(c, 50, 650)
c = canvas.Canvas("invoice.pdf",pagesize=(1040,1348))
invoice(c)
c.showPage()
c.save()

    
