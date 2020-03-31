# python-extract-journal.py
I have a journal written in Google Docs. The plan is to migrate this from Google Docs to [ghost blog](https://ghost.org/).

1. Go to Google Docs
2. Download as `Plain Text`
3. Open in Note++
4. From the `Encoding` menu, select `Convert to UTF-8-BOM via`
5. Save
6. Run this Python script

# Bugs

1. Manually run once per entry, because an infinite while-loop doesn't work without `exit()` at the end of the function. The code I wrote is bad and continues to write to `loopFile`
