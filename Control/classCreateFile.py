class Create_Open_File:
    def open_file_original(self, name_file_input: str):
        fin =  open(f"{name_file_input}.srt", 'rt', encoding="utf8")
        return fin                                 
    
    def open_file_update(self, name_file_input: str):
        fout = open(f"{name_file_input}_atualizada.srt", 'wt', encoding="utf8")
        return fout