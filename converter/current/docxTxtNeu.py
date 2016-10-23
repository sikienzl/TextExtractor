try:
	from xml.etree.cElementTree import XML
except Importerror:
	from xml.etree.ElementTree import XML
import zipfile

WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'

def get_docx_text(path):
	document = zipfile.ZipFile(path)
	xml_content = document.read('word/document.xml')
	document.close()
	tree = XML(xml_content)
	paragraphs = []
	for paragraph in tree.getiterator(PARA):
		texts = [noe.text
			for node in paragraph.getiterator(TEXT)
			if node.text]
		if texts:
			paragraphs.append(''.join(texts))
	print("\n\n".join(paragraphs)

