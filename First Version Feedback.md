Version 1 of document_updater is off to a strong start, and it handled well in a lot of the tests I ran in my first session. However, I did identify some defects, some of which have a significant impact on document_updater's functionality/reliability, and the user experience. I've raised these via the GitHub repository, and listed them here for ease of reference:

### Defects
Repository issues link: https://github.com/PhilipRidgers/document_updater/issues

#1 No Error Handling for Error Caused by Empty allowlist
#2 allowlist Will not Work Properly if it Contains More Than 64 Files
#3 document_updater Cannot handle Non-Alpha Characters in Filenames
#4 The Third Line of Addresses is Merged When droplist Doesn't Contain a Document's Name

My thanks go to the developers for the hard work they've already put into document_updater, and for the accompanying descriptions and diagram. These made it a lot easier to understand the intended functionality, and allowed me to start planning my testing session sooner rather than later.