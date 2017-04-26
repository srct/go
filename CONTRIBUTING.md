# On Contributing

## git

First take a look at [github flow](https://guides.github.com/introduction/flow/)
as this page gives a good starting point on understanding how to work with `git`
in an open source repo.

**Note:**

You will need to be a member before making any contributions. Join the slack #go channel and ask nicely.

### Branches

Each branch off of the development branch serves one and only one purpose: to
add, modify, or remove features/bugs from Go. Our list of tasks can be found on
the issues page.

If you decide to take on an issue for Go you will need to work in a branch off
of the current development branch (ie. `2.2-dev` with 2.2 being the version in
    development).

This can be done with the following chain of `git` commands within `go/`:

    git pull
    git checkout 2.2-dev
    git checkout -B ##-shortdescription


**Note:**

Replace `##` with the issue number that you are working on, and replace
`shortdescription` with a few words (<=4) that in brief describe what the branch
does.

**Example:**

    git pull
    git checkout 2.2-dev
    git checkout -B 102-readmeUpdates

If you are working on something that does not have an issue please open a new
issue before creating your branch.

### Commits & Their Messages

It is important to commit more often than not such that if we run into issues we
can narrow down which commit started to cause issues.

Commit messages should follow the format:

#### Title -

Should fill in the blank:

    This commit ______

Additionally, if you are closing an issue include:

    (Closes #issue_number_here)

Example commit title:

    Complete the about page + TOS (Closes #36)

#### Description -

Bullet points of some highlights from the commit.

They don't have to be super serious (see any of my commits) though just a tad bit of info is nice.

Example commit description:

    - mostly talk about how great SRCT (and :dhaynes:) is
    - plus a short blurb on how we can ban you

[Example full commit](https://git.gmu.edu/srct/go/commit/db89af2e4ffd06a6044d3301a3f7a45ced74799a)

### Merging to the current development branch

Once you've finished work in a branch you will need to push your commits to gitlab.

    git push origin ##-branchname

`Origin` is gitlab.

Open a [merge request](https://git.gmu.edu/srct/go/merge_requests/new)
to start the process of getting your code into the repo. Your code wil be reviewed
by another member before being merged. Your code must pass our tests and include
in the description:

    Closes #issue_number_here

[Example pull request](https://git.gmu.edu/srct/go/merge_requests/25)
