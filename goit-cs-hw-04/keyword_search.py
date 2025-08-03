import os
import time
import threading
import multiprocessing
from queue import Queue as ThreadQueue
from multiprocessing import Queue as ProcessQueue

# === Конфігурація ===
SEARCH_KEYWORDS = ["error", "warning", "critical"]
TEXT_FILES_DIR = "text_files"  # Директорія з файлами

def get_text_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".txt")]

# === Загальна функція пошуку ===
def search_keywords_in_file(file_path, keywords):
    results = {keyword: [] for keyword in keywords}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            for keyword in keywords:
                if keyword.lower() in content:
                    results[keyword].append(file_path)
    except (FileNotFoundError, IOError) as e:
        print(f"[Помилка] Не вдалося відкрити файл {file_path}: {e}")
    return results

# === Threading реалізація ===
def thread_worker(file_list, keywords, queue):
    combined = {keyword: [] for keyword in keywords}
    for file_path in file_list:
        result = search_keywords_in_file(file_path, keywords)
        for k, v in result.items():
            combined[k].extend(v)
    queue.put(combined)

def run_threaded(files, keywords, num_threads=4):
    start = time.time()
    queue = ThreadQueue()
    threads = []
    chunk_size = len(files) // num_threads + 1

    for i in range(num_threads):
        chunk = files[i * chunk_size:(i + 1) * chunk_size]
        t = threading.Thread(target=thread_worker, args=(chunk, keywords, queue))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    final_result = {keyword: [] for keyword in keywords}
    while not queue.empty():
        partial = queue.get()
        for k, v in partial.items():
            final_result[k].extend(v)

    end = time.time()
    print(f"[Threading] Час виконання: {end - start:.4f} секунд")
    return final_result

# === Multiprocessing реалізація ===
def process_worker(file_list, keywords, queue):
    combined = {keyword: [] for keyword in keywords}
    for file_path in file_list:
        result = search_keywords_in_file(file_path, keywords)
        for k, v in result.items():
            combined[k].extend(v)
    queue.put(combined)

def run_multiprocessing(files, keywords, num_processes=4):
    start = time.time()
    queue = ProcessQueue()
    processes = []
    chunk_size = len(files) // num_processes + 1

    for i in range(num_processes):
        chunk = files[i * chunk_size:(i + 1) * chunk_size]
        p = multiprocessing.Process(target=process_worker, args=(chunk, keywords, queue))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    final_result = {keyword: [] for keyword in keywords}
    while not queue.empty():
        partial = queue.get()
        for k, v in partial.items():
            final_result[k].extend(v)

    end = time.time()
    print(f"[Multiprocessing] Час виконання: {end - start:.4f} секунд")
    return final_result

# === Головна функція ===
if __name__ == "__main__":
    all_files = get_text_files(TEXT_FILES_DIR)

    print("\n=== Запуск з Threading ===")
    result_threads = run_threaded(all_files, SEARCH_KEYWORDS)
    print(result_threads)

    print("\n=== Запуск з Multiprocessing ===")
    result_processes = run_multiprocessing(all_files, SEARCH_KEYWORDS)
    print(result_processes)
