import argparse
import re
from pathlib import Path

def find_word_in_file(word: str, file_path: Path):
    pattern = re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE)
    found_lines = []
    with file_path.open('r', encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f, start=1):
            if pattern.search(line):
                found_lines.append((i, line.rstrip('\n')))
    return found_lines

def main():
    parser = argparse.ArgumentParser(description='Procura uma palavra em um arquivo e mostra as linhas.')
    parser.add_argument('word', nargs='?', help='palavra a procurar')
    parser.add_argument('file', nargs='?', help='caminho do arquivo de texto')
    args = parser.parse_args()

    word = args.word or input('Digite a palavra a procurar: ').strip()
    file_input = args.file or input('Digite o caminho do arquivo: ').strip()
    file_path = Path(file_input)

    if not file_path.is_file():
        print(f'Arquivo não encontrado: {file_path}')
        return

    results = find_word_in_file(word, file_path)
    if results:
        print(f'A palavra "{word}" foi encontrada nas linhas:')
        for lineno, text in results:
            print(f'{lineno}: {text}')
    else:
        print(f'A palavra "{word}" não foi encontrada em {file_path.name}.')

if __name__ == '__main__':
    main()