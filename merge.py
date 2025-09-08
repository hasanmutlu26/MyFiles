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
    merge_files("sysconfig-1.25.0_4268-setup.zip", "sysconfig-1.25.0_4268-setup.zip")
