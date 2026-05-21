import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def read_text_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None


def summarize_with_ai(text):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
        Summarize the following text clearly and simply.

        Text:
        {text}
        """
    )

    return response.output_text


def main():
    file_path = input("Enter the path to your text file: ")

    content = read_text_file(file_path)

    if content is None:
        print("Error: File not found. Please check the file path.")
        return

    summary = summarize_with_ai(content)

    print("\nAI Summary:")
    print(summary)


if __name__ == "__main__":
    main()