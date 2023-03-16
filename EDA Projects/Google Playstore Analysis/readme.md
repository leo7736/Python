Excited to share that I've just completed an EDA (Exploratory Data Analysis) project on Google Play Store analysis using Jupyter! 🚀📊

As part of this project, I analyzed a large dataset of apps from the Google Play Store and used Python libraries like Pandas, Matplotlib, and Seaborn to perform various data cleaning, transformation, and visualization tasks. I explored different aspects of the app market, such as categories, ratings, reviews, and installs, and gained valuable insights into what makes a successful app.

Some of the key findings from this project include:

📈 The top three app categories by number of installs are communication, social, and video players & editors.

👍 Higher ratings and more reviews tend to correlate with higher app installs, but there are some exceptions.

📉 Most apps have relatively low ratings (around 4 stars), but there are some outliers with extremely high or low ratings.

Overall, this project was a great opportunity for me to practice my data analysis skills and learn more about the Google Play Store ecosystem.


## Tasks

### 1. Data clean up – Missing value treatment
###   a. Drop records where rating is missing since rating is our target/study variable
###   b. Check the null values for the Android Ver column.
### 2. Data clean up – correcting the data types
###   a. Which all variables need to be brought to numeric types?
###   b. Price variable – remove $ sign and convert to float
###   c. Installs – remove ‘,’ and ‘+’ sign, convert to integer
###   d. Convert all other identified columns to numeric
### 3. Sanity checks – check for the following and handle accordingly
###   a. Avg. rating should be between 1 and 5, as only these values are allowed on the play
###   store.
###   b. Reviews should not be more than installs as only those who installed can review the
###   app.
### 4. Identify and handle outliers –
###   a. Price column
###   b. Reviews column
###   c. Installs

##    Data analysis to answer business questions
### 5. What is the distribution of ratings like? (use Seaborn) More skewed towards higher/lower
###   values?
###   a. How do you explain this?
###   b. What is the implication of this on your analysis?
### 6. What are the top Content Rating values?
###   a. Are there any values with very few records?
###   b. If yes, drop those as they won’t help in the analysis
### 7. Effect of size on rating
###   a. Make a joinplot to understand the effect of size on rating
###   b. Do you see any patterns?
###   c. How do you explain the pattern?
### 8. Effect of price on rating
###   a. Make a jointplot (with regression line)
###   b. What pattern do you see?
###   c. How do you explain the pattern?
###   d. Replot the data, this time with only records with price > 0
###   e. Does the pattern change?
###   f. What is your overall inference on the effect of price on the rating
### 9. Look at all the numeric interactions together –
###   a. Make a pairplort with the colulmns - 'Reviews', 'Size', 'Rating', 'Price'
### 10. Rating vs. content rating
###   a. Make a bar plot displaying the rating for each content rating
###   b. Which metric would you use? Mean? Median? Some other quantile?
###   c. Choose the right metric and plot
### 11. Content rating vs. size vs. rating – 3 variables at a time
###   a. Create 5 buckets (20% records in each) based on Size
###   b. By Content Rating vs. Size buckets, get the rating (20th percentile) for each
###   combination
###   c. Make a heatmap of this
###   d. What’s your inference? Are lighter apps preferred in all categories? Heavier? Some?
