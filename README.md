# Mineral_calculation
## Description
This script provides a web application designed for calculating the cost of mineral extraction, considering key factors such as employee salaries, equipment costs, and office rent. The application allows users to input various parameters related to the extraction process, and it calculates the total cost of mineral extraction based on these factors. This tool is useful for businesses in the mining industry, enabling quick and accurate cost estimations to support decision-making.

## Functional Description
The script performs the following tasks:
1. **Input Data Collection**: The user provides input for various parameters, such as the type of mineral, tonnage, equipment used, number of workers, average salary, office rent, and the type of work performed.
2. **Salary and Office Cost Calculation**: It calculates the total salary for workers and the office cost based on the number of workers, their average salary, and the office rent.
3. **Extraction Cost Calculation**: The script calculates the total cost of extraction by adding the costs of various equipment and work types, as well as the salaries and office costs.
4. **Cost Output**: After processing the inputs, the script provides the final cost of extraction, which helps businesses in budgeting and planning their operations.

## How It Works
1. **Initialization**: The Dash application is initialized and serves as the web interface for user interaction.
2. **User Input**: Users provide input via form fields, sliders, dropdowns, and checklists to specify the necessary data.
3. **Backend Calculation**: The input data is processed through functions that calculate worker salaries, office costs, and equipment-specific extraction costs.
4. **Cost Calculation**: Based on the inputs, the script determines the total cost of mineral extraction, taking into account all variables provided by the user.
5. **Result Display**: The application displays the calculated extraction cost in a user-friendly format, showing the total amount for easy reference.

## Input Structure
To run the application, the following inputs are required:
1. **General Information**: 
    - Quarry name (text input)
2. **Mineral Type**: 
    - Dropdown selection of mineral type (e.g., "щебень", "известняк", "песчаник")
3. **Tonnage**: 
    - Numeric input specifying the extracted mineral volume in tons.
4. **Work Type**: 
    - Radio button selection for the type of work being performed (e.g., "поиск-розыскные работы", "добыча полезных ископаемых в карьере", "добыча полезных ископаемых в шахте").
5. **Extraction Dates**: 
    - Date picker range for the period of extraction.
6. **Office Rent**: 
    - Numeric input for office rent cost.
7. **Equipment List**: 
    - Checklist for available equipment (e.g., "буровой станок", "экскаваторы", "конвейер").
8. **Workers and Salary**: 
    - Number of workers (slider input).
    - Average salary (slider input).

## Technical Requirements
To run this application, the following are required:
1. **Python 3.x**
2. **Installed Libraries**: 
    - Dash
    - pandas
    - numpy
    - Pillow (for image processing)
    - base64
3. **Local Environment**: The app runs on a local server (http://127.0.0.1:8050/) and requires a Python environment where the necessary libraries are installed.

## Usage
1. Ensure all required libraries are installed in your Python environment.
2. Set up the paths and input parameters (e.g., the image for display).
3. Run the script to start the Dash web application.
4. Interact with the web interface by providing input data, such as the mineral type, tonnage, work type, and more.
5. Click on the "Пересчитать цену" button to calculate and display the extraction cost.

## Example Output
The output will display the following:
1. **Total Extraction Cost**: The total cost of mineral extraction based on the input parameters.
2. **Cost Breakdown**: Detailed information about the various components contributing to the total cost (e.g., salaries, equipment costs, office rent).

## Conclusion
This tool provides an efficient and user-friendly way for businesses in the mining industry to calculate the total cost of mineral extraction. It streamlines the estimation process, allowing for accurate and timely financial planning, and improves decision-making by considering all relevant cost factors.
