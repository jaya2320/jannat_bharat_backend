# jannat_bharat_backend

### SET-UP Commands

1. Install Python using this url:-https://www.python.org/
2. Install pip
   ```
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   ```
   ```
   python3 get-pip.py
   ```
3. Check if pip is installed by running
    ```
    pip3 --version
    ```
4. Create a virtual environment 
   ```
   python3 -m venv myenv
   ```
5. Activate the virtual environment
   ```
   source myenv/bin/activate
   ```

#### Libraries to install for running the current project smoothly

   ```
     pip install django-ckeditor
   ```
   ```
     pip install django-rest_framework 
   ```
   ```
     pip install Pillow
   ```
   ```
      pip install django-cors-headers
   ```

### Django Commands 

+ To run the project
   ```
    python manage.py runserver
   ```
+ To run migrations and add changes to db
  1.
     ```
      python manage.py makemigrations
     ```  
  2.
     ```
     python manage.py migrate
     ```
+ Creating superuser
   ```
    python manage.py createsuperuser
   ```
  

