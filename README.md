# Text Summarization API

This project is a FastAPI-based text summarization service that supports multiple traditional summarization algorithms from the `sumy` library. It is not based on large language models (LLMs) but uses classical approaches for summarization.

![b31c5c38-64ec-43bf-88d1-a8425ff1fe4a](https://github.com/user-attachments/assets/09f5321b-f67e-4752-b2f5-1c64bde332b9)

## Features

- Supports various summarization algorithms:
  - SumBasic
  - Luhn
  - Edmundson
  - LexRank
  - TextRank
  - LSA (Latent Semantic Analysis)
- Cleans the input text by removing unwanted characters and links.

## Requirements

- Python 3.8+
- FastAPI
- Pydantic
- sumy
- nltk
- numpy

## Installation

1. Clone the repository:
    ```sh
    git clone github.com/AmirTahaMim/SumSimple
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install fastapi pydantic sumy nltk numpy
    ```

4. Download the necessary NLTK data:
    ```sh
    python -c "import nltk; nltk.download('punkt')"
    ```

## Running the Application

1. Run the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```

2. The API will be available at `http://127.0.0.1:8000`.

## API Usage

### Endpoint

- **POST** `/summarize/`

### Request Body

```json
{
  "input_text": "Your base64 encoded text here",
  "summarizer": "LSA",
  "sentences_count": 5,
  "language": "english"
}
```

- `input_text`: The text to summarize (base64 encoded).
- `summarizer`: The summarization algorithm to use (default: LSA). Options: "SumBasic", "Luhn", "Edmundson", "LexRank", "TextRank", "LSA".
- `sentences_count`: The number of sentences for the summary (default: 5).
- `language`: The language of the text (default: "english").

### Example Request

```sh
curl -X POST "http://127.0.0.1:8000/summarize/" -H "Content-Type: application/json" -d '{
  "input_text": "VGhpcyBpcyBhIHNhbXBsZSB0ZXh0IHRvIHN1bW1hcml6ZS4uLi4=",  # Base64 encoded text
  "summarizer": "LSA",
  "sentences_count": 3,
  "language": "english"
}'
```

### Example Response

```json
{
  "summary": "This is the summarized text."
}
```

## Text Cleaning

The input text is cleaned by:
- Removing lines with '*' or fewer than 50 words.
- Removing markdown and HTML links.
- Removing URLs.
- Removing extra whitespace and unwanted characters.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.
```
