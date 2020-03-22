# Description

The goal of this infographic is to provide students with an understanding on how stellar classification works and how classification relates to a number of other stellar properties.  The goal is to tell a story on how classification makes
a star unique, and how it does that.  I do this by taking sample data and doing my own anaylsis from the datasets/sources to offer my own conclusions in infographic form, so that others can easily understand this topic.  

### Charts
All charts have been created with data from various scientific sources (later on in document).  The code/analysis/outputted graphs are my own. 



# Sources of Data + Citations

## Peer Reviewed Sources

Here are the sources of data and information that have been used for this infographic.  More details are listed for each respective python file where data comes from.

```
Delfosse, X. et al. "Accurate masses of very low mass stars. IV. Improved mass-luminosity relations". \aap 364. (2000): 217-224.

Eker, Z., et al. “Main-Sequence Effective Temperatures From A Revised Mass–Luminosity Relation Based On Accurate Properties.” The Astronomical Journal, vol. 149, no. 4, 2015, p. 131., doi:10.1088/0004-6256/149/4/131.

LeDrew, Glenn. “The Real Starry Sky.” Journal of the Royal Astronomical Society of Canada, vol. 95, Feb. 2001, pp. 32–33.

Habets, G.M.H.J., and J.R.W. Heintze. “Empirical Bolometric Corrections for the Main-Sequence.” Astronomy and Astrophysics Supplement Series, vol. 46, Nov. 1981, pp. 193–237.

```

--> https://ui.adsabs.harvard.edu/abs/2000A%26A...364..217D/abstract

--> https://iopscience.iop.org/article/10.1088/0004-6256/149/4/131

--> http://adsabs.harvard.edu/full/2001JRASC..95...32L      Stellar percentages.

--> http://adsabs.harvard.edu/full/1981A%26AS...46..193H    Stellar Radius



## Astronomer Sources

By American Computer Scientist Landon Curt Noll.  He is best known for discovering 25th/26th Mersenne Prime number.  He is
also an astronomer with publications in Sky and Telescope where he focuses mainly on asteroid research.

```

Curt Noll, Landon. “Stellar Classification Table - Sorted by HR Class.” Isthe, www.isthe.com/chongo/tech/astro/HR-temp-mass-table-byhrclass.html.
```

--> http://www.isthe.com/chongo/tech/astro/HR-temp-mass-table-byhrclass.html

## Image Sources
I used an image of the sun from a NASA Goddard research partner.

```
“HE II 304 A.” Solar Data Analysis Center, NASA Goddard, https://umbra.nascom.nasa.gov/images/latest_aia_304.gif?t=1584853039280.
```

# Python Files
## Star Sizes Graphic
This script exists in draw_stars.py.  Data for these stars are based on information, and rough scaling differences, of data from this journal.

```
Habets, G.M.H.J., and J.R.W. Heintze. “Empirical Bolometric Corrections for the Main-Sequence.” Astronomy and Astrophysics Supplement Series, vol. 46, Nov. 1981, pp. 193–237.
```

## HR Diagram Graphic
This script exists in plotter.py.  Data from this script is from a combination of data from the following:

```
Curt Noll, Landon. “Stellar Classification Table - Sorted by HR Class.” Isthe, www.isthe.com/chongo/tech/astro/HR-temp-mass-table-byhrclass.html.

Eker, Z., et al. “Main-Sequence Effective Temperatures From A Revised Mass–Luminosity Relation Based On Accurate Properties.” The Astronomical Journal, vol. 149, no. 4, 2015, p. 131., doi:10.1088/0004-6256/149/4/131.
```

## Class Percentages
This script exists in percentage_chart.py.  Data from this script is from a combination of data from the following: 

```
Curt Noll, Landon. “Stellar Classification Table - Sorted by HR Class.” Isthe, www.isthe.com/chongo/tech/astro/HR-temp-mass-table-byhrclass.html.

LeDrew, Glenn. “The Real Starry Sky.” Journal of the Royal Astronomical Society of Canada, vol. 95, Feb. 2001, pp. 32–33.
```