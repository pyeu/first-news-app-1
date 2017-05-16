# First news app - Stanford Computational Journalism template

An iteration from the First News App tutorial published on [ireapps/first-news-app](ireapps/first-news-app). Mostly, it's the same app but simplified of some software engineering conventions (`test.py`, Travis, using FrozenFlask to generate a static app) and the [tutorial documentation that was found in `/docs`](http://first-news-app.rtfd.org/)

It also contains a few boilerplate files needed to get started on Heroku:

- `runtime.txt` - [specifies the version of Python to use *other* than the default of 2.7.x](https://devcenter.heroku.com/articles/python-runtimes). Heroku officially only supports 3.6.1, but even though this lesson was written using Python 3.5, you shouldn't have any compatibility issues... 
- `Procfile` - specifies the command Heroku should run to get the app going, i.e. `python app.py`



## Requirements

- Have Python 3.x installed (preferably via Anaconda)
- Have Flask 0.11+ (this comes with Anaconda)
- Be able to access your operating system's command-line interface to run `python app.py`

### Highly suggested

- Install a text editor designed for programming, such as [Github's Atom Text Editor](https://atom.io/).
- Have an account on Heroku.



## Interesting readings related to the Los Angeles Riots

- [1992 Los Angeles riots](https://en.wikipedia.org/wiki/1992_Los_Angeles_riots)
  
  Widespread looting, assault, arson, and killings occurred during the riots, and estimates of property damage were over $1 billion. Order was only restored after members of the California Army National Guard, the 7th Infantry Division, and the 1st Marine Division were called in to stop the rioting when local police could not control the situation. In total, 58 people were killed during the riots, more than 2,000 people were injured, and more than 11,000 were arrested. LAPD chief of police Daryl Gates, who had already announced his resignation by the time of the riots, took much of the institutional blame.




- [L.A. riots by the numbers](http://www.latimes.com/local/1992riots/la-me-riots-25-years-20170420-htmlstory.html)
- [Youngest victim of the LA Riots: Baby born with bullet wound]
(http://www.foxla.com/news/local-news/249152966-story)
- [For 22 murder victims, LA Riots leave legacy of justice eluded](http://www.foxnews.com/us/2012/04/29/for-22-murder-victims-la-riots-leave-legacy-justice-eluded.html)
- [Deaths in the 1992 LA Riots - Tracked by Professor Pamela Oliver of University of Wisconsin](http://www.ssc.wisc.edu/~oliver/soc220/Lectures220/AfricanAmericans/LA%20Riot%201992%20Deaths.htm)
- [Of the 63 people killed during '92 riots, 23 deaths remain unsolved — artist Jeff Beall is mapping where they fell](http://www.latimes.com/entertainment/arts/miranda/la-et-cam-la-riots-jeff-beall-los-angeles-uprising-20170427-htmlstory.html)
- [The L.A. Riots: 25 years later](http://timelines.latimes.com/los-angeles-riots/)
- [Los Angeles riots: Remember the 63 people who died](http://latimesblogs.latimes.com/lanow/2012/04/los-angeles-riots-remember-the-63-people-who-died-.html)
- [Deaths during the L.A. riots - Spreadsheets](http://spreadsheets.latimes.com/la-riots-deaths/)


### Other readings about death and data

- [Coroner Is Said to Rule James Brady’s Death a Homicide, 33 Years After a Shooting](https://www.nytimes.com/2014/08/09/us/james-brady-s-death-ruled-a-homicide-police-say.html)
- [Video: Why was James Brady's death ruled a homicide?](http://www.latimes.com/nation/nationnow/81041387-132.html)
- [Future of Homicide Watch D.C. uncertain as Amico joins Boston Globe](https://www.poynter.org/2014/future-of-homicide-watch-d-c-uncertain-as-amico-joins-boston-globe/260868/)
- [The Memory Keeper: Homicide Watch DC](https://www.washingtonian.com/2012/02/10/the-memory-keeper-homicide-watch-dc/)
- [Reporting from analytics: Example](https://web.archive.org/web/20160331122250/http://lauraamico.tumblr.com/post/5196806316/reporting-from-analytics-example)
- [Online Investigative journalism: more on reporting through analytics](https://web.archive.org/web/20160406200406/https://lauraamico.tumblr.com/post/11316313807/online-investigative-journalism-more-on-reporting)
- [For 7 years, L.A. Times’ Homicide Report has wrested stories from grim data](https://www.poynter.org/2014/since-2007-l-a-times-homicide-report-has-wrested-stories-from-data/240349/)
- [10-Year-Old Shames the Globe into Updating Its Database of Murder Victims](http://www.bostonmagazine.com/news/blog/2015/01/09/10-year-old-shames-boston-globe-updating-database-murder-victims/)

http://www.nytimes.com/1992/05/17/us/after-the-riots-of-58-riot-deaths-50-have-been-ruled-homicides.html

### Other homicide databases

- https://projects.jsonline.com/apps/Milwaukee-Homicide-Database/
- Chicago Sun-Times http://homicides.suntimes.com/
- WISH-TV http://wishtv.com/news/homicide-tracker/
- Our World in Data https://ourworldindata.org/homicides/
- Homicide Watch Boston http://boston.homicidewatch.org/
- Murder Data http://www.murderdata.org/
- Philly Crime Mapper https://www.phillypolice.com/crime-maps-stats/
- https://mic.com/unerased/database
- http://newsinteractive.post-gazette.com/homicide/
- https://www.nytimes.com/interactive/projects/crime/homicides/map
- http://rochester.nydatabases.com/database/rochester-homicides
