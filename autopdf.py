import pyttsx3
from PyPDF2 import PdfReader

# Open the PDF file
with open('book.pdf', 'rb') as file:
    pdfreader = PdfReader(file)
    num_pages = len(pdfreader.pages)

    # Initialize text-to-speech engine
    speaker = pyttsx3.init()

    # Read text from each page
    for page_num in range(num_pages):
        page = pdfreader.pages[page_num]
        text = page.extract_text()  # Use extract_text() instead of extractText()
        clean_text = text.strip().replace('\n', '')
        print(clean_text)

        # Convert text to speech and save to file
        speaker.save_to_file(clean_text, 'story.mp3')
        speaker.runAndWait()

    speaker.stop()



