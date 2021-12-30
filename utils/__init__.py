import math
import requests


def get_scoop(url):
    r = requests.get(url)

    return r.json()


def download_data(version, url, size="", arch="generic", os="multiplataforma"):
    return {
        'download_version': version,
        'download_url': url,
        'download_size': __from_bytes_to_human(size) if size != "" else "",
        'arquitectura': arch,
        'download_os': os
    }


def __from_bytes_to_human(size):

    log = math.log(int(size), __base)

    fixed = math.floor(log)
    exp = log - fixed

    precision = 2 if fixed > 1 else 1

    n = round( math.pow(__base, exp), precision)

    return f"{n:g} {__size_units[fixed]}".strip()


__size_units = [
    "", "KB", "MB", "GB","TB"
]

__base = 1024
