import shutil
import os.path
from os import path
from pybtex.database import parse_file

# LOCATIONS
_ARTICLES_FOLDER_ = "./weird_name_files"
_BIBITEX_FILE_ = './MyCollection.bib'
_FINAL_FOLDER = './beautiful_name_files'

# DEBUG
see_debug = True
detailed_debug = True

debug_file = list()
notFound_Path = list()
notFound_fromBib = list()
Found = list()

# SETUP
print('Initializing....')
print('Please, put all the PDFs with weird names in the folder "weird_name_files".')
print('And remember to leave your .bib file with name "MyCollection.bib". ')

if not path.exists(str(_ARTICLES_FOLDER_)):
    os.makedirs(str(_ARTICLES_FOLDER_))

if not path.exists(str(_FINAL_FOLDER)):
    os.makedirs(str(_FINAL_FOLDER))


input('Press ENTER to continue...')
bib_data = parse_file(_BIBITEX_FILE_)
articles_in_folder = os.listdir(_ARTICLES_FOLDER_)

dbg1 = str(input('Do you want to see some Debug? [Y/N] ')).strip()[0]
dbg2 = str(input('A lot of Debug? [Y/N] '))
print('')

if dbg1 in 'nN':
    see_debug = False
if dbg2 in 'nN':
    detailed_debug = False

for bib_artc in bib_data.entries.values():
    pdf_file_complete_path = str(bib_artc.fields['file']).split('/')

    split_count = len(pdf_file_complete_path) - 1
    pdf_file_name = pdf_file_complete_path[split_count].replace(':pdf', '')
    pdf_file_name = pdf_file_name.replace('{\_}', '_')

    article_name = str(bib_artc.fields['title'])[:].replace('{', '').replace('}', '').replace(':', '')
    article_year = str(bib_artc.fields['year'])[:]

    print('+ file: ', pdf_file_name, end=' - ')
    if pdf_file_name in articles_in_folder:
        print('FOUND')

        filePath = _ARTICLES_FOLDER_ + '/' + pdf_file_name
        final_pdf_name = article_year + ' - ' + article_name + '.pdf'
        debug_file = [pdf_file_name, filePath, article_year, article_name, final_pdf_name]

        if see_debug:
            print('+ path: ' + filePath, end=' - ')

        if path.exists(str(filePath)):
            if see_debug:
                print('FOUND')

            if detailed_debug:
                print('>> year: ' + article_year)
                print('>> name: ' + article_name)
                print('>> final name: ', final_pdf_name)

            shutil.copy2(filePath, './' + _FINAL_FOLDER + '/' + final_pdf_name)
            print('+ operation: SUCCESS')
            Found.append(debug_file[:])

        else:
            print('')
            print('+ operation: FAIL - PATH NOT FOUND')
            # the PDF was found, bet there was a problem in the patch to find the file
            notFound_Path.append(debug_file[:])

        debug_file.clear()

    else:
        print('')
        print('+ operation: FAIL - PDF DOES NOT EXIST')
        not_found_file = [pdf_file_name, article_year, article_name]
        notFound_fromBib.append(not_found_file[:])
        not_found_file.clear()
        # exists in .Bib, but was not found in PDfs in _ARTICLES_FOLDER_

    print('')


print('='*100)
print('Saving on debug.txt...')
with open('debug.txt', 'w') as f:

    f.write('-' * 100)
    f.write('\nPDF NOT FOUND\n>> Files that exists in your .bib, but the pdf was not found in {} \n\n'.format(_ARTICLES_FOLDER_))


    print('> NOT FOUND PDF - file:', end=' ')
    for i, file in enumerate(notFound_fromBib):
        string = f'File {i+1} / {len(notFound_fromBib)}\n>> article year: {file[1]}\n>> article name: {file[2]}\n>>>> pdf name in .bib: {file[0]}'
        print(f'{i+1} / {len(notFound_fromBib)}', end=' .. ')

        f.write(f'{string}\n\n')

    print('FINISH')
    f.write('-'*100)
    f.write('\nPATH NOT FOUND\n>> Files that exists in your .bib and a pdf was found, but there is some problem'
            ' with the path \n\n')

    print('> NOT FOUND PATH - file:', end=' ')
    for i, file in enumerate(notFound_Path):
        string = f'File {i + 1}/{len(notFound_Path)}\n>> article year: {file[2]}\n>> article name: {file[3]}\n' \
                 f'>>>> pdf name in .bib: {file[0]}\n>>>> pdf path: {file[1]}\n>>>> final pdf name: {file[4]}'
        print(f'{i+1}/{len(notFound_Path)}', end=' .. ')

        f.write(f'{string}\n\n')

    print('FINISH')
    f.write('-' * 100)
    f.write('\nFOUND FILES\n>> Files that was found and is copyed on the new folther with the new name \n\n')

    print('> FOUND FILES - file:', end=' ')
    for i, file in enumerate(Found):
        string = f'File {i + 1} / {len(Found)}\n>> article year: {file[2]}\n>> article name: {file[3]}\n' \
                 f'>>>> pdf name in .bib: {file[0]}\n>>>> pdf path: {file[1]}\n>>>> final pdf name: {file[4]}'
        print(f'{i + 1}/{len(Found)}', end=' .. ')

        f.write(f'{string}\n\n')

    print('FINISH')

print('Saving complete.')
input('\nPress ENTER to close.')
