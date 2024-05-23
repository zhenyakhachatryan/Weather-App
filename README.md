##  "Weather App" 
A simple web application that provides weather information for different locations. The app fetches data from a weather API and displays the current weather, temperature, humidity, and other relevant information.

## Features

- Search for weather by city name
- Display current weather conditions
- Show temperature, humidity and more

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/zhenyakhachatryan/Weather-App.git
    cd Weather-App
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up your environment variables. Create a `.env` file in the root directory and add your API key:

    ```plaintext
    API_KEY=YOUR_API_KEY
    ```

6. Run the application:

    ```bash
    flask run
    ```

7. Open your browser and go to `http://127.0.0.1:5000`.

## Usage

1. Enter the name of a city in the search bar.
2. Click the "Search" button.
3. View the current weather information for the specified city.

## Technologies Used

- Python
- Flask
- HTML/CSS
- Weather API (OpenWeatherMap)

##Contact

For questions or support, please contact me at khachatryanzhenya3@gmail.com.

Thank you for using Weather App!
