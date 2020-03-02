# command: python pdfmerger.py dummy.pdf twopage.pdf

import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		merger.append(pdf)
	merger.write('super.pdf')
	print('super.pdf created!!!!')

pdf_combiner(inputs)