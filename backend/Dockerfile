FROM python:3.10.5
WORKDIR /backend
COPY . .
RUN pip install .
EXPOSE 8000

# Command to run the FastAPI app for production
WORKDIR /
CMD ["gunicorn", "backend.app:create_app()", "-b", ":8000"]
