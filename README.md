![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Sebastian Kefer,

31.07.2024:
Problems with git commit because of user story template commit directly in github. fix Provided by tutor support (Oisin):

"Sometimes there are conflicts between your github repository and your local one. This can happen because you made a change directly on github, or because you are working from two computers or IDEs. Here is how to do a git pull and fix and merge conflicts:
- In the terminal type git config pull.rebase false # merge
- Run the command git pull
- Type git status to see which files have a conflict that needs fixing.
- Then check those files and look for places marked with #### or <<<<. These are the areas that differ between your local files and the Github ones. Correct these areas until the code is how you need it to be.
- Save all the files you changed.
- Then in the terminal type git add .  (don't forget the . that will add all the files changed since the last time they were committed.)
- Then git commit -m "fixed merge conflict"  You will know the merge is complete because (main | MERGING)  will return to just (main)  in the terminal
- Finally git push origin main so all your files are synced up."

-> The reason the first apps were installed without corresponding git commits.

Followed the "I think therfore I blog" project -> styling thats needs to be changed:
- base.html
- index.html
- post_detail.html
- templates -> login.html/logout.html/signup.html
    -> Add log in via google?

03.08.2024:
Ran into problems with wrong migrations -> restarted the project, left issues in old repository

05.08.2024:
Blog is up to date with "I think therfore I blog" -> started custom CSS -> About page is styled for anything over 968px. Fix coming soon.