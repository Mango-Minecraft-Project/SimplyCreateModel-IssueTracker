import zipfile
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
PROCESS_DIR = "mod"
RESULT_FILENAME = "Simply-Create-Model-Mod-v1.2"


current_folder_path = CURRENT_DIR / PROCESS_DIR

current_jar_path = CURRENT_DIR / f"{RESULT_FILENAME}.jar"
current_jar_path.unlink(missing_ok=True)

with zipfile.ZipFile(current_jar_path, "w") as zf:
    for file in (current_folder_path).rglob("*"):
        zf.write(file, file.relative_to(current_folder_path))
