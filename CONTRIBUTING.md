# On Contributing

## git

First take a look at [github flow](https://guides.github.com/introduction/flow/)
as this page gives a good starting point on understanding how to work with `git`
in an open source repo.

**Note:**

You will need to be **a member** before making any contributions. Join the slack #go channel and ask.

### Issues

Issues can be opened on gitlab and must adhere to the provided template:

```
# Summary

Here you should include two to three sentences explaining the thought process
about the current issue. Maybe a picture? Some details that could best help someone,
especially someone new, understand the goal of the issue and how they should best
approach the problem.

## Helpful Links

Here you should include a bullet point list of links to documentation, stack overflow,
whatever, that could help guide someone on what it is they are trying to do.
Essentially, a list of links to point them in the right direction.
```

Issues will be closed if they do not adhere to the standard.

You can claim issues by asking in the #go channel whether you can work on it. The project manager will then assign them to you in gitlab.

### Branches

Each branch off of the development branch serves one and only one purpose: to
add, modify, or remove features/bugs from Go. Our list of tasks can be found on
the issues page.

If you decide to take on an issue for Go you will need to work in a branch off
of the current development branch (ie. `go-three`).

This can be done with the following chain of `git` commands within `go/`:

**Note:**

Replace `##` with the issue number that you are working on, and replace
`short-description` with a few words that in brief describe what the branch
does.

```sh
git pull
git checkout go-three
git checkout -B ##-short-description
```

**Example Workflow:**

```sh
git pull
git checkout go-three
git checkout -B 102-readme-updates
```

If you are working on something that does not have an issue please open a new
issue before creating your branch.

Once you've written commits in a branch you will need to push your commits to gitlab.

    git push origin ##-branchname

`origin` is gitlab.

### Commits & Their Messages

It is important to commit more often than not such that if we run into issues we
can narrow down which commit started to cause issues.

Commit messages should follow the format:

#### Title -

Should fill in the blank (Don't actually write "This commit", just the part that comes after!):

    This commit ______

Additionally, if you are closing an issue include:

    (Closes #issue_number_here)

Example commit title:

    Complete the about page + TOS (Closes #36)

#### Description -

Bullet points of some highlights from the commit.

They don't have to be super serious (see any of my commits) though just a tad bit of info is nice.

Example commit description:

    - Composed a short blurb on how banning works
    - Composed a description of SRCT

[Example full commit](https://git.gmu.edu/srct/go/commit/db89af2e4ffd06a6044d3301a3f7a45ced74799a)

### Merging to the current development branch

Open a [merge request](https://git.gmu.edu/srct/go/merge_requests/new)
to start the process of getting your code into the repo. Your code wil be reviewed
by another member before being merged. Your code must pass our tests and include
in the description:

    Closes #issue_number_here

[Example pull request](https://git.gmu.edu/srct/go/merge_requests/25)
