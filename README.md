# VISITOR ENTRY MANAGEMENT SYSTEM 
An entry management application in Django, that keeps track of visitors and notifies the host about new visitors. Post visit, visitors get detailed information about their visit. Notifications are sent via email and sms.

## TABLE OF CONTENTS:
* [Technology and Version ](#technology-and-version)
* [Requirements](#requirements)
* [Setting Up Your Project](#setting-up-your-project)
* [How the Application Works](#how-the-application-works)

## Technology and Version:
* Django 2.0 or above 
* Python 3
* Bootstrap 4
   #### Third Party Apps:
   * Twilio- Communication APIs for SMS,Voice and Video Authentication : 
   
     https://www.twilio.com 
     
     https://www.twilio.com/docs/libraries/python


##  Requirements:
 * Install Pip3 on Ubuntu: \
 ``` sudo apt install python3-pip ``` \
  ``` Note: Ensure that you have Oracle JDK 11 installed ```
 
 * Install Django on Ubuntu: \
 ``` pip3 install Django ``` \
 ``` install python django-common ``` 
 
 ## Setting Up Your Project:
 
 * Clone the repository: \
 ``` https://github.com/kopalchakravarty/entry_management_system.git ``` \
 ``` Duplicate the project ```
 
 * Install twilio api: \
 ``` pip3 install twilio ```
 
 * Add necessary fields in the **settings.py** file 
 
 
 * Switch to the project directory and set up database: \
 ``` python3 manage.py migrate```
 
 * Start development server: \
 ``` python3 manage.py runserver ```
 
 ## How the Application Works:
 
 * The site manager handles the flow of information. All necessary details must be specified in the **settings.py** file.
 
 <img src='https://user-images.githubusercontent.com/31576619/69914595-08824500-146c-11ea-9085-143c9db5d396.png'/>
 
 
 * Twilio account should be set up before use. 
 
 <img src='https://user-images.githubusercontent.com/31576619/69784894-ec1ca900-11dc-11ea-808d-5b677a76c969.png'/>
 
 Visitor enters his details using the **'+'** button upon checkin. If the supplied credentials are in a valid format, the entry is added into the database. \
 Server time is recorded as the checkin time of the visitor. 
 
 <img src='https://user-images.githubusercontent.com/31576619/69786445-774b6e00-11e0-11ea-949c-88230d2783c8.png'/>
 
 Click on the 'Visitors' button to view the database
 
 <img src='https://user-images.githubusercontent.com/31576619/69786810-225c2780-11e1-11ea-93cb-c91d3b7d8e8f.png' />
 
 Host enters his details by clicking on the **'+'** button 
 
 <img src='https://user-images.githubusercontent.com/31576619/69786994-8e3e9000-11e1-11ea-9a91-689b6c26a722.png'>
 
 The Host cannot modify his credentials himself. The site manager needs to visit the admin page and do the needful. 
 
 <img src='https://user-images.githubusercontent.com/31576619/69787372-6ac81500-11e2-11ea-9561-6629f241242a.png'/>
 
 * Upon entry of a new visitor, an email and sms is sent to the Host, the details of which are supplied by the Host,verified and hardcoded into the application code by the sitemanager. 
 
 * Upon checkout, the user can edit the checkout field corresponding to his entry.
 
 * The complete details of his visit would now be sent on his registered email id and mobile number.
 
 **For testing purpose, the Email backed is redirected to the console**
 
 **Upon successful delivery of the sms a 'success' message is displayed on the console**
 
 <img src='https://user-images.githubusercontent.com/31576619/69788498-ac59bf80-11e4-11ea-922c-dc26f58c0cbe.png'/>
 
 * The 'FROM' field holds the site manager's email address/phone number. 
 
 * The 'TO' field holds the visitor's/ host's email address/phone number as the case may be.
 
 
 
 
 
 
 
 
 
 
 
 
 
 
