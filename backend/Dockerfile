FROM python:3.10.5
WORKDIR /backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

# Command to run the FastAPI app for production
CMD ["gunicorn", "app:create_app()", "-b", ":8000"]
