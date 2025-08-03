import argparse
import asyncio
import logging
from pathlib import Path
import aiofiles
import aiofiles.os
import shutil

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def copy_file(file_path: Path, output_dir: Path):
    try:
        ext = file_path.suffix[1:] or "no_extension"
        dest_dir = output_dir / ext
        await aiofiles.os.makedirs(dest_dir, exist_ok=True)
        dest_path = dest_dir / file_path.name

        # Використовуємо loop.run_in_executor для копіювання, оскільки shutil.copy є блокуючим
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, shutil.copy2, file_path, dest_path)

        logger.info(f"Copied: {file_path} -> {dest_path}")
    except Exception as e:
        logger.error(f"Failed to copy {file_path}: {e}")


async def read_folder(source_dir: Path, output_dir: Path):
    tasks = []
    async for entry in async_walk(source_dir):
        if entry.is_file():
            tasks.append(copy_file(entry, output_dir))
    await asyncio.gather(*tasks)


async def async_walk(dir_path: Path):
    for entry in dir_path.rglob("*"):
        yield entry


def parse_arguments():
    parser = argparse.ArgumentParser(description="Sort files by extension asynchronously.")
    parser.add_argument("source", type=str, help="Source folder to read files from.")
    parser.add_argument("output", type=str, help="Output folder to store sorted files.")
    return parser.parse_args()


def main():
    args = parse_arguments()
    source = Path(args.source)
    output = Path(args.output)

    if not source.exists() or not source.is_dir():
        logger.error(f"Source directory '{source}' does not exist or is not a directory.")
        return

    try:
        asyncio.run(read_folder(source, output))
    except Exception as e:
        logger.exception(f"Unexpected error during processing: {e}")


if __name__ == "__main__":
    main()
