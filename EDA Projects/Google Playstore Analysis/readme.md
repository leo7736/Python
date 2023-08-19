# Google Play Store Exploratory Data Analysis (EDA) Project 🚀📊

<!-- Project Highlights -->
<p align="center">
  <img src="https://github.com/leo7736/Python/blob/main/EDA%20Projects/Google%20Playstore%20Analysis/Google_Play_logo_PNG4.png" alt="Gplay">
</p>

I am excited to share that I've completed an EDA (Exploratory Data Analysis) project on Google Play Store analysis using Jupyter Notebook!

As part of this project, I analyzed a large dataset of apps from the Google Play Store. Using Python libraries such as Pandas, Matplotlib, and Seaborn, I performed data cleaning, transformation, and visualization tasks. I explored various aspects of the app market, including categories, ratings, reviews, and installs, to gain valuable insights into what contributes to a successful app.

## Key Findings

Here are some of the key findings from this project:

📈 The top three app categories by the number of installs are communication, social, and video players & editors.

👍 Higher ratings and more reviews tend to correlate with higher app installs, although there are some exceptions.

📉 Most apps have relatively low ratings (around 4 stars), but there are outliers with extremely high or low ratings.

Overall, this project provided a great opportunity for me to enhance my data analysis skills and gain insights into the Google Play Store ecosystem.

## Tasks

### 1. Data Clean Up – Missing Value Treatment

- Dropped records where the rating is missing since it is the target/study variable.
- Checked for null values in the Android Ver column.

### 2. Data Clean Up – Correcting Data Types

- Identified variables to be converted to numeric types.
- Cleaned the Price variable by removing the $ sign and converting it to float.
- Cleaned the Installs variable by removing ',' and '+' signs and converting it to an integer.
- Converted other identified columns to numeric.

### 3. Sanity Checks

- Ensured that the average rating falls between 1 and 5.
- Ensured that reviews are not more than installs, as only those who installed can review the app.

### 4. Identify and Handle Outliers

- Addressed outliers in the Price, Reviews, and Installs columns.

### Data Analysis to Answer Business Questions

### 5. Distribution of Ratings

- Analyzed the distribution of ratings using Seaborn.
- Explored the skewness towards higher/lower values.

### 6. Top Content Ratings

- Identified the top Content Rating values.
- Dropped values with very few records.

### 7. Effect of Size on Rating

- Made a jointplot to understand the effect of size on rating.
- Explored patterns and explained the findings.

### 8. Effect of Price on Rating

- Made a jointplot with a regression line to understand the effect of price on rating.
- Analyzed the pattern and inferred the impact of price on rating.

### 9. Numeric Interactions

- Created a pairplot with the columns: 'Reviews', 'Size', 'Rating', 'Price'.

### 10. Rating vs. Content Rating

- Made a bar plot displaying the rating for each content rating.
- Used the appropriate metric (mean, median, etc.) and plotted the results.

### 11. Content Rating vs. Size vs. Rating

- Grouped data by content rating and size buckets to get rating percentiles.
- Created a heatmap to visualize the relationships.

For more details, code implementation, and visualizations, please refer to the Jupyter Notebook associated with this project.

