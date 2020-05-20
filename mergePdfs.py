from PyPDF2 import PdfFileMerger
import glob
import re
import os



def mergepdfs(pdfs, name):
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append('pdfs/' + pdf)
    merger.write(name)
    merger.close()


def findFiles(number):
    results = []
    files = os.listdir('./pdfs/')
    print('FILES:', files)
    for file in files:
        result = re.match(r'HER_([' + str(number) + ']*)_([0-9]*)[.]pdf', file)
        if result == None:
            pass
        else:
            results.append(file)
    results.sort()
    return results


results = findFiles(176)    # ISSUE 176
print('Files found:', results)
name = 'Herodote_'+ results[0][4:7] + '.pdf'
mergepdfs(results, name)
print('SUCCESS, file writed as:', name)
