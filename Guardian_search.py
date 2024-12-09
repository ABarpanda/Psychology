import os
from multiprocessing import Pool

def search_in_chunk(args):
    """
    Searches for a word in a specific chunk of a file.

    Args:
        args (tuple): Contains (file_path, start_byte, end_byte, word_to_search).

    Returns:
        list: List of line numbers where the word is found in the chunk.
    """
    file_path, start_byte, end_byte, word_to_search = args
    found_lines = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        file.seek(start_byte)
        chunk = file.read(end_byte - start_byte)
        for line_number, line in enumerate(chunk.splitlines(), start=1):
            if word_to_search in line:
                found_lines.append(line_number + start_byte)
    return found_lines

def split_file_into_chunks(file_path, num_chunks):
    """
    Splits the file into chunks for parallel processing.

    Args:
        file_path (str): Path to the file.
        num_chunks (int): Number of chunks to create.

    Returns:
        list: List of tuples containing (start_byte, end_byte) for each chunk.
    """
    file_size = os.stat(file_path).st_size
    chunk_size = file_size // num_chunks
    chunks = []

    for i in range(num_chunks):
        start_byte = i * chunk_size
        end_byte = file_size if i == num_chunks - 1 else (i + 1) * chunk_size
        chunks.append((start_byte, end_byte))
    
    return chunks

def parallel_search(file_path, word_to_search, num_processes):
    """
    Searches for a word in a file using multiprocessing.

    Args:
        file_path (str): Path to the file.
        word_to_search (str): Word to search for.
        num_processes (int): Number of processes to use.

    Returns:
        list: List of line numbers where the word is found.
    """
    # Split the file into chunks
    chunks = split_file_into_chunks(file_path, num_processes)
    
    # Prepare arguments for each process
    args = [(file_path, start, end, word_to_search) for start, end in chunks]

    # Use multiprocessing pool to process chunks in parallel
    with Pool(num_processes) as pool:
        results = pool.map(search_in_chunk, args)
    
    # Combine results from all processes
    return [line for result in results for line in result]

# Example usage
if __name__ == "__main__":
    file_path = "large_text_file.txt"
    word_to_search = "example"
    num_processes = 4  # Number of CPU cores to use

    result = parallel_search(file_path, word_to_search, num_processes)
    if result:
        print(f"'{word_to_search}' found on lines: {result}")
    else:
        print(f"'{word_to_search}' not found in the file.")


'''

def search_multiple_words_in_file(file_path, words_to_search):
    """
    Searches for multiple words in a text file.
    
    Args:
        file_path (str): Path to the text file.
        words_to_search (list): List of words to search for.
    
    Returns:
        dict: Dictionary with words as keys and line numbers as values.
    """
    results = {word: [] for word in words_to_search}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            for word in words_to_search:
                if word in line:
                    results[word].append(line_number)
    return results

file_path = "new_text_dataset.txt"
words_to_search = ["example", "target", "missing"]

results = search_multiple_words_in_file(file_path, words_to_search)
for word, lines in results.items():
    if lines:
        print(f"'{word}' found on lines: {lines}")
    else:
        print(f"'{word}' not found in the file.")
'''