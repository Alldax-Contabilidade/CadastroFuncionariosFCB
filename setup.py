import sys
from cx_Freeze import setup, Executable


base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

executables = [
    Executable("arquivo_principal.py", base=base)
]

buildOptions = dict(
    packages=[],
    includes=["openpyxl", "pyodbc"],
    include_files=["banco_dados", "bases", "lista_util"],
    excludes=[]
)

setup(
    name="AppCadastroFCB",
    description="Automação de cadastros dos Funcionarios",
    options=dict(build_exe=buildOptions),
    executables=executables
)