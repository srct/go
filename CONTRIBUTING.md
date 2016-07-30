## On Contributing
<legend></legend>

### Working on Issues
First take a look at [github flow](https://guides.github.com/introduction/flow/) as this is how Go handles version control.

If you decide on taking on an already listed issue for Go you will need to work in a branch off of master.

This can be done with:

`git branch issue##`

NOTE: replace "##" with the issue number that you are working on. (ie. issue42)

and then you need to checkout that branch in order to write code in it.

`git checkout issue##`

If you are working on something that does not have an issue please open a new issue before creating your branch.

### Commits & Their Messages

It is important to commit more often than not such that if we run into issues we can narrow down which commit started to cause issues.

Commit messages should follow the format:

#### Title -
Should fill in the blank: "This commit ______"

Additionally if you are closing an issue include:

(Closes #issue_number_here)

ex.  "Complete the about page + TOS (Closes #36)"
#### Description -
Bullet points of some highlights from the commit.

They don't have to be super serious (see any of my commits) though just a tad bit of info is nice.

ex.
- mostly talk about how great SRCT (and :dhaynes:) is
- plus a short blurb on how we can ban you

[Reference](https://git.gmu.edu/srct/go/commit/db89af2e4ffd06a6044d3301a3f7a45ced74799a)
### Merging to Master
Open a [pull request](https://git.gmu.edu/srct/go/merge_requests/new) with a descriptive enough title and description and we'll take one last look at your code before merging.

[Reference](https://git.gmu.edu/srct/go/merge_requests/25)
