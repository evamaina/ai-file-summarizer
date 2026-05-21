import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


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
    file_path = "files/sample.txt"
    content = read_text_file(file_path)

    summary = summarize_with_ai(content)

    print("AI Summary:")
    print(summary)


if __name__ == "__main__":
    main()