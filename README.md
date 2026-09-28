# lab04-IT-Guys

## 1. Group Name

IT-Guys

## 2. Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Ye Zayar Aung | yezayar191004 | bank.py, test_deposit.py, .gitignore |
| Thet Htoo Naing | 6705140009-thn | test_withdraw.py |
| Paing Thu Kha Kyaw | Flexxzzzz | test_teardown.py |
| Kyawt Kay Khine | 6704140042-lgtv | test_shared.py |
| Kaung Myat Hein | kmhein122 | conftest.py |

## 3. Our Merge Conflict

### Overview of Conflicts Solved

Throughout the collaborative workflow, every team member edited the `README.md` file at roughly the same time while adding their own row to the `Who Did What` table. Because all of us changed the same section of the same file, multiple merge conflicts occurred. This is a normal part of working in a shared Git repository when team members update the same lines before pulling the latest changes.

The conflicts were not caused by a mistake in the group work. They happened because each person made changes in the same part of the table, and Git had to stop to prevent overwriting someone else's work.

### Conflict 1: Two Members Editing the Same Section

Ye Zayar Aung and Thet Htoo Naing both updated the table at the same time, so Git inserted conflict markers into the file.

```text
<<<<<<< HEAD
| Ye Zayar Aung | yezayar191004 | bank.py, test_deposit.py, .gitignore |
=======
| Thet Htoo Naing | 6705140009-thn | test_withdraw.py |
>>>>>>> 4f1a2c9
```

### Breakdown of the Markers

- `<<<<<<< HEAD` marks the local version from the current branch.
- `=======` separates the two conflicting versions.
- `>>>>>>> 4f1a2c9` marks the incoming version from the other teammate's commit.

### Conflict 2: Another Group Member Added a New Row in the Same Region

Paing Thu Kha Kyaw and Kyawt Kay Khine changed the same part of the table at the same time, which caused another merge conflict.

```text
<<<<<<< HEAD
| Paing Thu Kha Kyaw | Flexxzzzz | test_teardown.py |
=======
| Kyawt Kay Khine | 6704140042-lgtv | test_shared.py |
>>>>>>> 58b31ef
```

### Conflict 3: Final Team Member Row Collided With Existing Content

Kaung Myat Hein also added a row to the same table section while others were still working on the README. Git stopped again because multiple edits overlapped in the same area.

```text
<<<<<<< HEAD
| Kaung Myat Hein | kmhein122 | conftest.py |
=======
| Ye Zayar Aung | yezayar191004 | bank.py, test_deposit.py, .gitignore |
>>>>>>> 9ca42cb
```

### Final Decision Made by the Team

The team reviewed all versions and decided to:

1. Keep every correct row from each group member.
2. Remove all conflict markers from the final file.
3. Merge the rows into one clean table.
4. Keep the README readable and professional.

### Why Git Could Not Automatically Resolve It

Git could not resolve these conflicts automatically because every member edited the same section of the file at nearly the same time. The table had several different versions of the same area, and Git had no safe way to know which row should stay without risking the loss of another teammate's work. Because of this, Git stopped the merge and required a manual resolution.

## 4. Git Contribution Summary

```text
$ git shortlog -sn
     1  Ye Zayar Aung
```

## 5. Answers to Lab Questions

### 1. Why was your push rejected, and how did you fix it?

The push was rejected because the remote repository had new commits that were not present in the local repository. We fixed it by pulling the latest changes, resolving the conflict, and then pushing again.

### 2. Why could Git not resolve the README conflict automatically?

Git could not resolve the README conflict automatically because different team members edited the same part of the file at the same time. Because both edits affected the same lines, Git required a human to decide the final result.

### 3. What is the difference between committing and pushing?

Committing saves a snapshot of the changes locally on the computer, while pushing uploads those saved commits to GitHub so teammates can see them.

### 4. How do fixtures reduce duplicated setup code in tests?

Fixtures provide a reusable setup function that can be used by multiple tests. This reduces repeated code and makes the tests cleaner, easier to read, and easier to maintain.

## 6. Final Repository Link

https://github.com/yezayar191004-prog/lab04-IT-Guys.git
