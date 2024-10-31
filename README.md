# Bar Chart Animation

This project visualizes the popularity of various programming languages over time using a bar chart race animation. The animation showcases how different programming languages have trended over the years, making it easy to see how certain languages have gained or lost popularity.

## Overview

The project reads data from a CSV file containing monthly popularity stats for each programming language, combines the year and month columns to create a time index, and then generates a bar chart race animation.

![Sample Animation](video.mp4)

## Features

- **Smooth animation**: Configurable speed and smoothness of bar transitions.
- **Customizable**: Adjust the number of bars displayed, colors, and orientation.
- **Supports multiple languages**: Displays popularity trends for 10 different programming languages.

## Data Format

The input CSV file should have the following columns:

**Year:** Year of the data entry.
**Months:** Month of the data entry.

Example structure of `data.csv:`
```csv
Year,Months,Python,Java,JavaScript,C++,C#,PHP,R,Swift,Go,TypeScript
2018,January,25,30,22,15,18,10,7,6,5,3
2018,February,26,29,23,14,18,10,8,6,5,4
```
## Usages

Follow the mentioned procedure to run this project in your local system.
 - Clone or Download the Repository
```bash
   git clone https://github.com/cambridgeitcollege/GraphAnimation.git
   cd GraphAnimation
```
 - Create the Virtual Environment Before installing the requirements. 
 ```Bash
    python3 -m virtualenv venv #For Linux User
 ```
  - Activate the Virtual Environment
  ```bash
    source venv/bin/activate  #For Linux and MAC User
     Note: It is not Necessary to Create Virtual Environment but recommanded.
  ``` 
 - Install the Requirements
```bash
    pip install -r requirements.txt
```
 - Run the Script
 ```bash
   python3 main.py    
 ```

## Contributing
We welcome contributions! If you'd like to contribute to this Mero Share IPO Filler Script, please check out our [Contribution Guidelines](Contribution.md).

## Code of Conduct
Please review our [Code of Conduct](CodeOfConduct.md) before participating in this Script.

## License
This project is licensed under the MIT [License](LICENSE).
