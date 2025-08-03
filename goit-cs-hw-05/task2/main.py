import requests
import re
import string
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt


# Завантаження тексту з URL
def fetch_text_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


# Функція map: розбиває текст на слова
def mapper(text_chunk):
    words = re.findall(r'\b\w+\b', text_chunk.lower())
    return Counter(words)


# Функція reduce: об'єднує часткові результати
def reducer(partials):
    total = Counter()
    for partial in partials:
        total.update(partial)
    return total


# Візуалізація топ-слів
def visualize_top_words(word_counts, top_n=10):
    top_words = word_counts.most_common(top_n)
    words, counts = zip(*top_words)
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.title(f"Топ-{top_n} слів за частотою")
    plt.ylabel("Частота")
    plt.xlabel("Слова")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Основний блок
def main():
    url = "https://www.gutenberg.org/files/1342/1342-0.txt"  # Наприклад, "Pride and Prejudice" Джейн Остін
    text = fetch_text_from_url(url)

    # Розбивка тексту на частини
    num_threads = 8
    chunk_size = len(text) // num_threads
    chunks = [text[i * chunk_size:(i + 1) * chunk_size] for i in range(num_threads)]

    # Обробка частин паралельно (Map)
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        map_results = list(executor.map(mapper, chunks))

    # Зведення результатів (Reduce)
    final_word_count = reducer(map_results)

    # Візуалізація
    visualize_top_words(final_word_count, top_n=10)


if __name__ == "__main__":
    main()
