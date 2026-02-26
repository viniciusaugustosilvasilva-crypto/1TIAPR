import argparse
import locale
import os
import tempfile

def read_lines(path):
    for enc in ('utf-8', 'latin-1'):
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read().splitlines()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("Unable to decode file with utf-8 or latin-1")

def write_lines_atomic(path, lines, encoding='utf-8'):
    dirpath = os.path.dirname(os.path.abspath(path)) or '.'
    with tempfile.NamedTemporaryFile('w', encoding=encoding, dir=dirpath, delete=False) as tf:
        tf.write('\n'.join(lines))
        tf.write('\n' if lines and not lines[-1].endswith('\n') else '')
        tmpname = tf.name
    os.replace(tmpname, path)

def sort_file(input_path, output_path):
    try:
        locale.setlocale(locale.LC_COLLATE, '')
    except Exception:
        pass
    lines = read_lines(input_path)
    key = lambda s: locale.strxfrm(s.casefold())
    lines.sort(key=key)
    write_lines_atomic(output_path, lines)

def main():
    p = argparse.ArgumentParser(description='Ordena linhas de um arquivo texto e salva em outro arquivo.')
    p.add_argument('input', help='arquivo de entrada')
    p.add_argument('output', help='arquivo de saída')
    args = p.parse_args()
    sort_file(args.input, args.output)

if __name__ == '__main__':
    main()