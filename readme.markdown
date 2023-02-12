<h1 text-align="center"><h1>Twitter Users Info</h1>

<p text-align="center"><project-description>
You can use the code to find important information about Twitter users and save them in a csv file. The code and its result will help researchers who want to analyze Twitter data based on users’ personalities.
I have used the official Twitter API and three Python libraries, including Pandas, configparser, and tweepy, for getting related data. First, I read an excel file that contained Twitter usernames. After reading the file, these usernames were saved in the list.
When I ran the code, I encountered an error and found that some users had changed their usernames on Twitter. I decided to use error handling to find and save usernames that the Twitter API couldn’t find in the list because usernames had changed.
In the following step, I used Pandas to create a data frame, save the usernames data in a .csv file, and sort them by the date they’ve joined Twitter.
At the final step, you can see the numbers of users and their usernames that have not been found by the API and tweepy.
</p>

## Built With

- Python


## Author

**Hamid Jafari**

- [Github](https://github.com/hamiidjafarii "github.com/hamiidjafarii")

- [Linkedin](linkedin.com/in/hamiidjafarii "linkedin.com/in/hamiidjafarii")

## 🤝 Support

Give a ⭐️ if you like this project!
