# lab04-IT-Guys

## Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Ye Zayar Aung | yezayar191004 | bank.py, test_deposit.py ,.gitignore|
|Thet Htoo Naing  | 6705140009-thn | test_withdraw.py |
| Paing Thu Kha Kyaw | Flexxzzzz | test_teardown.py |
| Kyawt Kay Khine | 6704140042-lgtv| test_shared.py |
| Kaung Myat Hein | kmhein122 | conftest.py |
## Our Merge Conflict

During the collaborative README update, Git detected that two different edits were being made to the same section of the file. The conflict markers looked like this:

```text
<<<<<<< HEAD
| Avaxmeom | yezayar191004 | bank.py, test_deposit.py, test_withdraw.py, test_teardown.py, test_shared.py, conftest.py |
=======
| Another Contributor | another-user | README.md |
>>>>>>> main
```

The final version kept the row that accurately reflected the current repository state and removed the conflict markers. Git could not resolve the conflict automatically because both versions changed the exact same lines in the table, so Git needed a human to choose the correct final result.

## Git Contribution Summary

```text
$ git shortlog -sn
     4  Avaxmeom
```

## Reflection Questions

1. Why was your push rejected, and how did you fix it?  
   A push can be rejected when GitHub has newer commits than your local repository. I fixed it by pulling the latest changes, resolving any differences, and then pushing again.

2. Why could Git not resolve the README conflict automatically?  
   Git could not decide between two different edits to the same lines, so it paused and required a human to merge the two versions manually.

3. What is the difference between committing and pushing?  
   A commit saves a snapshot in the local repository, while pushing uploads those saved commits to the remote GitHub repository so teammates can see them.

4. How do fixtures reduce duplicated setup code in tests?  
   Fixtures provide a reusable setup function, so tests can share the same object creation and initialization logic without rewriting it in every test.
