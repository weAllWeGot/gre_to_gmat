# gre_to_gmat

A package to convert from GRE scores to equivalent (roughly) GMAT scores.

Table and equation are from [mbacrystalball.com](https://www.mbacrystalball.com/blog/2014/01/23/gre-to-gmat-score-conversion/
)



## Installation

```
sudo pip install gre2gmat
```

## Usage

```
>>> from gre2gmat.conversions import gre2gmat
>>> gre2gmat(gre_verbal=170,gre_quant=160)
700
>>> gre2gmat(gre_verbal=170,gre_quant=161)
710
>>> gre2gmat(gre_verbal=170,gre_quant=162)
730
```

## Contributing
Its still pretty early but if you have suggestions, thoughts, feedback, criticism, etc feel free to open a PR or submit an Issue.

Thanks in advance 😊

-------------------------------------

### gre2gmat in the wild


##### Handicapping EVERYONES MBA Odds (according to Poets & Quants)
Made this as a building block for a [much more interesting project!](https://github.com/weAllWeGot/poets_quants_handicap/)

This project is still a work in progress but its essentially a webscrape of an MBA website where a former admissions officer gives people the odds that they'll get into certain programs across the country. The webscrape is used to build a dataset of applicant profiles. The applicant profiles will be fed into a linear regression model and used to teach a model how to predict someones chances of getting into different business schools based on their profile. uses the most basic of features, GMAT or GMAT equivalent (the point of this repository), GPA, school, major, gender, race. Obviously a lot more goes into an admission decision, but this is still fun to do. Since I'm assuming people don't want to read all 200+ profiles looking for someone with a similar profile to them. I think there's real demand for this because the comments in those articles are overflowing with people posting their profiles and waiting for the website to do a feature on them. 

-----------------------------------------------

### Donating
If ya feeling generous, hollr @ the kid ❤️

https://www.paypal.me/hijodelsol

**BTC: 3EbMygEoo8gqgPHxmqa631ZVSwgWaoCj3m**

**ETH: 0x2F2604AA943dB4E7257636793F38dD3B1808A9e7**

**LTC: MQVgzNDgw43YzyUg3XmH3jQ7L8ndVswmN3**

