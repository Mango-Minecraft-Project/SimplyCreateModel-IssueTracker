import zipfile
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
PROCESS_DIRS = {
    "mod": "Simply-Create-Model-Mod-v1.2",
}



for process_dir, result_filename in PROCESS_DIRS.items():
    current_jar_path = CURRENT_DIR / f"{result_filename}.jar"
    current_jar_path.unlink(missing_ok=True)

    current_folder_path = CURRENT_DIR / process_dir
    with zipfile.ZipFile(current_jar_path, "w") as zf:
        for file in (current_folder_path).rglob("*"):
            zf.write(file, file.relative_to(current_folder_path))
