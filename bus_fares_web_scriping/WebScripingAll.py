#####MEGABUS#######
###################

# import numpy as np
# import pandas as pd
# import requests
# import json
# from datetime import datetime, timedelta
# import time
# import os

# # Initialize the starting dates
# departure_date_from_start = datetime(2024, 10, 28)
# departure_date_to_start = datetime(2024, 10, 29)

# # Define the number of days to iterate (from 2024-10-28 to 2024-11-03)
# days_to_iterate = 6

# # File to save the data
# output_file = r"C:\Users\Luis.ParraMorales\Documents\Python Code\Ana Rodriguez\Rail Fares - Web Scriping\Megabus Runs\Megabusquotes_data.csv"

# # Check if the file already exists (to handle appending data)
# if os.path.exists(output_file):
#     df_saved = pd.read_csv(output_file)
#     all_quotes = df_saved.to_dict('records')  # Convert to list of dicts for appending new data
# else:
#     all_quotes = []

# # Read the Excel file containing O-D pairs
# OD_pairs = pd.read_excel(r"C:\Users\Luis.ParraMorales\Documents\Python Code\Ana Rodriguez\Rail Fares - Web Scriping\NWEC - Origin and Destination List - Final.xlsx", sheet_name='O-D Fares')

# # Filter rows where Operator is Megabus
# megabus_rows = OD_pairs[OD_pairs['Operator'] == 'Megabus']

# # Define batch size (20 ODs per batch)
# batch_size = 20

# # Split the rows into batches
# batches = [megabus_rows[i:i+batch_size] for i in range(0, len(megabus_rows), batch_size)]

# # Headers to mimic a browser request
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }

# # Iterate over each batch of O-D pairs
# for batch_index, batch in enumerate(batches):
#     print(f"Processing batch {batch_index + 1}/{len(batches)}")
    
#     # Iterate over each row in the batch
#     for index, row in batch.iterrows():
#         origin_id = row['Origin_ID']
#         destination_id = row['Destination_ID']
        
#         # Iterate over the dates
#         for i in range(days_to_iterate + 1):
#             try:
#                 # Update the departure dates
#                 departure_date = (departure_date_from_start + timedelta(days=i)).strftime("%Y-%m-%d")

#                 # Build the updated URL with the new origin, destination, and dates for Megabus
#                 url = f"https://uk.megabus.com/journey-planner/api/journeys?originId={origin_id}&destinationId={destination_id}&departureDate={departure_date}&totalPassengers=1&concessionCount=0&nusCount=0&otherDisabilityCount=0&wheelchairSeated=0&pcaCount=0&days=1"

#                 # Data from requestor with headers
#                 response = requests.get(url, headers=headers, verify=False)

#                 # Check the response
#                 if response.status_code == 200:
#                     data = response.json()  # Parse the JSON data
#                     print(f"Data retrieved for {origin_id} to {destination_id} on {departure_date}")
#                 else:
#                     print(f"Failed to retrieve data for {origin_id} to {destination_id} on {departure_date}: {response.status_code}")
#                     continue  # Skip the iteration if the request fails

#                 # List to store the extracted information for this iteration
#                 quotes_list = []

#                 # Extract journey information
#                 for journey in data['journeys']:
#                     service_id = journey['journeyId']
#                     departure_time = journey['departureDateTime']
#                     arrival_time = journey['arrivalDateTime']
#                     duration = journey['duration']
#                     price = journey['price']

#                     # Origin and destination details
#                     origin_name = journey['origin']['cityName']
#                     origin_code = journey['origin']['cityId']
#                     destination_name = journey['destination']['cityName']
#                     destination_code = journey['destination']['cityId']

#                     # Additional data from the leg
#                     for leg in journey['legs']:
#                         carrier = leg.get('carrier', 'megabus')  # Megabus carrier
#                         transport_type = leg.get('transportIndicator', 'coach')

#                     # Append the extracted information to the list
#                     quotes_list.append({
#                         "Origin Name": origin_name,
#                         "Origin Code": origin_code,
#                         "Destination Name": destination_name,
#                         "Destination Code": destination_code,
#                         "Departure Date": departure_time,
#                         "Arrival Date": arrival_time,
#                         "Duration": duration,
#                         "Operator": carrier,
#                         "Transport Type": transport_type,
#                         "Fare": price,
#                         "Origin ID": origin_id,
#                         "Destination ID": destination_id,
#                         "Service ID": service_id  # Service ID from Megabus
#                     })

#                 # Append the quotes from this iteration to the overall list
#                 all_quotes.extend(quotes_list)

#                 # Convert the collected data to a DataFrame
#                 df = pd.DataFrame(all_quotes)

#                 # Save the DataFrame to a CSV file after every successful request
#                 df.to_csv(output_file, index=False)
#                 print(f"Data saved to {output_file}")

#             except Exception as e:
#                 print(f"An error occurred: {e}")
#                 break  # Exit the loop if there's an error, but the data will be saved up to this point
    
#     # Pause for a few seconds after each batch to avoid overwhelming the server
#     print(f"Batch {batch_index + 1} completed. Pausing to avoid being blocked...")
#     time.sleep(30)  # Adjust the sleep time as needed (e.g., 30 seconds or more)

# # Final DataFrame (if needed for further analysis)
# print(df)




###########################
######EMBER CODE###########
###########################



# import numpy as np
# import pandas as pd
# import requests
# import json
# from datetime import datetime, timedelta
# import time
# import os

# # Initialize the starting dates
# departure_date_from_start = datetime(2024, 10, 28)
# departure_date_to_start = datetime(2024, 10, 29)

# # Define the number of days to iterate (from 2024-10-28 to 2024-11-03)
# days_to_iterate = 6

# # File to save the data
# output_file = r"C:\Users\Luis.ParraMorales\Documents\Python Code\Ana Rodriguez\Rail Fares - Web Scriping\Ember Runs\Emberquotes_data.csv"

# # Check if the file already exists (to handle appending data)
# if os.path.exists(output_file):
#     df_saved = pd.read_csv(output_file)
#     all_quotes = df_saved.to_dict('records')  # Convert to list of dicts for appending new data
# else:
#     all_quotes = []

# # Read the Excel file containing O-D pairs
# OD_pairs = pd.read_excel(r"C:\Users\Luis.ParraMorales\Documents\Python Code\Ana Rodriguez\Rail Fares - Web Scriping\NWEC - Origin and Destination List - Final.xlsx", sheet_name='O-D Fares')

# # Filter rows where Operator is Ember
# ember_rows = OD_pairs[OD_pairs['Operator'] == 'Ember']

# # Define batch size (20 ODs per batch)
# batch_size = 20

# # Split the rows into batches
# batches = [ember_rows[i:i+batch_size] for i in range(0, len(ember_rows), batch_size)]

# # Iterate over each batch of O-D pairs
# for batch_index, batch in enumerate(batches):
#     print(f"Processing batch {batch_index + 1}/{len(batches)}")
    
#     # Iterate over each row in the batch
#     for index, row in batch.iterrows():
#         origin_id = row['Origin_ID']
#         destination_id = row['Destination_ID']
        
#         # Iterate over the dates
#         for i in range(days_to_iterate + 1):
#             try:
#                 # Update the departure dates
#                 departure_date_from = (departure_date_from_start + timedelta(days=i)).strftime("%Y-%m-%dT00:00:00Z")
#                 departure_date_to = (departure_date_to_start + timedelta(days=i)).strftime("%Y-%m-%dT04:00:00Z")

#                 # Build the updated URL with the new origin, destination, and dates
#                 url = f"https://api.ember.to/v1/quotes/?origin={origin_id}&destination={destination_id}&departure_date_from={departure_date_from}&departure_date_to={departure_date_to}&include_unlisted_trips=true"

#                 # Data from requestor (disabling SSL certificate verification)
#                 response = requests.get(url, verify=False)

#                 # Check the data
#                 if response.status_code == 200:
#                     data = response.json()  # Parse the JSON data
#                     print(f"Data retrieved for {origin_id} to {destination_id} from {departure_date_from} to {departure_date_to}")
#                 else:
#                     print(f"Failed to retrieve data for {origin_id} to {destination_id} from {departure_date_from} to {departure_date_to}: {response.status_code}")
#                     continue  # Skip the iteration if the request fails

#                 # List to store the extracted information for this iteration
#                 quotes_list = []

#                 # Extract and store specific information for each quote
#                 for quote in data.get('quotes', []):  # Using get to handle cases where 'quotes' might be missing
#                     service_id = None  # Initialize Service ID variable
                    
#                     for leg in quote['legs']:  # Loop through each leg in the legs list
#                         origin_name = leg['origin']['name']
#                         origin_code = leg['origin']['code']
#                         destination_name = leg['destination']['name']
#                         destination_code = leg['destination']['code']
#                         departure_date = leg['departure']['scheduled']
#                         arrival_date = leg['arrival']['scheduled']
#                         operator = leg['description'].get('operator', 'Ember')  # Default to 'Ember' if missing
#                         fare = quote['prices']['adult']

#                         # Calculate duration
#                         departure_time = datetime.fromisoformat(departure_date.replace("Z", "+00:00"))
#                         arrival_time = datetime.fromisoformat(arrival_date.replace("Z", "+00:00"))
#                         duration = arrival_time - departure_time

#                         # Extract the trip_uid as the Service ID for the first leg of the trip
#                         if service_id is None:
#                             service_id = leg['trip_uid']  # Capture service_id from the first leg

#                         # Append the extracted information to the list
#                         quotes_list.append({
#                             "Origin Name": origin_name,
#                             "Origin Code": origin_code,
#                             "Destination Name": destination_name,
#                             "Destination Code": destination_code,
#                             "Departure Date": departure_date,
#                             "Duration": duration,
#                             "Operator": operator,
#                             "Fare": fare / 100,
#                             "Origin ID": origin_id,   # Add Origin ID
#                             "Destination ID": destination_id,  # Add Destination ID
#                             "Service ID": service_id  # Add Service ID
#                         })

#                     # If no service_id was found in the earlier legs, use the final leg's trip_uid as the Service ID
#                     if service_id is None and quote['legs']:
#                         service_id = quote['legs'][-1]['trip_uid']

#                 # Append the quotes from this iteration to the overall list
#                 all_quotes.extend(quotes_list)

#                 # Convert the collected data to a DataFrame
#                 df = pd.DataFrame(all_quotes)

#                 # Save the DataFrame to a CSV file after every successful request
#                 df.to_csv(output_file, index=False)
#                 print(f"Data saved to {output_file}")

#             except Exception as e:
#                 print(f"An error occurred: {e}")
#                 break  # Exit the loop if there's an error, but the data will be saved up to this point
    
#     # Pause for a few seconds after each batch to avoid overwhelming the server
#     print(f"Batch {batch_index + 1} completed. Pausing to avoid being blocked...")
#     time.sleep(30)  # Adjust the sleep time as needed (e.g., 30 seconds or more)

# # Final DataFrame (if needed for further analysis)
# print(df)



# #######FLIXBUS######
# ####################
# import numpy as np
# import pandas as pd
# import requests
# import json
# from datetime import datetime, timedelta
# import time
# import os
# import urllib3

# # Disable SSL warnings
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# # Initialize the starting dates
# departure_date_from_start = datetime(2024, 10, 28)
# departure_date_to_start = datetime(2024, 10, 29)

# # Define the number of days to iterate
# days_to_iterate = 6

# # File to save the data
# output_file = r"C:\Users\Luis.ParraMorales\Documents\Python Code\Ana Rodriguez\Rail Fares - Web Scriping\Flixbus Runs\Flixbusquotes_data.csv"

# # Check if the file already exists
# if os.path.exists(output_file):
#     df_saved = pd.read_csv(output_file)
#     all_quotes = df_saved.to_dict('records')
# else:
#     all_quotes = []

# # Read the Excel file containing O-D pairs
# OD_pairs = pd.read_excel(
#     r"C:\Users\Luis.ParraMorales\Documents\Python Code\Ana Rodriguez\Rail Fares - Web Scriping\NWEC - Origin and Destination List - Final.xlsx",
#     sheet_name='O-D Fares'
# )

# # Filter rows where Operator is Flixbus
# flixbus_rows = OD_pairs[OD_pairs['Operator'] == 'Flixbus']

# # Define batch size
# batch_size = 20

# # Split the rows into batches
# batches = [flixbus_rows[i:i+batch_size] for i in range(0, len(flixbus_rows), batch_size)]

# # Headers to mimic a browser request
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }

# # Iterate over each batch of O-D pairs
# for batch_index, batch in enumerate(batches):
#     print(f"Processing batch {batch_index + 1}/{len(batches)}")
    
#     # Iterate over each row in the batch
#     for index, row in batch.iterrows():
#         origin_id = str(row['Origin_ID']).strip()  # Ensure clean string
#         destination_id = str(row['Destination_ID']).strip()  # Ensure clean string
#         origin_name = row['Origin']
#         destination_name = row['Destination']
        
#         print(f"\nProcessing route: {origin_name} to {destination_name}")
#         print(f"Origin ID: {origin_id}")
#         print(f"Destination ID: {destination_id}")
        
#         # Iterate over the dates
#         for i in range(days_to_iterate + 1):
#             try:
#                 # Update the departure date with the correct format (DD.MM.YYYY)
#                 current_date = departure_date_from_start + timedelta(days=i)
#                 departure_date = current_date.strftime("%d.%m.%Y")  # Changed format to match the API requirement

#                 # Build the URL exactly as in the example
#                 url = (f"https://global.api.flixbus.com/search/service/v4/search?"
#                       f"from_city_id={origin_id}&"
#                       f"to_city_id={destination_id}&"
#                       f"departure_date={departure_date}&"  # Using the correctly formatted date
#                       f"products=%7B%22adult%22%3A1%7D&"
#                       f"currency=GBP&"
#                       f"locale=en_GB&"
#                       f"search_by=cities&"
#                       f"include_after_midnight_rides=1&"
#                       f"disable_distribusion_trips=0&"
#                       f"disable_global_trips=0")

#                 print(f"Requesting URL: {url}")  # Print URL for debugging

#                 # Make the request with headers
#                 response = requests.get(url, headers=headers, verify=False)

#                 # Check the response
#                 if response.status_code == 200:
#                     data = response.json()
                    
#                     # Check if trips exist and have results
#                     if data.get('trips') and len(data['trips']) > 0 and data['trips'][0].get('results'):
#                         # Extract journey information
#                         results = data['trips'][0]['results']
                        
#                         for journey_id, journey_info in results.items():
#                             try:
#                                 if journey_info['status'] != 'available':
#                                     continue
                                    
#                                 departure_time = journey_info['departure']['date']
#                                 arrival_time = journey_info['arrival']['date']
#                                 price = journey_info['price']['total_with_platform_fee']
#                                 duration_info = journey_info['duration']
#                                 duration_minutes = duration_info['hours'] * 60 + duration_info['minutes']
#                                 service_id = journey_info['uid']
                                
#                                 # Create quote dictionary
#                                 quote = {
#                                     "Origin Name": origin_name,
#                                     "Destination Name": destination_name,
#                                     "Departure Date": departure_time,
#                                     "Arrival Date": arrival_time,
#                                     "Duration (minutes)": duration_minutes,
#                                     "Price": price,
#                                     "Origin ID": origin_id,
#                                     "Destination ID": destination_id,
#                                     "Service ID": service_id
#                                 }
                                
#                                 all_quotes.append(quote)
                                
#                             except KeyError as ke:
#                                 print(f"Missing data in journey info: {ke}")
#                                 continue
#                             except Exception as e:
#                                 print(f"Error processing journey: {e}")
#                                 continue
                        
#                         print(f"Successfully processed data for {origin_name} to {destination_name} on {departure_date}")
#                     else:
#                         print(f"No trips found for {origin_name} to {destination_name} on {departure_date}")
#                 else:
#                     print(f"Failed to retrieve data: Status code {response.status_code}")
#                     print(f"Response content: {response.text}")  # Added to see error details
                    
#                 # Save progress after each successful request
#                 if all_quotes:  # Only save if we have data
#                     df = pd.DataFrame(all_quotes)
#                     df.to_csv(output_file, index=False)
                
#                 # Small pause between requests
#                 time.sleep(2)

#             except requests.exceptions.RequestException as e:
#                 print(f"Request error: {e}")
#                 continue
#             except json.JSONDecodeError as e:
#                 print(f"JSON parsing error: {e}")
#                 continue
#             except Exception as e:
#                 print(f"Unexpected error: {e}")
#                 continue
    
#     # Pause between batches
#     print(f"Batch {batch_index + 1} completed. Pausing...")
#     time.sleep(30)

# print("Data collection completed!")
# if all_quotes:
#     final_df = pd.DataFrame(all_quotes)
#     final_df.to_csv(output_file, index=False)
#     print(f"\nFinal dataset shape: {final_df.shape}")
#     print(f"Data saved to: {output_file}")