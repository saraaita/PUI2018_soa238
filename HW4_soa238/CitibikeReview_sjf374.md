  Citibike Review of HW4_Assignment 2 for soa238

  a. verify that their Null and alternative hypotheses are formulated correctly, and that they are state in both words and formula (with the proper definitions to accompany the formula)

  no alternative hypothesis defined
  no formula for either hypothesis

  Though the way in which the null hypothesis is formulated, it doesn't seem to be properly related to the idea statement of "Men make longer commutes than women." If this was the case, the null would state that,  "the average trip duration of men is the same or lower than the average women's trip duration"

  b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

  This notebook does drop all columns not related to the test. All that is left in the database is the trip duration and the gender- which seems to be all that is needed to continue. This person did not, however, create the averages as stated in the hypothesis. I'm not sure if this is necessary, considering the prompt. 

  c. chose an appropriate test to test _H0_ given the type of data, and the question asked.  You can refer to the flowchart of statistical tests for this in the slides, or [here](https://urldefense.proofpoint.com/v2/url?u=https-3A__www.ncbi.nlm.nih.gov_pmc_articles_PMC3116565_&d=DwIBAg&c=slrrB7dE8n7gBJbeO0g-IQ&r=j50H48qsqK5YYxEF3YLpcA&m=9WL_46DENIF1ZH5a1LelGD7QBijj5eDFR7E3maaFf_E&s=Anjt8GsZyUzPAlQCsTFIJemxur-ZZ72sULpksbwX9IU&e=), or the book Statistics in a Nutshell, or any of the resources that I shared in class.

  I think a chi Square test would be appropriate for this hypothesis. This is because the data comes from one source and the hypothesis is comparing the difference between categories within a variable

4. Write  your comments, suggestions, and suggested an appropriate statistical test, motivating your test choice, in a markdown **named CitibikeReview\_\<netID\>.md**. Suggest variations on the question, if you think it may be made more interesting.

I think this could be a very interesting hypothesis to test. I suggest the person takes more time defining the variables and parameters at which to test. It would also be helpful to think about what to do with the null gender rows. Ideally, they would be dropped. It would be important to look at the size and distribution of the samples to ensure this does case any reciprocal effects

It is also suggested to fill in "male" and "female" for the numeric values given in place of gender, so that someone would have an easier ability to review the notebook. 