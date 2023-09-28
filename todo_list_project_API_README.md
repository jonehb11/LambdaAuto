

---

# To-Do List API

The To-Do List API is a simple backend application built with Python and FastAPI. It allows users to manage their to-do lists by providing CRUD (Create, Read, Update, Delete) operations for tasks.

## Features

- Create new tasks
- Retrieve a list of tasks
- Retrieve a specific task by ID
- Update task details
- Delete tasks

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite (for the database)

## Getting Started

### Prerequisites

- Python 3.6+
- pip package manager
- Git (optional)

### Installation

1. Clone the repository (if you haven't already):

   ```bash
   git clone https://github.com/yourusername/todo-list-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd todo-list-api
   ```

3. Create a virtual environment :

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

To start the To-Do List API, run the following command:

```bash
uvicorn main:app --reload
```

You can now access the API at [http://localhost:8000](http://localhost:8000).

## API Endpoints

- **POST /tasks/**: Create a new task.
- **GET /tasks/**: Retrieve a list of tasks.
- **GET /tasks/{task_id}**: Retrieve a specific task by ID.
- **PUT /tasks/{task_id}**: Update task details.
- **DELETE /tasks/{task_id}**: Delete a task.

## Usage Examples

Here are some example requests you can make to the API:

- **Create a Task**:

  ```http
  POST /tasks/
  {
      "title": "Buy groceries",
      "description": "Milk, eggs, bread"
  }
  ```

- **Retrieve Tasks**:

  ```http
  GET /tasks/
  ```

- **Retrieve a Specific Task**:

  ```http
  GET /tasks/{task_id}
  ```

- **Update a Task**:

  ```http
  PUT /tasks/{task_id}
  {
      "title": "Buy groceries",
      "description": "Milk, eggs, bread, and cheese"
  }
  ```

- **Delete a Task**:

  ```http
  DELETE /tasks/{task_id}
  ```


---

