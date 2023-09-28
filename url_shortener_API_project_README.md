

---

# URL Shortener

The URL Shortener is a simple backend application built with Python, FastAPI, and a SQL database. It allows users to shorten long URLs and provides a redirection service to the original URLs using unique short URLs.

## Features

- Shorten long URLs to unique short URLs
- Redirect to original URLs using short URLs
- Persistence of URL mappings in a SQL database



### Installation

1. Clone the repository (if you haven't already):

   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   ```

2. Navigate to the project directory:

   ```bash
   cd url-shortener
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To start the URL Shortener application, run the following command:

```bash
uvicorn main:app --reload
```

You can now access the API at [http://localhost:8000](http://localhost:8000).

## API Endpoints

- **POST /shorten**: Shorten a long URL.
- **GET /{short_url}**: Redirect to the original URL using a short URL.

## Usage Examples

Here are some example requests you can make to the API:

- **Shorten a URL**:

  ```http
  POST /shorten
  {
      "original_url": "https://www.example.com/very/long/url/to/somewhere"
  }
  ```

- **Redirect to Original URL**:

  Access the shortened URL, e.g., [http://localhost:8000/abc123](http://localhost:8000/abc123), and you will be redirected to the original URL.

