# waterquality / server-1

This a Django Webapp, for performing following tasks in the given order:

1. Receive data via `POST` request, from Hardware.
2. Post Process data.
3. Store data in MongoDB container.

### Let's get started!

- **Step 0**: Install Python3. Set `python` and `pip` as environment variable 

- **Step 1**: From CMD/Terminal, Navigate to `path/to/waterquality/dashboard`. Install Dependencies 

    ```bash
    pip install -r requirements.txt
    ```

- **Step 3**: Spin the Django Server

    ```bash
    python3 manage.py runserver
    ```