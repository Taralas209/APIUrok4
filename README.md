# Space Telegram

This project contains several scripts to download images from NASA's Astronomy Picture of the Day (APOD), NASA's Earth Polychromatic Imaging Camera (EPIC), and SpaceX's latest launches. The downloaded images can be published to a Telegram channel either on-demand or at regular intervals. A utility script `common_scripts.py` provides helper functions for folder creation and file extension retrieval.

## How to install

1. Get your NASA API key from [https://api.nasa.gov/](https://api.nasa.gov/).
2. Get your Telegram API key by creating a new bot using the [BotFather](https://core.telegram.org/bots#botfather).
3. Clone the repository and create a `.env` file in the project root directory with the following contents:

`NASA_API_KEY=your_nasa_api_key`\
`TELEGRAM_API_KEY=your_telegram_api_key`\
`TELEGRAM_CHANNEL_ID`


4. Python3 should be already installed. Then use `pip` (or `pip3`) to install dependencies:

`pip install -r requirements.txt`


## Usage

### 1. Script `fetch_nasa_apod.py`

This script downloads images from NASA's Astronomy Picture of the Day (APOD) and saves them to a local folder.

#### Functions

- `fetch_nasa_apod(folder_path, nasa_token, count=5)`: The main function of the script that takes the following parameters:
  - `folder_path`: The Path object where the downloaded images will be saved.
  - `nasa_token`: Your NASA API key.
  - `count`: The number of images to download (default: 5). The script fetches a random selection of images if not specified.

#### How to run

You can run the script from the console using the following command:

`python fetch_nasa_apod.py [--count COUNT]`

#### Arguments

- `--count COUNT:` (Optional) The number of images to download. If not specified, the default value is 5.


### 2. Script `fetch_nasa_epic.py`

This script downloads images from NASA's Earth Polychromatic Imaging Camera (EPIC) and saves them to a local folder.

#### Functions

- `fetch_nasa_epic(folder_path, nasa_token)`: The main function of the script that takes the following parameters:
  - `folder_path`: The Path object where the downloaded images will be saved.
  - `nasa_token`: Your NASA API key.

#### How to run

You can run the script from the console using the following command:

`python fetch_nasa_epic.py`

#### Arguments

This script does not accept any command line arguments.


### 3. Script `fetch_spacex_images.py`

This script downloads images related to SpaceX's latest or specified launch and saves them to a local folder.

#### Functions

- `fetch_spacex_images(folder_path, launch_id)`: The main function of the script that takes the following parameters:
  - `folder_path`: The Path object where the downloaded images will be saved.
  - `launch_id`: (Optional) The ID of the SpaceX launch for which images should be downloaded. If not specified, images from the latest launch will be downloaded.

#### How to run

You can run the script from the console using the following command:

`python fetch_spacex_images.py [--launch_id LAUNCH_ID]`

#### Arguments

- `--launch_id LAUNCH_ID`: (Optional) The ID of the SpaceX launch for which images should be downloaded. If not specified, images from the latest launch will be downloaded.


### 4. Script ` fetch_all_images.py`

This script combines the functionality of `fetch_spacex_images.py`, `fetch_nasa_apod.py`, and `fetch_nasa_epic.py`. It downloads images from SpaceX, NASA APOD, and NASA EPIC, and saves them to a local folder.

#### How to run

You can run the script from the console using the following command:

`python fetch_all_images.py [--launch_id LAUNCH_ID] [--count COUNT]`

#### Arguments
- `--launch_id LAUNCH_ID`: (Optional) The ID of the SpaceX launch for which images should be downloaded. If not specified, images from the latest launch will be downloaded.
- `--count COUNT`: (Optional) The number of NASA APOD images to download. If not specified, the default value is 5.

This script imports and uses the functions from the individual scripts as follows:

- `fetch_spacex_images(folder_path, args.launch_id)` from `fetch_spacex_images.py` script.
- `fetch_nasa_apod(folder_path, nasa_token, args.count)` from `fetch_nasa_apod.py` script.
- `fetch_nasa_epic(folder_path, nasa_token)` from `fetch_nasa_epic.py` script.

Additionally, it uses the `create_folder` function from `common_scripts.py` to create a folder for storing the downloaded images.


### 5. Script `telegram_bot.py`

This script publishes a single image to a specified Telegram channel. The image can be selected randomly from a folder or specified by its name.

#### Functions

- `publish_image(api_key, channel_id, folder_name, image_name)`: The main function of the script that takes the following parameters:
  - `api_key`: Your Telegram API key.
  - `channel_id`: The unique identifier of the Telegram channel where the image will be published.
  - `folder_name`: The name of the folder containing images.
  - `image_name`: (Optional) The name of the image to publish. If not specified, a random image from the folder will be published.

#### How to run

You can run the script from the console using the following command:

`python telegram_bot.py [--folder_name FOLDER_NAME] [--image_name IMAGE_NAME]`


#### Arguments

- `--folder_name FOLDER_NAME`: (Optional) The name of the folder containing images. If not specified, the default folder name is 'images'.
- `--image_name IMAGE_NAME`: (Optional) The name of the image to publish. If not specified, a random image from the folder will be published.



### 6. Script `autopublish_telegram_bot.py`

This script publishes images to a specified Telegram channel at regular intervals. Images are selected randomly from a folder and published at the specified frequency.

#### Functions

- `publish_images_at_intervals(api_key, channel_id, hours_interval, folder_name)`: The main function of the script that takes the following parameters:
  - `api_key`: Your Telegram API key.
  - `channel_id`: The unique identifier of the Telegram channel where the images will be published.
  - `hours_interval`: The frequency of publication in hours.
  - `folder_name`: The name of the folder containing images.

#### How to run

You can run the script from the console using the following command:

`python autopublish_telegram_bot.py [--hours_interval HOURS_INTERVAL] [--folder_name FOLDER_NAME]`

#### Arguments
- `--hours_interval HOURS_INTERVAL`: (Optional) The frequency of publication in hours. If not specified, the default value is 4 hours.
- `--folder_name FOLDER_NAME`: (Optional) The name of the folder containing images. If not specified, the default folder name is 'images


### 7. Script `common_scripts.py`

This script contains utility functions that are shared among multiple other scripts. It is not meant to be run directly but is imported and used by the other scripts.

#### Functions
- `download_and_save_file(url, file_path, params=None)`: Sends a GET request to the provided URL (with optional parameters), checks the response status, and if it's successful, downloads the content and saves it to a file at the given path. If the response status indicates an error, it raises an HTTPError.
    - `url`: The URL for the GET request.
    - `file_path`: The path where the content from the response will be saved.
    - `params`: A dictionary of parameters to be added to the GET request (optional).


- `get_file_extension(image_url)`: Extracts and returns the file extension from a given image URL.
  - `image_url`: The URL of the image.

### How to use
  The functions in this script can be imported into other scripts and used as needed. For example, to import and use the `download_and_save_image` function, you can include the following line at the beginning of another script:
  
`from common_scripts import download_and_save_image`

Then, you can use the create_folder function in your script like this:

`download_and_save_file(url, file_path, params=None)`

Since `common_scripts.py` is a collection of utility functions, there are no command line arguments or specific instructions for running it directly.


## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
