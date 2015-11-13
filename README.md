# does require ensure the correct load order of entry_points?

    pkg_resources.require("foo==1.1.0")
    pkg_resources.working_set.find(pkg_resources.Requirement.parse('foo')).activate()


http://svn.python.org/projects/sandbox/trunk/setuptools/doc/formats.txt

# Usage
http://stackoverflow.com/questions/6445167/force-python-to-use-an-older-version-of-module-than-what-i-have-installed-now