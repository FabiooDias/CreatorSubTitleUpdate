import Control.classFileSrt
import Control.classCreateFile
import Control.classCreateSubtitle

def main():
    print("_______________ATUALIZADOR DE LEGENDA_______________")
    print("Será criado um novo arquivo com a legenda atualizada\n")
    name_file_input = input("Digite o exato nome do arquivo de legenda que quer atualizar (não inclua ao nome do arquivo o .srt no fim):\n")
    value_time = float(input("Informe o valor em segundos a quantidade que quer atualizar (Valor positivo é para atrasar e valor negativo é para adiantar):\n").replace(",", "."))

    verify_File = Control.classFileSrt.File_Srt()
    create_File = Control.classCreateFile.Create_Open_File()
    subtitle_create = Control.classCreateSubtitle.SubtitleCreate()

    file_Verify = verify_File.verifyFile(name_file_input)

    if file_Verify == True:
        fin = create_File.open_file_original(name_file_input)
        fout = create_File.open_file_update(name_file_input)

        subtitle_create.create_subtitle_update(fin, fout, value_time)
        print("Arquivo de legenda atualizado foi criado com sucesso!!!!")
    else:
        print("Não foi encontrado nenhum aquivo com esse nome")
        exit()

if __name__ == "__main__": 
    main()