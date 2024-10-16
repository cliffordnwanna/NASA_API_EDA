
# **NASA API Data Exploration Project**

## **Overview**
This project demonstrates how to interact with NASA's public APIs to fetch and analyze data. Specifically, it covers two main use cases:
1. Fetching and displaying the **Astronomy Picture of the Day (APOD)**.
2. Retrieving data on near-Earth objects (asteroids) using the **NeoWs (Near-Earth Object Web Service)** and processing it for analysis.

By working on this project, you will learn how to consume data from public APIs, handle JSON responses, process and clean the data, and save your results to a file. The project is implemented in **Python** using popular libraries such as **Requests**, **Pandas**, and **Matplotlib**.

## **Features**
- Fetch and display the **Astronomy Picture of the Day** using NASA's APOD API.
- Enhanced code to handle both images and other media types (e.g., videos).
- Fetch information about **near-Earth objects** (asteroids) from NASA's NeoWs API.
- Create clean, structured **DataFrames** with key details about each asteroid.
- Export processed data to **CSV** files for easy sharing and further analysis.
- Demonstrates robust **error handling** and **modular coding practices**.

## **Technologies Used**
- **Python**: Main programming language for the project.
- **Requests**: To handle HTTP requests to the NASA APIs.
- **Pandas**: For data processing and manipulation.
- **Matplotlib**: To display images in the notebook.
- **PIL (Python Imaging Library)**: To handle image processing.

## **Prerequisites**
Before running the project, ensure you have the following installed:
- Python 3.x
- `requests` library
- `pandas` library
- `matplotlib` library
- `PIL` (Pillow) library

You can install the necessary dependencies using:
```bash
pip install requests pandas matplotlib pillow
```

## **Setup Instructions**
1. **Get Your NASA API Key:**
   - Visit the [NASA Open APIs](https://api.nasa.gov/) portal.
   - Sign up to get your **API key**. This key is required to make requests to the NASA services.
   
2. **Clone the Repository:**
   ```bash
   git clone https://github.com/username/nasa-api-exploration.git
   cd nasa-api-exploration
   ```

3. **Configure the Project:**
   - Open the project code and replace the placeholder `YOUR_API_KEY_HERE` with your actual API key:
     ```python
     API_KEY = "YOUR_API_KEY_HERE"
     ```

4. **Run the Script:**
   Execute the script to see the **Astronomy Picture of the Day** and fetch data on **near-Earth objects**:
   ```bash
   python nasa_project.py
   ```

## **Project Structure**
```
nasa-api-exploration/
│
├── README.md           # Project description and setup instructions
├── nasa_project.py     # Main script with all functionalities
└── requirements.txt    # List of required Python packages
```

## **Usage**
### **1. Astronomy Picture of the Day (APOD)**
This module will fetch the **Astronomy Picture of the Day** and display it:
- The script first requests the APOD from the NASA API.
- It checks if the returned media is an image; if so, it displays it.
- If the media type is not an image (e.g., a video), it provides a message to the user.

### **2. Fetching Near-Earth Object (Asteroid) Data**
- The script retrieves a list of near-Earth objects from the NeoWs API.
- The information fetched includes **Asteroid ID**, **name**, **minimal estimated diameter**, **absolute magnitude**, and **relative velocity**.
- After processing, the data is saved to a **CSV file** named `asteroid_data.csv`.

## **Sample Output**
### **APOD**
![Sample APOD](sample_image_url.png)

### **Asteroid Data Preview**
| Asteroid ID | Asteroid Name | Minimal Estimated Diameter (km) | Absolute Magnitude | Relative Velocity (km/s) |
|-------------|---------------|---------------------------------|--------------------|--------------------------|
| 123456      | Apophis       | 0.37                            | 19.2               | 5.6                      |

## **Error Handling**
The script includes error handling for:
- **Network failures**: Will alert you if the API request fails due to a network issue.
- **Invalid API Key**: Will notify you if the provided API key is incorrect.
- **Non-image APOD content**: Will display an appropriate message if the content returned is not an image.

## **Future Enhancements**
- Add support for more NASA APIs, such as Mars Rover Photos and Earth Polychromatic Imaging Camera (EPIC).
- Implement a graphical user interface (GUI) for easier interaction.
- Automate daily fetching and storing of APOD and asteroid data using scheduled tasks (cron jobs).

## **Contributions**
Contributions are welcome! Feel free to open an **issue** or submit a **pull request** with improvements.

## **License**
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## **Contact**
For any inquiries or issues, please contact:
- **Name:** Chukwuma Nwanna
- **Email:** nwannachumaclifford@gmail.com


