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
        You are a helpful assistant that summarizes documents.

        Summarize the text using this format:

        1. Short Summary:
        Write 2-3 sentences.

        2. Key Points:
        - List the most important ideas as bullet points.

        3. Main Takeaway:
        Write one final sentence explaining the most important message.

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
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    except FileNotFoundError:
        print("PDF Error: File was not found.")
        return None

    except Exception as error:
        print(f"PDF Error: {error}")
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