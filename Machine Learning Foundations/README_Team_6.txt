# README

--

Title
“Valuing” Our Players: Market Value Prediction of Football Players Using Machine Learning
 
Authors

Right after the title, make sure to include the authors of the project. You should include the following:

Niharika Patil, Marisa Yang, Madi Zhaksylyk
niharikp@andrew.cmu.edu, yujuy@andrew.cmu.edu, mzhaksyl@andrew.cmu.edu


--

Project Description

The European football transfer market has now become a multi-billion-dollar industry. Football clubs invest heavily in player transfers, and player values can change rapidly based on their performance, age, position and other factors. Understanding the market values of football players is essential for clubs, agents, and sponsoring companies looking to make informed decisions about player transfers and investments. Clustering players based on their performance could provide insights into the different types of players and help with player scouting, team composition, and talent development strategies. Also, based on the performance of players, clubs would want an effective algorithm to predict/classify the positions of players, which may help to identify potential recruits who match the team's tactical and strategic needs. 

Key Words: Football, goals, assists, position, market value, clustering, prediction, Champions League

Questions:

1) What is the market value of the player based on his performance statistics (goals, assists, games played, games in the Champions League, position etc.) and demographic characteristics (age, height)?
2) What is the position of the player (attack, midfield, defense) based on performance metrics, market value, and demographic characteristics?
3) What are some identifiable clusters of players based on their performance statistics (goals, assists, games, etc.), and what are the characteristics of each cluster?

Data Collection

- The link to the dataset: https://drive.google.com/file/d/1UI1c_8jNTZfzhki_NKXXyFqJmqPJdxVv/view?usp=share_link. This dataset is the one we got after cleaning and merging with other datasets. All questions for the final submission are answered using this dataset.
- The original datasets were obtained from https://data.world/dcereijo/player-scores (in February 2023). 

--

Running the Project / Getting Started

During our last submission, Data_Cleaning_Team_6_MY_MZ_NP.ipynb was where we derived the document “all_merged.csv” that we would be working on this time.

We have created separate notebooks, namely, clustering, prediction and classification. And to run each notebook, one should have the “all_merged.csv” ready, which is also prepared in our shared google drive.

Additionally, for running the notebook prediction, since we introduced a new model: eXtreme Gradient Boosting, one should have “pip install xgboost” in advance to run the code.




