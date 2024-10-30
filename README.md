# Django REST Framework API Example

This is a simple Django project demonstrating basic CRUD operations for a `Data` model using the Django REST Framework.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nassrkhan/Django-Rest-API-Project.git
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Apply database migrations:
  ```bash python manage.py migrate```
4. Run the development server:
  ```bash python manage.py runserver```
The API will be accessible at http://127.0.0.1:8000/.

API Endpoints
1. Get Data
URL: /data/
Method: GET
Description: Retrieve a list of all data objects.
2. Post Data
URL: /data/new/

Method: POST

Description: Create a new data object.

Data Format:

json
Copy code
{
  "name": "Example Name",
  "description": "Example Description"
}
3. Get Data Detail
URL: /data/<int:pk>/
Method: GET
Description: Retrieve details of a specific data object.
4. Put Data
URL: /data/<int:pk>/edit/

Method: PUT

Description: Update details of a specific data object.

Data Format:

json
Copy code
{
  "name": "Updated Name",
  "description": "Updated Description"
}
5. Delete Data
URL: /data/<int:pk>/delete/
Method: DELETE
Description: Delete a specific data object.
Example Usage
Using curl
Create a new data object:

```bash curl -X POST -H "Content-Type: application/json" -d '{"name": "New Data", "description": "New Description"}' http://127.0.0.1:8000/data/new/```
Get all data:
```bash curl http://127.0.0.1:8000/data/```

