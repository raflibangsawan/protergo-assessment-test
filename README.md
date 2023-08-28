# Protergo Ecommerce Scraper

This scraper is created as part of the Protergo Programming Assessment Test. I will take an example of scraping data from https://e-katalog.lkpp.go.id/. In this case, I will be scraping the data from ‘Alat Olahraga’ category which can be accessed from https://e-katalog.lkpp.go.id/id/search/produk/alat-olahraga/72?tkdn_produk=&jenis_produk=. The scraped data then will be saved and displayed as CSV. For data scraping I will be using Python with the help of the Selenium library. I also will be using Chrome webdriver to access the web using Google Chrome.

## Prerequisites

Before you can use this program, ensure you have the following prerequisites installed:

- **Python:** This project is developed using Python. Preferably, use Python version 3.9.xx. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

- **Webdriver:** You will need a webdriver that matches the version of your browser. Popular choices include:
  - [Chrome WebDriver](https://sites.google.com/chromium.org/driver/)
  - [Firefox WebDriver](https://github.com/mozilla/geckodriver/releases)

Make sure to download and configure the webdriver correctly.

## Installation

To set up this project, follow these steps:

1. **Clone the Repository:** Start by cloning this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/protergo-ecommerce-scraper.git
   cd protergo-ecommerce-scraper
   ```

2. **Create a Python Virtual Environment (optional but recommended):** It's a good practice to work within a virtual environment to keep project dependencies isolated.

   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   # On Windows:
   .\venv\Scripts\activate
   # On macOS and Linux:
   source venv/bin/activate
   ```

3. **Install Project Dependencies:** Use pip to install the required packages listed in requirements.txt.
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure WebDriver:** Ensure that the WebDriver is correctly configured and matches your browser's version. Update the WebDriver path in the project files as needed.
