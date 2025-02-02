According to the Day3Notes.txt Q1,Q2

1.Creating a script to generate a file [ 001-ShellScriptProject.sh ]
2.File git-clone.sh is a script to read the input from the user ie : Providing github repo link
3.It will clone the provided github repo and then it will generate a war file inside the repo target folder.
4.It will copy the war file and paste it in the tomcat server webapps.
5.It will start the catalina.bat present in the tomacat bin folder.
6.Then we can access the File Which we have Cloned the gihtub repo in the Broswer.


#STEPS TO FOLLOW

Step1 : clone My repository by typing command.
        git clone https://github.com/RASHANTH793/ShellScripting.git
        Navigate to the Day3 folder
        Day3Notes.txt You can find the Question to the Assignment.

Step2 : 001-ShellScriptProject.sh is the Script file to create a Shell scipt
        file called git-clone.txt by using linux commands.
        
Step3 : git-clone.sh is the scipt file that will automate

Step4 : Open terminal either in Vs code or Bash

Step5 : Start the Automation by typing the command.
        sh git-clone.sh or .\git-clone.sh

Step6 : Provide the github link you want to clone.

Step7 : After tomcat server started please check war file is present in the webapps or not for your reference.

Step8 : Open Broswer and  Type localhost:8080 (default of Tomcat server)
        localhost:8080/Githubfoldername/filename

      