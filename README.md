## 🧪 Testing with Postman

We provide both a **Postman collection** and a **Postman environment**:

- `postman_collection.json`
- `postman_environment.json`

### Steps
1. Open Postman → Import both files.
2. Select environment **Books Scraper Local**.
3. Run requests directly:
   - GET `{{BASE_URL}}/api/books`
   - GET `{{BASE_URL}}/api/books/{book_id}`
   - GET `{{BASE_URL}}/api/changes`

N.B: No need to type API keys — everything is pre-configured.
