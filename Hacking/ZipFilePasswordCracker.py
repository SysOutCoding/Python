from datetime import timedelta
import time
import itertools
import zipfile
import string
import zlib


def crack_zip(src, min_length=1, max_length=None, chars=string.printable.strip()):
    print("\u001b[32m[Coded by Paul]")
    time.sleep(3)
    start = time
    count = 1
    with zipfile.ZipFile(src, 'r') as zf:
        while True:

            if max_length is not None:
                if min_length == max_length+1:
                    input('Scan wurde auf MAX Länge angepasst. Drücke Enter...')
                    raise SystemExit

            for pwd in itertools.product(chars, repeat=min_length):
                try:
                    zf.extractall(pwd=bytes(''.join(pwd), encoding='utf-8'))
                    fmt = "\n+{}+\n|{:^88}|\n|{:^88}|\n+{}+"
                    return print(fmt.format(f"{'-'*34}_!PASSWORT_GEFUNDEN!_{'-'*34}",
                                            "[+] Passwort GEFUNDEN!",
                                            f"Versuche: {count} | Passwort: {''.join(pwd)} | "
                                            f"Vergangene Zeit: {timedelta(seconds=time()-start)}", '-'*88))
                except (RuntimeError, zlib.error, zipfile.BadZipFile):
                    print(f"[{count}] [-] Passwort Falsch: {''.join(pwd)} | "
                          f"Vergangene Zeit: {timedelta(seconds=time()-start)}")
                    count += 1
            min_length += 1


if __name__ == '__main__':
    crack_zip('asd.zip', min_length=1, chars=string.ascii_lowercase)
    input('\nDrücke Enter...')

