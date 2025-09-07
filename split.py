import os

def split_file(file_path, chunk_size_mb=90):
    chunk_size = chunk_size_mb * 1024 * 1024  # MB -> byte
    file_size = os.path.getsize(file_path)
    base_name = os.path.basename(file_path)

    with open(file_path, 'rb') as f:
        part_num = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            part_filename = f"{base_name}.part{part_num:03d}"
            with open(part_filename, 'wb') as chunk_file:
                chunk_file.write(chunk)
            print(f"Oluşturuldu: {part_filename}")
            part_num += 1

if __name__ == "__main__":
    split_file("ti_cgt_armllvm_4.0.1.LTS_windows-x64_installer.zip")  # buraya kendi dosya adını yaz
