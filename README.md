# FastAPI Summarizer API

This FastAPI project provides a simple API for text summarization using the Hugging Face Transformers library.


## Endpoint

### Summarize Text
- **Endpoint:** `/summarize`
- **Method:** `POST`
- **Parameters:**
  - `long_string` (str, required): The long text to be summarized.
  - `max_length `  (int, optional): Maximum length of the summary (default: 130).
  - `min_length ` (int, optional): Minimum length of the summary (default: 30).
  

### Contributing

If you'd like to contribute to this project, follow these steps:
- **Parameters:**
  - `Fork the repository.` 
  - `Create a new branch for your feature: git checkout -b feature-name.` 
  - `Make your changes and commit them: git commit -m 'Add new feature'.` 
  - `Push to the branch: git push origin feature-name.` 
  - `Submit a pull request.` 
  

  Example Request:
```request
 {
  "long_string": "Your long text goes here...",
  "max_length": 130,
  "min_length": 30
}
