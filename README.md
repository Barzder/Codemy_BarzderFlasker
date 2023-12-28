# Codemy_BarzderFlasker
Flasker blog website built by initially following Codemy's youtube tutorial

This Website was originally created following the tutorial on youtube from Codemy:
https://www.youtube.com/embed/videoseries?si=3M9k5v6Wzp5iElhk&amp;list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz


I have modified it quite a bit.

Using the getbootstrap.com frontend toolkit I built out from the tutorial, testing different things and building specific things I want to use on another project of mine.
I am using a MariaDB database running on another server. This implementation is not to easy, as there are additional steps to be taken apart from "pip install -r requirements.txt".
The requirements.txt does not hold the packages for the mariaDB connection. Feel free to search the internet for your solution and install the required packages for your DB.


Fell free to clone this repository and play around with it. Just remember to set up your preffered database and install its dependencies...

There is be a YAML file, where a secret key and the database connection has to be set by yourself once.
Copy the "config_template.yml" to "config.yml" and enter your personal data in that file.
The "config.yml" file is part of the ".gitignore" file and will not be uploaded to git.
