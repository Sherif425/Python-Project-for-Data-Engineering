import glob
import pandas as pd

def extract():
    # create an empty dataframe to hold extracted data
    extracted_data = pd.DataFrame(columns=['name', 'height', 'weight'])                                  
    
    # read all CSV files in the current directory
    for csvfile in glob.glob("*.csv"):
        extracted_data = extracted_data.append(pd.read_csv(csvfile), ignore_index=True)

    # read all json files in the current directory
    for jsonfile in glob.glob("*.json"):
        extracted_data = extracted_data.append(pd.read_json(jsonfile), ignore_index=True)

    return extracted_data


def transform(data):
    # convert height from inches to centimeters
    data['height'] = round(data['height'] * 0.0254 ,2)
    
    # convert weight from pounds to kilograms
    data['weight'] = round(data['weight'] * 0.453592, 2)
    
    return data

def load(targetfile, data_to_load):
    # save the transformed data to a CSV file
    data_to_load.to_csv(targetfile, index=False)
    targetfile = "transformed_data.csv"

    load(targetfile, transform(extract()))

from datetime import datetime
def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    timestamp = datetime.now().strftime(timestamp_format)

    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')
    # simple logging function
    print(f"LOG: {message}")



if __name__ == "__main__":
    log("ETL Job Started")
    extracted_data = extract()
    log(f"Extracted {len(extracted_data)} records")
    transformed_data = transform(extracted_data)
    log("Transformation complete")
    load("transformed_data.csv", transformed_data)
    log("ETL Job Ended")

    