# DockerDowLog
Tool that helps to download docker logs and save them into specified folder

Instructions:
1) Download repository on machine
2) Use ``pip install -r requirements.txt``
2) Create .env file and specify required variables:
    - DOCKER_DOWLOG_APP:
      * cli - if want to launch as regular python script
    - DOCKER_CONTAINERS - comma separated list of containers names
    - DOWNLOAD_LOG_SCHEDULE - time when logs should be saved to file. Supported format: 00:00
    - FOLDER_PATH (Optional) - optional path where folder should be created. 
If not specified folder will be created in current directory.
3) Use ``python3 main.py`` command to launch script.


If you want to upload your logs to telegram instead of saving them locally:
1) Set additional variables in .env file:

   - TELEGRAM_BOT_API_KEY
   - TELEGRAM_CHAT_ID

After that, script will send logs to provided telegram chat and WILL NOT save them on disk
