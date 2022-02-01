# 721Proj1
In this project, I created a microservice that realizes continous integration and delivery.
The main tasks of the project are: 
- Create a Microservice in Flask or Fast API (I used FastAPI)
- Push source code to Github (linked in Cloud9)
- Configure Build System to Deploy changes (makefile, github actions, etc)
- Use IaC (Infrastructure as Code) to deploy code (I used apprunner)
- Use AWS

I utilized AWS's Cloud9 to write the code, IAC build, and pushed to Github.  
On Github, a workflow is set up in the Github actions.  
Then I deployed the changes to apprunner to complete the cycle.  
When one clicks on the apprunner link, they will be able to see the webpage summoned and do basic multiplication in the web-browser.  
As for testing, I set up github actions to complete the continuous integration for me.  
And in the test_main.py file, unit tests are conducted to check if the code runs fine.  
Check out the webapp deployed by Apprunner using this link: https://tkwkrbyf6z.us-east-2.awsapprunner.com
If you would like to use calculator for multiplication, use this link: https://tkwkrbyf6z.us-east-2.awsapprunner.com/multiply/2/4
Thank you very much!