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


def findFiles(issue):
    results = []
    files = os.listdir('./pdfs/')

    for file in files:
        result = re.match(r'HER_' + str(issue) + '_([0-9]*)[.]pdf', file)
        if result == None:
            pass
        else:
            results.append(file)
    results.sort()
    return results


def createIssue(issue):
    results = findFiles(issue)
    print('Files found for issue', issue, ':', len(results), '|', results)
    name = 'Herodote_'+ str(issue) + '.pdf'
    mergepdfs(results, name)
    print('SUCCESS, file writed as:', name, '\n')


for issue in range(171, 177):
    createIssue(issue)
    
