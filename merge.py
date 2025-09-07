def merge_files(base_name, output_file):
    part_num = 0
    with open(output_file, 'wb') as outfile:
        while True:
            part_filename = f"{base_name}.part{part_num:03d}"
            try:
                with open(part_filename, 'rb') as infile:
                    outfile.write(infile.read())
                print(f"Birleştirildi: {part_filename}")
                part_num += 1
            except FileNotFoundError:
                break
    print(f"Tüm parçalar birleştirildi -> {output_file}")

if __name__ == "__main__":
    merge_files("ti_cgt_armllvm_4.0.1.LTS_windows-x64_installer.zip", "ti_cgt_armllvm_4.0.1.LTS_windows-x64_installer.zip")
