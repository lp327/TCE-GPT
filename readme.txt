chat.py
Step 1 : We have to install the respective packages
         [Make sure you have latest python version]

         pip install gpt_index
         pip install OpenAI
         pip install googletrans

Step 2 : There is a doc folder from which the GPT model trains and tunes to the large data. So, add the respective pdfs from which you want the esponses from TCE GPT, here we handed in HandBook and faculty details of TCE.

Step 3 : Run the file [chat.py] which tells us the no of tokens available and creates index.json file from which responses are created.


app.py
This py file uses flask in backend to integrade the method from chat.py to receive input or pass output and renders them to the front end html which is defiled in templates folder.

Step 1 : Install the packages
         pip install flask
         pip install flask_cors

Step 2 : Run the file [app.py] which gives you the link to local host where you click the link and you can see the  TCE home page with bot icon at bottom left corner.