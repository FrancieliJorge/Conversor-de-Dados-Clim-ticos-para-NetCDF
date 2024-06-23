import os
import subprocess
import pandas as pd
from glob import glob
from datetime import datetime

# Definir intervalo de datas e filtrar para incluir apenas os dias 1 e 16 de cada mês
_rodadas = pd.date_range("19991101T00", "20110316T00", freq='1D')
rodadas = [rod for rod in _rodadas if rod.day in [1, 16]]

# Converter arquivos .ctl para .nc
for rod in rodadas:
    paths = sorted(glob(rod.strftime("%Y%m%d%H/*.ctl")))
    for path in paths:
        path_in = path
        path_out = path.replace('.ctl', '.nc')
        cmd = f"cdo -f nc import_binary {path_in} {path_out}"
        print(cmd)
        subprocess.check_call(cmd, shell=True)

# Combinar arquivos NetCDF para membros do conjunto
for rod in rodadas:
    members = list(range(1, 13))
    for m in members:
        m = str(m).zfill(2)
        m_input = rod.strftime(f"%Y%m%d%H/*_{m}_*.nc")
        m_output = rod.strftime(f"%Y%m%d%H/member{m}.nc")
        if not os.path.isfile(m_output):
            cmd = f'cdo mergetime {m_input} {m_output}'
            print(cmd)
            try:
                subprocess.check_call(cmd, shell=True)
            except:
                print(f'pass: {cmd}')
        else:
            print(f'done: {m_output}')

