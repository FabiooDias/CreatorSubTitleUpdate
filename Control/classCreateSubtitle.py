import Control.classCalculeTime
import re

class SubtitleCreate:

    def create_subtitle_update(self, fin, fout, value: float):
        time_regex = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}')
        time_update = Control.classCalculeTime.Calculator_time()

        for line in fin:
            time_old = time_regex.findall(line)
        
            if len(time_old) > 0:
                fout.write(time_update.line_time_update(time_old, value))
            else:
                fout.write(line)