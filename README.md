# PORTFOLIO-API-INTEGRATION-AND-DATA-VISUALIZATION

**Name**: Tanish Kini

**Company**: CODETECH IT SOLUTIONS

**ID**: CT08ERX

**Domain**: Python Programming

**Duration**: 20th December to 20th January

**Mentor**: Neela Santhosh Kumar

# OUTPUT OF THE TASK

![OUTPUT]![image](https://github.com/user-attachments/assets/f538ab98-bdc8-4f3a-b1e7-44c4a128c6d8)


# Project Overview: Weather Data Visualization and Analysis  
This project demonstrates how to fetch, parse, and visualize real-time weather data for a specified city using the OpenWeatherMap API. The goal is to provide an interactive and clear graphical representation of weather metrics, helping users analyze temperature trends and other key parameters.

---

## Key Components  

### Data Fetching  
- **API Integration**:  
  The project connects to the OpenWeatherMap API to retrieve live weather forecast data for a specified city.  
- **Functionality**:  
  The `fetch_weather_data` function constructs the API request URL, sends the request, and handles the response.  
  - If successful (HTTP status code 200), it returns JSON data.  
  - In case of failure, an error message is displayed to guide the user.  

---

### Data Parsing  
- **JSON Processing**:  
  The `parse_weather_data` function extracts relevant data (timestamps and temperature values) from the API response.  
- **DataFrame Creation**:  
  Using Pandas, the extracted data is organized into a structured DataFrame for easy manipulation and analysis.  

---

### Data Visualization  
- **Line Plot for Trends**:  
  The `plot_weather_data` function generates a clean and visually appealing line plot using Seaborn and Matplotlib.  
  - The plot shows temperature trends over time, complete with labeled axes, a title, and formatted timestamps for clarity.  
- **Customizable Graphs**:  
  Additional parameters, such as humidity or wind speed, can be added for richer insights.  

---

## Main Script Execution  
The script is designed to run seamlessly as a standalone program:  
1. Define the API key and specify the city.  
2. Fetch, parse, and visualize the weather data by calling the corresponding functions in sequence.  

---

## Usage Instructions  
1. **API Key Setup**:  
   Replace the placeholder API key with your valid OpenWeatherMap API key.  
2. **City Selection**:  
   Modify the `CITY` variable to analyze data for your desired location.  
3. **Run the Script**:  
   Execute the script to display a line plot of temperature trends for the specified city.  

---

## Dependencies  
This project uses the following Python libraries:  
- **requests**: For sending HTTP requests to the OpenWeatherMap API.  
- **matplotlib**: For creating static and interactive visualizations.  
- **seaborn**: For generating aesthetic and statistical graphics.  
- **pandas**: For data manipulation and creating DataFrames.  

---

## Potential Enhancements  
- **Error Handling**:  
  - Provide detailed messages when the city is not found or the API key is invalid.  
- **User Interaction**:  
  - Allow users to input the city name and API key through command-line arguments or a graphical user interface.  
- **Enhanced Visualizations**:  
  - Include additional weather parameters such as humidity, wind speed, or precipitation.  
  - Offer various visualization types (e.g., bar charts, scatter plots) or custom time intervals (e.g., daily, weekly).  
- **Data Export**:  
  - Enable exporting parsed data as a CSV file for external analysis.  

---

## Why This Project?  
This project serves as a hands-on example of integrating API data with Python applications to create meaningful visualizations. It is an excellent resource for those looking to improve their skills in data analysis, API integration, and Python programming.



