# MNIST Digit Generator

This is a simple web application built with Streamlit that displays handwritten digits from the famous MNIST dataset. You can interactively select a digit (from 0 to 9), and the application will fetch and display five random examples of that digit from the dataset.

## Features

-   **Interactive Digit Selection**: Use a simple slider to choose a digit.
-   **Random Image Display**: See 5 different handwritten examples for the selected digit.

## How to Run

This project is configured to run in a Dev Container, which makes setup seamless.


If you want to run it manually, ensure you have the dependencies from [`requirements.txt`](requirements.txt) installed:

```bash
pip install -r requirements.txt
```

Then run the Streamlit application:

```bash
streamlit run app.py
```

## Project Files

-   [`app.py`](app.py): The main Streamlit application script.
-   [`requirements.txt`](requirements.txt): A list of Python dependencies for the project.
-   [`.devcontainer/devcontainer.json`](.devcontainer/devcontainer.json): Configuration file for the development container.