# Codemy_BarzderFlasker
Flasker blog website built by initially following Codemy's youtube tutorial
Demo: https://blog.barzdermania.de

This Website was originally created following the tutorial on youtube from Codemy https://codemy.com/:

https://www.youtube.com/embed/videoseries?si=3M9k5v6Wzp5iElhk&amp;list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz


I have modified it quite a bit.

Using the https://getbootstrap.com frontend toolkit I built out from the tutorial, testing different things and building specific things I want to use on another project of mine.
I am using a MariaDB database running on another server. This implementation is not to easy, as there are additional steps to be taken apart from "pip install -r requirements.txt".
The requirements.txt does not hold the packages for the mariaDB connection. Feel free to search the internet for your solution and install the required packages for your DB.

There are some packages and files that are not necessary anymore, that were used during the tutorial or my trials. I did not clean out all the files.
I have optimized some parts of the website for use with mobile devices, especially the navbar. But other elemnts are not perfectly adapted for mobile devices, like the single bolg post site and user dashboard / about author page. As I do not plan to use this website as a "production" website I do not want to pour in the time for all these tedious changes.


## Feel free to clone this repository and play around with it. Just remember to set up your preffered database and install its dependencies...

### There is a YAML file, where a secret key and the database connection has to be set by yourself once.
Copy the "config_template.yml" to "config.yml" and enter your personal data in that file.
The "config.yml" file is part of the ".gitignore" file and will not be uploaded to git.
