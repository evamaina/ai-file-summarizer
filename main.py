import os
from dotenv import load_dotenv
from openai import OpenAI
from PyPDF2 import PdfReader


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

def read_pdf_file(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text
    except Exception:
        return None

def main():
    print("Program started")
    file_path = input("Enter the path to your file: ")

    if file_path.endswith(".txt"):
        content = read_text_file(file_path)
    elif file_path.endswith(".pdf"):
        content = read_pdf_file(file_path)
    else:
        print("Error: Unsupported file type. Use .txt or .pdf")
        return

    if content is None:
        print("Error: File not found or could not be read.")
        return

    if not content.strip():
        print("Error: The file is empty.")
        return

    summary = summarize_with_ai(content)

    print("\nAI Summary:")
    print(summary)


if __name__ == "__main__":
    main()