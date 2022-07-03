"""
    File Name: 8.3.1 压缩文件
    Description:
    Author: 15920313768@163.com
    Date: 2022/7/3 17:26
"""
import tarfile
import zipfile
from pathlib import Path


path = 'test'
newzip = zipfile.ZipFile('new.zip', 'w')

# 压缩所有文件
for p in Path(Path.cwd()).rglob('*'):
    newzip.write(p, compress_type=zipfile.ZIP_DEFLATED)

newzip.close()
print('done!')

# .tar.gz格式的压缩文件，使用gzip算法，可选bz2，表示bzip2，或xz模式，采用lzma算法
tar = tarfile.open('new.tar.gz', 'w:gz')

for p in Path(Path.cwd()).rglob('*'):
    tar.add(p)

tar.close()
print('done!')