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

During the collaborative workflow, all members edited the `README.md` file at nearly the same time while adding their own rows into the `Who Did What` table. Because everyone changed the same section of the same file, multiple merge conflicts occurred. This is a normal situation in Git when teammates work on the same file without pulling the latest version first.

The conflicts were not caused by a mistake in the team work. They happened because each person updated the same adjacent lines in the table, so Git could not decide automatically which version should remain.

### Conflict 1: Team Members Editing the Same Table Row

When Ye Zayar Aung and Thet Htoo Naing both updated the README table at the same time, Git stopped the merge and added conflict markers.

```text
<<<<<<< HEAD
| Ye Zayar Aung | yezayar191004 | bank.py, test_deposit.py, .gitignore |
=======
| Thet Htoo Naing | 6705140009-thn | test_withdraw.py |
>>>>>>> 4f1a2c9
```

### Breakdown of the Markers

- `<<<<<<< HEAD` marks the local version currently in the branch.
- `=======` separates the two conflicting versions.
- `>>>>>>> 4f1a2c9` marks the incoming version from another teammate's commit.

### Conflict 2: Another Team Member Added a Different Row in the Same Region

A second conflict happened when Paing Thu Kha Kyaw, Kyawt Kay Khine, and Kaung Myat Hein added their rows into the same table block at the same time. Because all of them changed the same area, Git could not merge them automatically.

```text
<<<<<<< HEAD
| Paing Thu Kha Kyaw | Flexxzzzz | test_teardown.py |
=======
| Kyawt Kay Khine | 6704140042-lgtv | test_shared.py |
>>>>>>> 58b31ef
```

### Final Decision Made by the Team

The team reviewed both versions and decided to:

1. Keep every correct row from every team member.
2. Remove all Git conflict markers.
3. Merge all table rows into one final, clean version.
4. Preserve the documentation in a readable and professional format.

### Why Git Could Not Automatically Resolve It

Git could not resolve these conflicts automatically because multiple teammates changed the same lines in the README file at the same time. The file had several different versions of the same section, and Git had no safe way to choose one version without risking losing someone else's work. Because of that, Git stopped and required the team to resolve the conflict manually.

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
