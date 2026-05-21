def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def main():
    file_path = "files/sample.txt"
    content = read_text_file(file_path)

    print("File Content:")
    print(content)


if __name__ == "__main__":
    main()