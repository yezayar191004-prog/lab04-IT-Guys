# lab04-IT-Guys

## Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Ye Zayar Aung | yezayar191004 | bank.py, test_deposit.py, .gitignore |
| Thet Htoo Naing | 6705140009-thn | test_withdraw.py |
| Paing Thu Kha Kyaw | Flexxzzzz | test_teardown.py |
| Kyawt Kay Khine | 6704140042-lgtv | test_shared.py |
| Kaung Myat Hein | kmhein122 | conftest.py |

## Our Merge Conflict

When we were all pushing changes to the same README.md file at roughly the same time, Git noticed that different members had edited the same table section. Because each person added their own row to the same part of the file, the repository had two different versions of the same lines.

This is what the conflict looked like in Git:

```text
<<<<<<< HEAD
| Ye Zayar Aung | yezayar191004 | bank.py, test_deposit.py, .gitignore |
=======
| Thet Htoo Naing | 6705140009-thn | test_withdraw.py |
>>>>>>> 123abc
```

Git could not decide automatically which version should stay because both edits were changing the same section of the file. We fixed it by reading both versions, keeping both team rows, and removing the conflict markers. In the final file, both rows remained because each row belonged to a different group member and both were correct.

## Git Contribution Summary

```text
$ git shortlog -sn
     1  Ye Zayar Aung
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
