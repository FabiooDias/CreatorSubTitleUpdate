import os
from pathlib import Path
class File_Srt:

    def verifyFile(self, nameFile: str) -> bool:
        if Path(f'{nameFile.title()}.srt').suffix == '.srt':
            if (os.path.isfile(f'{nameFile.title()}.srt')):
                return True
            else:
                return False