# Summerize_and_Updated_News_post_Automation

𝙏𝙝𝙞𝙨 𝙞𝙨 𝙖𝙣 𝘼𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙤𝙣 𝙪𝙨𝙞𝙣𝙜 𝙋𝙮𝙩𝙝𝙤𝙣

𝙁𝙚𝙖𝙩𝙪𝙧𝙚𝙨: Using this project we can automatically update latest news article from various websites
         and post in blogger.
         We don't need to do anything just run the program and it will post automatically with summarize news and
         image.
         
𝙒𝙤𝙧𝙠𝙞𝙣𝙜: 1.We need to scrap latest data from various news websites(We use google news here)
         2.we use beautiful soup to extrack the news link and news heading from source.
         3.We use newspaper module to summarize the data and get the image link from the artice.(images are subject to copyright)
         4.We store newslink,heading,summarize article(body),image link in a csv file.
         5.We use newslink as a primary key to remove  redundency.(You can apply basic logic to do this)
         6.There is a blogger API to work with blogger(recommended) but here we use pyautogui.
         7.We setup pyautogui to post into blogges as our need and then extract the data from csv file and post in blogger.
         8.Here also we need to think about redundency because if we run the script again we dont want to post the same news article
           It should be unique everytime.(Use basic logic to overcome the problem)
         9.That all now run the program and sit back and watch your article posted automatically.

𝙁𝙞𝙡𝙚𝙨: For better understanding and learning we divide the code in pieces.I will tell here program workings:
       1.scrap.py : We use this script to scrap the data from source and store in correspondent csv file.
       2.check_link.py : We use this script to check the extract link is already present or not in the csv
       3.summary.py : we use this script to summarize the news article and save it to the csv.
       4.bloger_publish.py: Here the work of pyautogui work start.Now this script post the article with image and post it.
       
       𝗡.𝗕 : blogger limits daily post.so,after few post blogger stop you from posting.
       To overcome this use your own website to post content automatically.
         
        
