import os.path
import pandas as pd

# writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')

df = pd.DataFrame(columns=['Ano', 'Nome'])

# Pegar pasta
_PASTA_COM_OS_ARTIGOS_ = "T:/0 - PUCPR/Mestrado/1 - MetodologiaDePesquisa/Pre-Pool"

# Pegar arquivos na pasta

artigos = os.listdir(_PASTA_COM_OS_ARTIGOS_)
# print(artigos)

# Pegar nome de cada um
for art in artigos:
    # Dividir entre ANO e NOME
    um_artigo = [art[0:4], art[4:].replace('.pdf', '')]
    # print(um_artigo)

    # Salvar em uma nova linha
    df = df.append({'Ano': str(um_artigo[0]), 'Nome': str(um_artigo[1])}, ignore_index=True)

# Sallvar arquivo
# print(df)

df.to_excel(_PASTA_COM_OS_ARTIGOS_ + '/artigos.xlsx')
"""

_IMAGES_ORIGINAL_PATH_ = "./covid-chestxray-dataset/images"
_IMAGES_FINAL_PATH_ = "./imagensOrganizadas"



df = pd.read_csv("./covid-chestxray-dataset/metadata.csv")



rows, cols = df.shape[0], df.shape[1]
print(f'Row = {rows}')
print(f'Cols = {cols}')


# Verifica se se um diretorio existe, e entao cria ele
def CreateNewFolder(folder):
    if not path.exists(str(folder)):
        os.makedirs(str(folder))
        #print("Pasta criada")
    #else:
        #print("Pasta já existe")

# Criar Diretorios
def CreateFolders():
    #Separa todos os virus existentes
    virusList = ['']
    for index, row in df.iterrows():
        v = row['finding']
        v = v.title().replace(" ", "")
        print(v)

        newOne = True
        for name in range(len(virusList)):
            if v == virusList[name]:
                #print('old --- ', v)
                newOne = False
                break

        if newOne:
            #print('NEW one ---', v)
            virusList.append(v)

    #Comeca a criacao dos dirtorios
    #CreateNewFolder(_IMAGES_FINAL_PATH_)

    for name in range(len(virusList)):
        newPath = _IMAGES_FINAL_PATH_ + "/" + virusList[name]
        CreateNewFolder(newPath)

# Copiar o arquivo e coloca em uma pasta
def File_To_Folders():
    notFoundCount = 0
    notFoundFiles = ['']
    for index, row in df.iterrows():

        #if row['finding'] == "Klebsiella":
        imageLocation = _IMAGES_ORIGINAL_PATH_ + "/" + row['filename']
        finalLocation = _IMAGES_FINAL_PATH_ + "/" + row['finding'].title().replace(" ", "")

        if path.exists(str(imageLocation)):
            shutil.copy2(imageLocation, finalLocation + "/" + row['filename'])
            print("." + str(index))
        else:
            #print("Not found id:" + str(row) + " - PATH: " + imageLocation)
            notFoundCount += 1
            notFoundFiles.append(imageLocation)


    with open('not_found_files.txt', 'w') as f:
        for item in notFoundFiles:
            f.write("%s\n" % item)

    print("End")

# -- Recomendavel que seja feito um de cada vez

CreateFolders()
File_To_Folders()


"""
