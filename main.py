def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def summarize_text(text, sentence_count=2):
    sentences = text.split(".")
    selected_sentences = sentences[:sentence_count]

    summary = ".".join(selected_sentences).strip()

    if summary:
        summary += "."

    return summary


def main():
    file_path = "files/sample.txt"
    content = read_text_file(file_path)

    summary = summarize_text(content)

    print("Summary:")
    print(summary)


if __name__ == "__main__":
    main()