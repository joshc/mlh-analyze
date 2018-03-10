# MLH Post-Hackathon Survey Analysis: Report Card
Author: Josh Chen

## Background
I recently received the survey data from the hackathon that I helped organize that had a ton of responses from hackers about our hackathon, ranging from food to venue to Wi-Fi and more. A lot of these categories had scores, so I thought I'd put together a package to compiles the numeric results of the survey into averages for easier digestion.

## Analysis
The analysis contained in this package is reasonably simple. For the categories where they ask you to rank from 1-5 or from 1-10, we take a simple average and then assign a grade based on the grading scale found here: https://en.wikipedia.org/wiki/Academic_grading_in_the_United_States. Additionally, for the categories that range from "Strongly disagree" to "Strongly Agree", we change the strings into their corresponding values from 1 to 5, respectively, and similarly assign a score.

Finally, we total up the contributions from each category, with the current heuristic being equal contributions from each category, normalized for the range of the possible choices the hackers could have been made, and assign a final letter grade corresponding to the grading scale in the link above.

## Intended Use
The intended use is for hackathon organizers who want to get a brief overview in a semi-familiar format (i.e. report card) to know what areas they did well on and what areas can be improved, in a general sense.

## Further Suggestions
To take full advantage of the results of the surveys, I suggest you read the comments provided by the hackers to get a more specific list of things that could have gone better during the event. Feel free to reach out to me (josh[at]joshchen.me) if you have any questions. Remember that this grade should just be used as a general guideline for improving your hackathon, and more specific fixes will come only from introspection.

## Last Notes
If you get an error with utf-8 encoding, open up the .csv file in Excel and save as CSV-delimited with UTF-8 encoding. The hackathon name must also be the name of the file + '.csv' in order to be parsed correctly. Template data has been provided from a hackathon for reference. Run by
    ./analyze.py hackathon_name
