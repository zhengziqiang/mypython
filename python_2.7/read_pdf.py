#coding=utf-8
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
import LAParams
import PDFPageAggregator
fp = open('/home/zzq/learngit/pdf_document/php.pdf')#打开文件
parser=PDFParser(fp)#解析器
doc =PDFDocument()#文档
doc.set_parser(parser)#设置解析器
doc.initialize("")#初始化
resource=PDFResourceManager()#资源管理器
laparams=LAParams()#参数分析期
#聚合器
device=PDFPageAggregator()
#页面解析器
interpreter=PDFPageInterpreter(resource,device)

for page in doc.get_pages():
	interpreter.process_page(page)
	layout=device.get_result()
	for out in layout:
		print out.get_text()