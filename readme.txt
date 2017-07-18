1. This script can be used to scrape Jenkins RSS feed.
2. Upon successful run this job displays the name and trigger time of Jenkins jobs that ran on previous day.
3. This job uses BeautifulSoup hence bs4 pip installation is mandatory.
4. Below is the format to execute this job
   python JeniinsRSSScrappingWithPython.py 'http://JenkinsHost:JenkinsPort' 'JenkinsUser' 'JenkinsUserPassword'
