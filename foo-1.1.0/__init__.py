"""
# does require ensure the correct load order of entry_points?
pkg_resources.require("foo==1.1.0")
pkg_resources.working_set.find(pkg_resources.Requirement.parse('foo')).activate()
"""

import bar


def foofy():
    return "meh"
