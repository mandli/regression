regression
==========

Regression tests that may test code from multiple repositories.

Proposal (@rjleveque and @mandli on  7/20/13)
----------------------------------------------

Have a directory for each test suite.

Within each directory, be able to run a few "short tests" that run quickly and
produce a small quantity of output data (e.g. one set of gauge results or
solution only at final time).

Commit the small set of output data along with the code.  If a newer version of
the code gives different output that is deemed to now be "correct", commit a
new version of the output data.  (Older versions will remain in the git history.)

Also commit sufficient metadata (e.g. commit hash and/or tag from all repositories)
so that the code that created this data can be recreated easily later.
(Suggest creating a new tag of all repositories whenever a new regression test or
new output data is committed, so that it is easy to checkout the right combination of
commits from all the repositories to recreate the "correct" version of code.)

Also have a "full test" that may run more slowly and creates much more output,
e.g. many frames of the solution.  Do not commit the output from these tests,
instead perform regression against these by checking out the tagged versions
and re-running the "correct" version at the time of testing.
(Or archive these results in a database outside of github so that this
repository does not grow to be huge as more tests and "correct" versions are
added in the future.)

The full test could be run if the short test fails in order to try to see what
went wrong.  (Or the archived data retrieved from elsewhere.)

All full tests should be run before any new official release.

All short tests relevant to a given repository should be run before merging a
pull request.

Create a python script for testing that makes it easy to run all the tests
relevant to a particular repository.  Integrate this eventually with a 
continuous integration server such as *Travis-CI*.

