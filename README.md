# THEE BLOG

#### Author: [ROWENA RONO]


* Link to live site: [Thee Blog]())

## Description
This is a flask application that allows writers to post blogs, edit and delete blogs. It also allows users who have signed up to comment on the blogs that has been posted by a writer.

## Blogs
The user would like to.... :
*  View the blog posts on the site
*  Comment on blog posts
*  View the most recent posts
* See random quotes on the site


## Behaviour Driven Development
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| View blog | Click on comment | Taken to the clicked post | Click on `Comment` | Taken to where you can comment | Signs In/ Signs Up |
| Click on `Click Add a blog` | If logged in, display form to add a blog| Redirected to the home page |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |
| Click on Sign Out | Redirects to the home page | Signs user out |


## Getting started

### Prerequisites
* python3.6
* virtual environment
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/rowenarono95/Thee-Blog
        $ cd blog

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a `start.sh` file in the root of the folder and add the following code:

        export MAIL_USERNAME=<your-email-address>
        export MAIL_PASSWORD=<your-email-password>
        export SECRET_KEY=<your-secret-key>

* Edit the configuration instance in `manage.py` from `development` to `production`
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 manage.py server
        
## Built With

* Flask
* Boostrap
* HTML

## Support and contact details
 Incase you want to contact me find me at [rowenarono@gmail.com]


### License

* [[License: MIT]](Licence.md) <rowenarono@gmail.com> 