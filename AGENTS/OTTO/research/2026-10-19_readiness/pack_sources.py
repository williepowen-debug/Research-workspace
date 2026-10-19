"""Pack captured originals/extracted text; canonical committed source bundle."""
import gzip
import io
from pathlib import Path
import tarfile

B=Path(__file__).resolve().parent
with (B/'sources.tar.gz').open('wb') as dest:
    with gzip.GzipFile(fileobj=dest,mode='wb',mtime=0,filename='') as gz:
        with tarfile.open(fileobj=gz,mode='w') as archive:
            for p in sorted((B/'sources').iterdir()):
                if not p.is_file():continue
                data=p.read_bytes()
                entry=tarfile.TarInfo(str(p.relative_to(B)))
                entry.size=len(data);entry.mode=0o644;entry.mtime=0
                archive.addfile(entry,io.BytesIO(data))
print('Packed source bundle', (B/'sources.tar.gz').stat().st_size, 'bytes')
