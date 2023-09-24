Command line for the win

Here are the steps I follow:

1. I take the screenshots of the completed level.
2. I open my terminal or command prompt on my local machine.
3. I navigate to the folder where the file to be uploaded is stored:
   -PS C:\Users\Ibn Uxair\Desktop> cd ALX
4. I connect to my Sandbox using SFTP:
   -sftp f3b77fcbf2e4@f3b77fcbf2e4.05ecbdd3.alx-cod.online
   -then enter my sandbox password.
5. I navigate to the Destination Directory:
   -/root/alx-system_engineering-devops/command_line_for_the_win/
6. I upload the file using put command:
   - put 0-first_9_tasks.jpg
7. I list the files:
   -ls
8. I exit:
   -exit