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

Throughout the group work, the team encountered and resolved a merge conflict while editing the same section of the README file at the same time. In collaborative Git work, this happens when different team members change the same lines before pulling the latest update.

### Conflict Markers Encountered

When Git detected two different versions of the same table section, it inserted conflict markers into the file:

```text
<<<<<<< HEAD
| Ye Zayar Aung | yezayar191004 | bank.py, test_deposit.py, .gitignore |
=======
| Thet Htoo Naing | 6705140009-thn | test_withdraw.py |
>>>>>>> 123abc
```

### Breakdown of the Markers

- `<<<<<<< HEAD` marks the beginning of the conflicting section from the current local branch.
- `=======` separates the local version from the incoming version from GitHub.
- `>>>>>>> 123abc` marks the end of the incoming change from another commit.

### Final Decision Made by the Team

The team reviewed both versions and decided to:

1. Keep all member rows that belonged to the correct group members.
2. Remove the conflict markers.
3. Keep the final table clean and readable.
4. Preserve both versions of the changed text in one merged result.

### Why Git Could Not Automatically Resolve It

Git could not resolve this automatically because both group members edited the same lines in `README.md` around the table section. Since the changes happened in the same area, Git had no clear way to know which version should remain without risking data loss. Because of that, Git stopped the merge and asked the team to resolve it manually.

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
