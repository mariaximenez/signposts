Signposts
Stay Accountable with each Post

Check out the deployed app here: https://signposts.herokuapp.com/


It's not easy to stay accountable to ourselves. When no one is looking, we grab that extra cookie or press the snooze button and miss our morning run. And most of these acts are harmless. However, a series of these acts builds a habit that can hold us back from our full potential. 

The app Signposts will help users stick to their goals. Once signed up, users can join a group aligned to their current goal. Through daily check-ins, users will stay accountable to themselves but also can help motivate and inspire others by their committment to post.




Features

Models:
User Model
Group Model
Post Model
Profile Model

Functionality
User Sign-up
User Log-in
Add self to Group
Post post/reflection to Group Page
Display username, group name, group goal on profile page

Technologies Used: Python, Django, Bulma, Postgresql database

Necessary Installations for developers:
Django Environment: 
pip3 install pipenv
pipenv install django
pipenv shell

Postgresql Database:
create db <signposts>
python3 manage.py migrate


To run server:
python3 manage.py runserver



My user has a common goal shared with friends, such as eating healthy, exercising more, quitting a bad habit like smoking, or a commitment to be more mindful, connected, or adventurous.

Users want to achieve their goals but not as a loner who clenches their fist through the process, but in a community with trusted friends to support and encourage their progress and help them process the shame of setbacks. 



Wireframes: 
[Login Page.pdf](https://github.com/mariaximenez/signposts/files/8834792/Login.Page.pdf)

[Capstone Sign Up Page.pdf](https://github.com/mariaximenez/signposts/files/8834802/Capstone.Sign.Up.Page.pdf)

![Capstone Profile Page](https://user-images.githubusercontent.com/101551729/171924428-019a3ebf-bb44-4469-8cca-70278cc4f5ff.jpg)

[GOAL PAGE.pdf](https://github.com/mariaximenez/signposts/files/8834807/GOAL.PAGE.pdf)


Data Models: 
![CAPSTONE MODEL DIAGRAM ](https://user-images.githubusercontent.com/101551729/171924350-904b5ba6-dd14-4636-88ec-f4b682d2940b.jpg)

[ERD CAPSTONE PROJECT.pdf](https://github.com/mariaximenez/signposts/files/8834790/ERD.CAPSTONE.PROJECT.pdf)
  
Home Page
<img width="1312" alt="Home Page" src="https://user-images.githubusercontent.com/101551729/173259627-0b6de69b-705c-4156-8b6d-7d83a78a56a2.png">
  
Profile Page
<img width="1185" alt="Profile Page" src="https://user-images.githubusercontent.com/101551729/173259640-357b00bc-6c80-40f1-ab91-eb981f3fe51a.png">

List of Users
<img width="859" alt="User View Page" src="https://user-images.githubusercontent.com/101551729/173259665-63379d0b-39d9-456c-bc60-8b15f3650758.png">

List of Groups
<img width="861" alt="Group Display Page" src="https://user-images.githubusercontent.com/101551729/173259695-2b7792f9-6aac-44bf-8867-3644685f281b.png">

 Description of Levels/Signposts
 ![Description of Levels](https://user-images.githubusercontent.com/101551729/173259712-789c75d8-f921-4261-9d5f-75438f3c34fe.png)
  
Posts Page
<img width="985" alt="Posts page" src="https://user-images.githubusercontent.com/101551729/173259729-ead8f8cb-05d0-4643-9048-364470d21aba.png">

  
  
  
  
  

Future features:

A comment model that is connecte to the Profile and Post Model

Group authorization that only allows group members to see posts

A reward system that tracks the number of posts and awards an icon or badge related to the user's "signpost" level



If you are interested in collaborating and helping me develop this project, please reach out to mtjimenez@gmail.com





